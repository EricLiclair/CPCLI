import os
import shutil
import unittest

from cpcli.cpcli import (_create_file_from_template, _delete_directory,
                           _file_exists, clean_file_name, get_paths)

class Base:
    test_file_name_1 = "test_file_name_1"

class TestMisc(unittest.TestCase, Base):

    def test_get_paths(self):
        dir_path = os.path.join(self.test_file_name_1)
        file_path = f"{dir_path}/{self.test_file_name_1}.cpp"
        output_path = f"{dir_path}/output.exe"
        self.assertEqual(get_paths(self.test_file_name_1), (dir_path, file_path, output_path))

    def test_clean_file_name(self):
        _test_file_name_1 = self.test_file_name_1 + "/"
        cleaned_file_name = _test_file_name_1.strip('/')
        self.assertEqual(clean_file_name(_test_file_name_1), cleaned_file_name)

    def test_file_exists(self):
        # create a temporary test file
        dir_path, file_path, _ = get_paths(self.test_file_name_1)
        os.mkdir(dir_path)
        file = open(file_path, 'w')
        file.close()
        exception_file_path = _create_file_from_template(self.test_file_name_1)
        self.assertIsNone(exception_file_path)
        self.assertTrue(_file_exists(self.test_file_name_1))
        # delete file path
        shutil.rmtree(dir_path)


class TestCreate(Base):

    def test_create_file_from_template(self):
        file_path = _create_file_from_template(self.test_file_name_1)
        self.assertIsNotNone(file_path)
        self.assertTrue(os.path.isfile(file_path))
        # delete file path
        shutil.rmtree(self.test_file_name_1)


class TestDelete(Base):

    def test_delete_directory(self):
        file_path = _create_file_from_template(self.test_file_name_1)
        _delete_directory(self.test_file_name_1)
        self.assertFalse(os.path.isfile(file_path))

class TestAdditional(unittest.TestCase, Base):

    def test_create_file_from_template_with_existing_file(self):
        # Test creating a file when a file with the same name already exists
        dir_path, file_path, _ = get_paths(self.test_file_name_1)
        os.mkdir(dir_path)
        file = open(file_path, 'w')
        file.close()
        exception_file_path = _create_file_from_template(self.test_file_name_1)
        self.assertIsNone(exception_file_path)
        self.assertTrue(_file_exists(self.test_file_name_1))
        # Clean up
        shutil.rmtree(dir_path)

    def test_delete_nonexistent_directory(self):
        # Test deleting a directory that doesn't exist
        non_existent_dir = "non_existent_directory"
        self.assertFalse(os.path.exists(non_existent_dir))
        _delete_directory(non_existent_dir)  # This should not raise an error

    def test_file_does_not_exist(self):
        # Test the _file_exists function with a file that doesn't exist
        self.assertFalse(_file_exists("non_existent_file"))

    def test_clean_file_name_no_slash(self):
        # Test the clean_file_name function with a filename that doesn't contain slashes
        file_name = "test_file_name_2.cpp"
        self.assertEqual(clean_file_name(file_name), file_name)

if __name__ == '__main__':
    unittest.main()
