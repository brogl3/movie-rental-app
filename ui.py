class consoleUi:

    def __init__(self, commands, processor, readers):
        self.commands = commands
        self.processor = processor
        self.readers = readers

    def parse(self, cmd):
        parts = [part.strip() for part in cmd.split(";")]
        return parts[0], parts[1:]

    def getArguments(self, parts):
        """
        NEEDS A PARSED COMMAND
        :param parts:
        :return:
        """
        return parts[1]

    def getCommand(self, parts):
        """
        NEEDS A PARSED COMMAND
        :param parts:
        :return:
        """
        return parts[0]

    def readInput(self, cmd):
        cmd = self.parse(cmd)
        command = self.readers.readCommand(self.getCommand(cmd))
        args = self.processor.process(cmd)
        return command, args

    # input(cmd) -> cmd = parse(cmd) -> process command, process arguments...
    def runUi(self):
        while True:
            print("""
Movie rentals management system

type [help] for a list of commands and accepted arguments
        """)
            try:
                userInput = input(">>> ")
                command, args = self.readInput(userInput)
                self.commands.executeCommand(command, args)
            except ValueError as e:
                print(e)


##################
#parsing and argument interpreting
