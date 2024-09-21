import os
import secrets
from pathlib import Path

from django.core.management.commands.startproject import Command as StartProjectCommand

from .helpers import base, db, formatter


class CreateProjectCommand(StartProjectCommand):
    rewrite_template_suffixes = (
        ('.py-tpl', '.py'),
        ('.env-tpl', '.env'),
        ('.gitignore-tpl', '.gitignore'),
        ('Dockerfile-tpl', 'Dockerfile'),
        ('docker-compose.yaml-tpl', 'docker-compose.yaml'),
        ('README.md-tpl', 'README.md'),
    )
    project_dir = Path(os.getcwd())

    def add_arguments(self, parser):
        super().add_arguments(parser)

        # default template
        template_dir = str(Path(__file__).resolve().parent / 'template')
        parser.set_defaults(template=template_dir)

        # db
        parser.add_argument(
            '--db',
            choices=['sqlite', 'mysql', 'postgres'],
            default='sqlite',
            help='Choose the database backend (default: sqlite)',
        )

        # docker
        parser.add_argument(
            '--docker',
            action='store_true',
            help='Add Dockerfile and docker-compose.yaml for containerization',
        )

        # formatter
        parser.add_argument(
            '--formatter',
            action='store_true',
            help='Add black and ruff formatter configuration in pyproject.toml',
        )

    def handle(self, *args, **options):
        self.options = options
        secret_key = secrets.token_urlsafe(50)
        options['python_version'] = base.get_python_version()
        options['poetry_version'] = base.get_poetry_version()
        options['secret_key'] = secret_key
        options['db_config'] = db.get_databases_config(options['db'])

        super().handle(*args, **options)
        base.remove_root_folder(options['name'])
        base.render_template(self.project_dir / 'config/settings.py', **options)
        base.render_template(self.project_dir / '.env', **options)
        base.render_template(self.project_dir / 'README.md', **options)

        if options['formatter']:
            formatter.add_config_to_pyproject(self.project_dir / 'pyproject.toml')

        if options['docker']:
            base.render_template(self.project_dir / 'Dockerfile', **options)
            base.render_template(self.project_dir / 'docker-compose.yaml', **options)

        self.stdout.write(self.style.SUCCESS('Project created successfully.'))

    def list_dependencies(self):
        must_install_dependencies = {}
        if self.options['db'] == 'mysql':
            must_install_dependencies['db'] = ['mysqlclient']
        elif self.options['db'] == 'postgres':
            must_install_dependencies['db'] = ['psycopg2-binary']

        if self.options['docker']:
            must_install_dependencies['docker'] = ['gunicorn', 'uvicorn']

        if self.options['formatter']:
            must_install_dependencies['formatter'] = ['black', 'ruff']

        if must_install_dependencies:
            self.stdout.write(
                self.style.WARNING('You may need to install the following dependencies:')
            )
            for key, values in must_install_dependencies.items():
                self.stdout.write(f"  - {key}: {', '.join(values)}")
