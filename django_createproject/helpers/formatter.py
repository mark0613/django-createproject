from pathlib import Path

import toml

black_config = """
[tool.black]
include = '\\.pyi?$'
extend-exclude = '''
(
    \\.git/
    | \\.ruff_cache/
    | /logs/
    | /media/
    | /static/
    | /venv/
)
'''
line-length = 100
"""

ruff_config = """
[tool.ruff]
lint.select = [
    "Q",
    "I",
    "F401",
]
lint.exclude = [
    ".git",
    ".ruff_cache",
    "logs",
    "media",
    "static",
    "venv",
]
lint.ignore-init-module-imports = true
line-length = 100

[tool.ruff.lint.flake8-quotes]
inline-quotes = "single"
multiline-quotes = "double"
docstring-quotes = "double"
"""


def add_config_to_pyproject(pyproject_path: Path):
    if not pyproject_path.exists():
        with open(pyproject_path, 'w') as f:
            f.write('')

    with open(pyproject_path, 'r') as f:
        toml_text = f.read()
        toml_data = toml.load(f)

    content = ''

    if 'tool' not in toml_data or 'black' not in toml_data.get('tool', {}):
        content += black_config

    if 'tool' not in toml_data or 'ruff' not in toml_data.get('tool', {}):
        content += ruff_config

    content = content.strip()

    if content:
        if toml_text:
            content = '\n' + content

        content = content + '\n'
        with open(pyproject_path, 'a') as f:
            f.write(content)
