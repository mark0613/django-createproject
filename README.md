
# Django Create Project
`django-createproject` is a Django project creation command, designed to quickly set up project templates that I frequently use. It includes additional configurations for database setup, Docker, and code formatters.


## Features
- **Config Directory**: The project's configuration files will be placed inside a `config` directory, which is created in the current working directory along with `manage.py`. This allows you to set up a virtual environment (`venv`) or Poetry before running the command, and the project will be created in the current location. You don't need to move any files around.
- **Database configuration**: Choose your database backend, and I will automatically generate the corresponding configuration in `settings.py`. Currently supported options are: `sqlite`, `mysql`, or `postgres`. Default is `sqlite`.
- **Docker support**: Optionally include a `Dockerfile` and `docker-compose.yaml` for containerization.
- **Code formatters**: Optionally include `black` and `ruff` formatters in the `pyproject.toml` configuration file.


## Installation
To install the package, run:
```bash
pip install git+https://github.com/mark0613/django-createproject.git
```


## Usage
Once installed, you can use the `django-createproject` command to create a new Django project:
```bash
django-createproject my_project --db=postgres --docker --formatter
```

### Options
- `--db`: Specify the database backend. Options are:
  - `sqlite` (default)
  - `mysql`
  - `postgres`
- `--docker`: Include a `Dockerfile` and `docker-compose.yaml` for containerization.
- `--formatter`: Include configuration for the `black` and `ruff` formatters in `pyproject.toml`.


## Example
### Normal
Create a new Django project with SQLite as the database:
```bash
django-createproject my_project
```

### Docker
Create a new Django project with SQLite as the database and Docker support:
```bash
django-createproject my_project --docker
```

### Docker & PostgreSQL
Create a new Django project with PostgreSQL as the database and Docker support:

```bash
django-createproject my_project --db=postgres --docker
```

### Docker & PostgreSQL & Formatters
Create a new Django project with PostgreSQL as the database, Docker support, and code formatters:
```bash
django-createproject my_project --db=postgres --docker --formatter
```


## License
This project is licensed under the MIT License.
