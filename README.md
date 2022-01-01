[![working](https://img.shields.io/static/v1?label=Working&message=True&color=green&style=flat-square)]()
[![issues](https://img.shields.io/github/issues/ericliclair/CPCLI?label=Issues&style=flat-square)](https://github.com/EricLiclair/CPCLI/issues)
[![license](https://img.shields.io/github/license/EricLiclair/CPCLI?label=Licens&color=pink&style=flat-square)](https://github.com/EricLiclair/CPCLI/blob/main/LICENSE)

# CPCLI
A command line tool to organize your competitive programming folders and create `.cpp` file from a template, compile, and execute them; right from your terminal.

## Installation (Local Install)
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install CPCLI.

###### Step 1: 
Clone the repo

```bash
git clone https://github.com/EricLiclair/CPCLI.git
```

###### Step 2:
Change to root directory

```bash
cd CPCLI
```

###### Step 3:
Run directly or in a virtual environment (make sure you have python >=3.8.10)

```bash
python setup.py install
```
Alternately, you can install it with pip

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
cpcli create <filename>
```
This will create a folder named `filename` in the current directory. This folder will further contain a `filename.cpp` file using a predefined template.


```console
cpcli run <filename>
```
This will create an executable in the directory `filename` using the `filename\filename.cpp` file and run it.


```console
cpcli delete <filename>
```
This will check if a subdirectory `filename` exists in the directory. If it does, it'll force remove all the content of the dir, else throws an error: `No such directory exists`

## Features
All the input output redirecting commands works fine with the `run` command. For example,

```console
cpcli run filename < input.txt
```
This will execute the output.exe using the input.txt file as input.

```console
cpcli run filename > output.txt
```
This will execute the output.exe and create output.txt with the console output of the execution.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
