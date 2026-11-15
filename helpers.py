"""Stateless reusable utilities; these do not need a class."""

def isLeap(date: str):
    year = int(date.split('/')[2])
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def dateToDays(date: str):
    parts = date.split('/')
    day, month, year = (int(p.strip()) for p in parts)
    lengths = [0, 31, 28 + int(isLeap(date)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    completed = year - 1
    return (day + sum(lengths[1:month]) + completed * 365 +
            completed // 4 - completed // 100 + completed // 400)


def normalizeDate(date):
    return '/'.join(piece.strip() for piece in date.split('/'))


def isDate(date):
    parts = date.split('/') if isinstance(date, str) else []
    if len(parts) != 3 or not all(part.strip().isascii() and part.strip().isdigit() for part in parts):
        return False
    day, month, year = (int(part.strip()) for part in parts)
    if not (1 <= month <= 12 and year >= 1):
        return False
    lengths = [0, 31, 28 + int(isLeap(normalizeDate(date))), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 1 <= day <= lengths[month]


def isId(x):
    return isinstance(x, str) and x.strip().isascii() and x.strip().isdigit()


def isDatePair(d):
    return dateToDays(d[0]) <= dateToDays(d[1])
