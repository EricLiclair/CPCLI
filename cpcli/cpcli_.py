import os
from typing import Optional
from PyInquirer import prompt
from typer import Typer, echo
from os import getcwd, mkdir, path
from typer.params import Option

app = Typer()
here = path.abspath(path.dirname(__file__))
this_dir, this_filename = os.path.split(__file__)


@app.command()
def create(file_name: str):
    """
    Create a new file <name>.cpp in /filename/filename.cpp
    """
    file_dir = '.' + path.join(here, f'/{file_name}')
    template_path = this_dir + f'/templates/template.cpp'
    print(template_path)
    os.system(f'mkdir {file_dir}')
    os.system(f'cat {template_path} > {file_dir}/{file_name}.cpp')
    echo(f'Created a file {file_name}cpp at {file_dir}')


@app.command()
def run(file_name: str, executable_name: str, run: bool = Option(False, prompt=True)):
    """
    Creates an executable for given file name and runs the executable
    """
    file_path = '.' + path.join(here, f'/{file_name}')
    if run:
        try:
            os.system(
                f'g++ {file_path} -o {executable_name} && ./{executable_name}'
            )
        except:
            print('Could not execute file')
    else:
        echo(f'Created executable {executable_name} for {file_name}')


def cpcli():
    app()

# questions = [
#     {
#         'type': 'list',
#         'name': 'choice',
#         'message': 'What do you want to do?',
#         'choices': [
#             'Option A',
#             'Option B',
#             'Option C',
#         ],
#     },
#     {
#         'type': 'list',
#         'name': 'choice',
#         'message': 'What do you want to do?',
#         'choices': [
#             'Option A',
#             'Option B',
#             'Option C',
#         ],
#     }
# ]

# answers = prompt(questions)
# print(answers)  # use the answers as input for your app
