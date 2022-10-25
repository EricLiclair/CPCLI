from typer import Typer
import os
from typing import List
import shutil

this_dir, this_filename = os.path.split(__file__)

# path to template from this_dir
template_path = '/templates/template.cpp'

app = Typer()


def get_paths(file_name: str) -> List[str]:
    dir_path = os.path.join(file_name)

    _file_path = os.path.join(file_name, file_name)
    file_extension = ".cpp"

    output_path = os.path.join(file_name, "output.exe")
    file_path = _file_path + file_extension
    return dir_path, file_path, output_path


def _file_exists(file_name: str) -> bool:
    sub_directories = list(os.walk('.'))[0][1]
    return file_name in sub_directories


def _create_file_from_template(file_name: str) -> None:
    template_file_path = this_dir + template_path
    dir_path, file_path, _ = get_paths(file_name)
    try:
        if _file_exists(file_name=file_name):
          raise FileExistsError(
              f"cpcli: {file_path} already exists")
        os.mkdir(dir_path)
        shutil.copy(template_file_path, file_path)
        print("file created succesfully")
        return file_path

    except FileExistsError as err:
      print(
          f"cpcli: Cannot create file. {file_path} already exists")

    except Exception as err:
        print(
            f"cpcli: error in creating file '{file_name}'. {err}")


def _run_executable_by_file_name(file_name: str) -> None:
    _, file_path, output_path = get_paths(file_name=file_name)
    try:
        os.system(
            f'g++ {file_path} -o {output_path}')
        os.system(output_path)
    except Exception as err:
        print(err)


def _delete_directory(file_name: str) -> None:
    try:
        if _file_exists(file_name):
            shutil.rmtree(file_name)
            print(f"Deleted successfully")
        else:
            raise Exception(
                f"cpcli: cannot delete '{file_name}': No such directory exists"
            )
    except Exception as err:
        print(err)


def clean_file_name(file_name: str) -> str:
    return file_name.strip('/')


@app.command()
def create(file_name: str):
    """
    Create a new file <name>.cpp in ./file_name/file_name.cpp
    """
    file_name = clean_file_name(file_name)
    _create_file_from_template(file_name)


@app.command()
def run(file_name: str):
    """
    Runs the output file output.exe in ./file_name
    """
    file_name = clean_file_name(file_name)
    _run_executable_by_file_name(file_name)


@app.command()
def delete(file_name: str):
    """
    Removes the folder along with the contents inside it
    Warning! uses force delete
    """
    file_name = clean_file_name(file_name)
    _delete_directory(file_name)


def cpcli():
    app()
