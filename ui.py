class ConsoleUI:
    def __init__(self, commands, processor, readers):
        self.commands = commands
        self.processor = processor
        self.readers = readers

    def parse(self, cmd):
        parts = [part.strip() for part in cmd.split(";")]
        return parts[0], parts[1:]

    def getArguments(self, parts):
        return parts[1]

    def getCommand(self, parts):
        return parts[0]

    def readInput(self, cmd):
        cmd = self.parse(cmd)
        command = self.readers.readCommand(self.getCommand(cmd))
        args = self.processor.process(cmd)
        return command, args

    def runUi(self):
        print("""
Movie rentals management system

type [help] for a list of commands and accepted arguments
""")
        while True:
            try:
                userInput = input(">>> ")
                command, args = self.readInput(userInput)
                if self.commands.executeCommand(command, args) is False:
                    break
            except ValueError as e:
                print(e)
            except (EOFError, KeyboardInterrupt):
                print("\nTalofa!")
                break

    # Helpful for testing a single command without running input() in a loop.
    def executeInput(self, cmd):
        command, args = self.readInput(cmd)
        return self.commands.executeCommand(command, args)
