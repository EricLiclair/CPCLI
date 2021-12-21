import os

this_dir, this_filename = os.path.split(__file__)

template_path = '/'.join(this_dir.split('/')[:-1]) + '/template/template.cpp'


def create_file_from_template(file_name: str) -> None:
    print(template_path)
