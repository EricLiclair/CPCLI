import os
import pytest

from ..cpcli.cpcli import clean_file_name, get_paths


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
