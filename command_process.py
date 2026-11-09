from commands import getParams
from readers import readName, readId, readMId, readCId, readRId, readDates


def process(cmd):
    codes = {
        "N": readName,
        "I": readId,
        "m": readMId,
        "c": readCId,
        "r": readRId,
        "P": readDates
    }

    expected, code = getParams(cmd[0])
    args = cmd[1]

    if len(args) != expected:
        raise ValueError("Invalid number of arguments!")

    result = []
    i = 0

    for cde in code:
        if cde == "P":
            dates = readDates((args[i], args[i + 1]))
            result.extend(dates)
            i += 2
        else:
            result.append(codes[cde](args[i]))
            i += 1

    return result # a list of all normalized and validated arguments