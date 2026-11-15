def isLeap(d:str):
    d = d.split("/")
    y = int(d[2])
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def dateToDays(d:str):
    m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(d):
        m[2] = 29
    d = d.split("/")
    days = int(d[0])
    months = int(d[1])
    years = int(d[2]) - 1
    for i in range (1, months):
        days += m[i]
    days += years * 365 + years // 4 - years // 100 + years // 400
    return days

#

def normalizeDate(d):
    d = d.split("/")
    return d[0].strip() + "/" + d[1].strip() + "/" + d[2].strip()

def isDate(d):
    """
    Raises ValueError for invalid read dates, or return the normalized version if they're valid
    :param d:
    :return:
    """
    m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = month = year = normalized = None
    ok = True

    d = d.split("/")
    if len(d) != 3:
        ok = False
    else:

        d[0] = d[0].strip()
        d[1] = d[1].strip()
        d[2] = d[2].strip()
        if not d[0].isdigit() or not d[1].isdigit() or not d[2].isdigit():
            ok = False
        else:
            day = int(d[0])
            month = int(d[1])
            year = int(d[2])
            if not 1 <= month <= 12:
                ok = False
            else:
                normalized = d[0] + "/" + d[1] + "/" + d[2]
                if isLeap(normalized):
                    m[2] = 29
                if not (1 <= day <= m[month]) or year < 1:
                    ok = False

    return ok

def isId(x):
    x = x.strip()
    return x.isdigit()

def isDatePair(d):
    #d is a tuple
    return dateToDays(d[0]) <= dateToDays(d[1])