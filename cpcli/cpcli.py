from typing import Type
from typer import Typer, echo
from create import create_file_from_template

app = Typer()


@app.command()
def create(file_name: str):
    """
    Create a new file <name>.cpp in /filename/filename.cpp
    """
    create_file_from_template('hello')
    pass


def cpcli():
    app()
