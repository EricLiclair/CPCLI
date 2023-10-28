import os
import shutil

from ..cpcli.cpcli import (_create_file_from_template, _delete_directory,
                           _file_exists, clean_file_name, get_paths)


class Base:
    test_file_name_1 = "test_file_name_1"


class TestMisc(Base):

    def test_get_paths(self):
        dir_path = os.path.join(self.test_file_name_1)
        file_path = f"{dir_path}/{self.test_file_name_1}.cpp"
        output_path = f"{dir_path}/output.exe"
        assert get_paths(self.test_file_name_1) == (
            dir_path, file_path, output_path)

    def test_clean_file_name(self):
        _test_file_name_1 = self.test_file_name_1 + "/"
        cleaned_file_name = _test_file_name_1.strip('/')

        assert clean_file_name(_test_file_name_1) == cleaned_file_name

    def test_file_exists(self):
        # create a temporary test file
        dir_path, file_path, _ = get_paths(self.test_file_name_1)
        os.mkdir(dir_path)

        file = open(file_path, 'w')
        file.close()

        exception_file_path = _create_file_from_template(self.test_file_name_1)
        assert exception_file_path is None
        assert _file_exists(dir_path) == True

        # delete file path
        shutil.rmtree(dir_path)


class TestCreate(Base):

    # test file_path after creation is not None
    def test_create_file_from_template(self):
        file_path = _create_file_from_template(self.test_file_name_1)

        assert file_path is not None
        assert os.path.isfile(file_path) == True

        # delete file path
        shutil.rmtree(self.test_file_name_1)


class TestDelete(Base):

    def test_delete_directory(self):
      file_path = _create_file_from_template(self.test_file_name_1)
      _delete_directory(self.test_file_name_1)

      assert os.path.isfile(file_path) == False
