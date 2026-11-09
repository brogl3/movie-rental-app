from command_process import process
from commands import executeCommand
from readers import readCommand


##################
#parsing and argument interpreting
def parse(cmd):
    parts = [part.strip() for part in cmd.split(";")]
    return parts[0], parts[1:]

def getArguments(parts):
    """
    NEEDS A PARSED COMMAND
    :param parts:
    :return:
    """
    return parts[1]

def getCommand(parts):
    """
    NEEDS A PARSED COMMAND
    :param parts:
    :return:
    """
    return parts[0]


def readInput(cmd):
    cmd = parse(cmd)
    command = readCommand(getCommand(cmd))
    args = process(cmd)

    return command, args


# input(cmd) -> cmd = parse(cmd) -> process command, process arguments...
###################

def runUi():
    while True:
        print("""
Movie rentals management system

type [help] for a list of commands and accepted arguments
""")
        try:
            userInput = input(">>> ")
            command, args = readInput(userInput)
            executeCommand(command, args)
        except ValueError as e:
            print(e)