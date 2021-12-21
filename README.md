[![issues](https://img.shields.io/github/issues/ericliclair/CPCLI?label=Issues&style=flat-square)](https://github.com/EricLiclair/CPCLI/issues)
[![license](https://img.shields.io/github/license/EricLiclair/CPCLI?label=License&style=flat-square)](https://github.com/EricLiclair/CPCLI/blob/main/LICENSE)
[![working](https://img.shields.io/static/v1?label=Working&message=False&color=red)]

# CPCLI

A command line tool to organize your competitive programming folders and create `.cpp` file from a template, compile, and execute them; right from your terminal.

## Installation (Local Install)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install CPCLI.

###### Step 1: 
Clone the repo
###### Step 2:
In the root directory (where `setup.py` is there) use the following command

```bash
pip install .
```
## Installation (From PyPI)
The package is not yet uploaded to PyPI. Once it's up there it will be installed using the python package manager pip.

```bash
pip install cpcli
```
## Usage

```console
cpcli create main
```
This will create a folder named `main` in the current directory. This folder will further contain a `main.cpp` file with a predefined template.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)