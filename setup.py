from setuptools import find_packages, setup

setup(
    name='django-createproject',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'django-createproject=django_createproject.main:createproject',
        ],
    },
    include_package_data=True,
    package_data={
        'django_createproject': ['template/**/*'],
    },
    install_requires=[
        'Django>=4.0',
        'djangorestframework>=3.12',
        'python-dotenv>=0.19',
        'toml>=0.10',
    ],
    author='Mark Ma',
    description='A Django project template generator',
)
