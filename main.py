from repository import RepositoryManager
from validation import Validator
from readers import Readers
from commands import commandHandler
from command_process import Processor
from ui import consoleUi


def createApplication():
    repositories = RepositoryManager()
    commands = commandHandler(repositories)
    validator = Validator(repositories)
    validator.setCommandNames(commands.getCommands())
    readers = Readers(validator)
    processor = Processor(commands, readers)
    ui = consoleUi(commands, processor, readers)
    return ui, repositories


if __name__ == '__main__':
    ui, repos = createApplication()
    ui.runUi()
