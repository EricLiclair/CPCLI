from typer import Typer
import os

this_dir, this_filename = os.path.split(__file__)

# path to template from this_dir
template_path = '/templates/template.cpp'


app = Typer()


def _create_file_from_template(file_name: str) -> None:
    template_file_path = this_dir + template_path
    os.system(f'mkdir {file_name}')
    os.system(f'cat {template_file_path} > ./{file_name}/{file_name}.cpp')


def _run_executable_by_file_name(file_name: str) -> None:
    os.system(
        f'g++ {file_name}/{file_name}.cpp -o {file_name}/output.exe')
    os.system(f'{file_name}/output.exe')
    pass


def clean_file_name(file_name: str) -> str:
    return file_name.strip('/')


@app.command()
def create(file_name: str):
    """
    Create a new file <name>.cpp in ./file_name/file_name.cpp
    """
    file_name = clean_file_name(file_name)
    _create_file_from_template(file_name)
    pass


@app.command()
def run(file_name: str):
    """
    Runs the output file output.exe in ./file_name
    """
    file_name = clean_file_name(file_name)
    _run_executable_by_file_name(file_name)
    pass


def cpcli():
    app()
