from setuptools import setup, find_packages
from io import open
from os import path

here = path.abspath(path.dirname(__file__))

# get the dependencies
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs
                    if 'git+' in x]

setup(
    name='cpcli',
    author='Shubham Kushwaha',
    license='MIT',
    version='1.0.0',
    requires=[
        'PyInquirer',
    ],
    description='A CLI to create template file, organise folders, build and execute cpp code.',
    python_requires=">=3.8.10",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: '
    ],
    data_files=[('', 'templates/templates.cpp')],
    keywords='click, prompt-toolkit, cli, command-line, commandline, command-line-interface, python-inquiry, inquirer',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='eric.liclair@gmail.com',
    # download_url='',
    url='https://github.com/EricLiclair/CPCLI.git',
)
