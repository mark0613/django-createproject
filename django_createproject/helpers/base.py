import os
import shutil
import subprocess
import sys
from pathlib import Path

from django.template import Context, Engine


def remove_root_folder(project_name: str):
    all_items = os.listdir(project_name)
    for item in all_items:
        shutil.move(f'{project_name}/{item}', item)
    shutil.rmtree(project_name)


def remove_lines_with_spaces(content: str):
    result = []
    for line in content.split('\n'):
        if len(line) > 0 and len(line.replace(' ', '')) == 0:
            continue
        result.append(line)

    return '\n'.join(result)


def render_template(template_path: Path, **kwargs: str):
    if not template_path.exists():
        return

    with open(template_path, 'r') as f:
        content = f.read()

    context = Context(kwargs)
    template = Engine().from_string(content)
    content = template.render(context)
    content = remove_lines_with_spaces(content)
    content = content.strip('\n') + '\n'

    with open(template_path, 'w') as f:
        f.write(content)


def get_python_version():
    return f'{sys.version_info.major}.{sys.version_info.minor}'


def get_poetry_version():
    try:
        result = subprocess.run(['poetry', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
    except FileNotFoundError:
        return None
    return None
