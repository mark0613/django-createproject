import sys

from .command import CreateProjectCommand


def createproject():
    command = CreateProjectCommand()
    parser = command.create_parser('django', 'createproject')
    options = parser.parse_args(sys.argv[1:])
    command.execute(**vars(options))
    command.list_dependencies()


if __name__ == '__main__':
    createproject()
