import os
import shutil

import pytest

from ..cpcli.cpcli import (_create_file_from_template, clean_file_name,
                           get_paths)


class TestMisc:
  test_file_name = "test_file_name"

  def test_get_paths(self):
    dir_path = os.path.join(self.test_file_name)
    file_path = f"{dir_path}/{self.test_file_name}.cpp"
    output_path = f"{dir_path}/output.exe"
    assert get_paths(self.test_file_name) == (dir_path, file_path, output_path)

  def test_clean_file_name(self):
    _test_file_name = self.test_file_name + "/"
    cleaned_file_name = _test_file_name.strip('/')

    assert clean_file_name(_test_file_name) == cleaned_file_name


class TestCreate:
  test_file_name = "test_file_name"

  # test file_path after creation is not None
  def test_create_file_from_template(self):
    file_path = _create_file_from_template(self.test_file_name)

    assert file_path is not None
    assert os.path.isfile(file_path) == True

    # delete file path
    shutil.rmtree(self.test_file_name)

  # test for exception while creating file
  def test_exception_create_file_from_template(self):
    # create a temporary test file
    _create_file_from_template(self.test_file_name)

    # Exception
    with pytest.raises(FileExistsError):
      exception_file_path = _create_file_from_template(self.test_file_name)
      assert exception_file_path is None

    # delete file path
    shutil.rmtree(self.test_file_name)
