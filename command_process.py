class CommandProcessor:
    def __init__(self, commands, readers):
        self.commands = commands
        self.readers = readers

    def process(self, cmd):
        codes = {
            "N": self.readers.readName,
            "I": self.readers.readId,
            "m": self.readers.readMId,
            "c": self.readers.readCId,
            "r": self.readers.readRId,
            "P": self.readers.readDates
        }

        expected, code = self.commands.getParams(cmd[0])
        args = cmd[1]

        if len(args) != expected:
            raise ValueError("Invalid number of arguments!")

        result = []
        i = 0

        for cde in code:
            if cde == "P":
                dates = self.readers.readDates((args[i], args[i + 1]))
                result.extend(dates)
                i += 2
            else:
                result.append(codes[cde](args[i]))
                i += 1

        return result  # a list of all normalized and validated arguments
