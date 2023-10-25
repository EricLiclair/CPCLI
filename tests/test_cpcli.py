import os
import shutil
import pytest
from ..cpcli.cpcli import (
    _create_file_from_template, _delete_directory, _file_exists,
    clean_file_name, get_paths
)

class Base:
    test_file_name_1 = "test_file_name_1"
    test_file_name_2 = "test_file_name_2"

class TestMisc(Base):

    def test_get_paths(self):
        dir_path, file_path, output_path = get_paths(self.test_file_name_1)
        assert os.path.exists(dir_path)
        assert os.path.exists(file_path)
        assert os.path.exists(output_path)

    def test_clean_file_name(self):
        file_name_with_slash = self.test_file_name_1 + "/"
        cleaned_file_name = clean_file_name(file_name_with_slash)
        assert cleaned_file_name == self.test_file_name_1

    def test_file_exists(self):
        # Ensure the file does not exist initially
        assert not _file_exists(self.test_file_name_1)

        # Create a temporary test file
        dir_path, file_path, _ = get_paths(self.test_file_name_1)
        os.mkdir(dir_path)
        file = open(file_path, 'w')
        file.close()

        # Now, the file should exist
        assert _file_exists(self.test_file_name_1)

        # Delete the file and test directory
        shutil.rmtree(dir_path)

    def test_non_existing_file(self):
        # Ensure that a non-existing file does not exist
        assert not _file_exists("non_existing_file")

class TestCreate(Base):

    def test_create_file_from_template(self):
        # Test that the file is successfully created from the template
        file_path = _create_file_from_template(self.test_file_name_1)
        assert os.path.isfile(file_path)

        # Cleanup: Delete the test directory
        shutil.rmtree(self.test_file_name_1)

    def test_create_file_already_exists(self):
        # Test creating a file that already exists
        # Create the file first
        _create_file_from_template(self.test_file_name_1)

        # Attempt to create it again and check for a FileExistsError
        with pytest.raises(FileExistsError):
            _create_file_from_template(self.test_file_name_1)

class TestDelete(Base):

    def test_delete_directory(self):
        # Create a test file and directory
        file_path = _create_file_from_template(self.test_file_name_1)

        # Verify that the file exists
        assert os.path.isfile(file_path)

        # Delete the test directory
        _delete_directory(self.test_file_name_1)

        # Verify that the file no longer exists after deletion
        assert not os.path.exists(file_path)

    def test_delete_non_existing_directory(self):
        # Test deleting a non-existing directory
        # Ensure that the directory does not exist initially
        assert not os.path.exists(self.test_file_name_2)

        # Attempt to delete it and check for a FileNotFoundError
        with pytest.raises(FileNotFoundError):
            _delete_directory(self.test_file_name_2)

# Run the tests
if __name__ == '__main__':
    pytest.main()
