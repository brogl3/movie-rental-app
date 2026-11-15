from repository import RepositoryManager
from validation import Validator
from readers import InputReader
from commands import CommandHandler
from command_process import CommandProcessor
from ui import ConsoleUI


def createApplication(with_sample_data=True):
    repositories = RepositoryManager()
    if with_sample_data:
        repositories.initializeRepository()
    commands = CommandHandler(repositories)
    validator = Validator(repositories)
    validator.setCommandNames(commands.getCommands())
    readers = InputReader(validator)
    processor = CommandProcessor(commands, readers)
    ui = ConsoleUI(commands, processor, readers)
    return ui, repositories


if __name__ == '__main__':
    ui, _ = createApplication()
    ui.runUi()
