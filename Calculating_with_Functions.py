def operator(operation, y):
    operators = {
        "plus": y + operation["number"],
        "minus": y - operation["number"],
        "times": y * operation["number"],
        "divided_by": y // operation["number"] if operation["number"] else 1,
    }
    return operators[operation["operation"]]


def number_foo(operation, n):
    return operator(operation, n) if operation else n


def zero(operation=None):
    return number_foo(operation, 0)


def one(operation=None):
    return number_foo(operation, 1)


def two(operation=None):
    return number_foo(operation, 2)


def three(operation=None):
    return number_foo(operation, 3)


def four(operation=None):
    return number_foo(operation, 4)


def five(operation=None):
    return number_foo(operation, 5)


def six(operation=None):
    return number_foo(operation, 6)


def seven(operation=None):
    return number_foo(operation, 7)


def eight(operation=None):
    return number_foo(operation, 8)


def nine(operation=None):
    return number_foo(operation, 9)


def plus(n):
    return {"operation": "plus", "number": n}


def minus(n):
    return {"operation": "minus", "number": n}


def times(n):
    return {"operation": "times", "number": n}


def divided_by(n):
    return {"operation": "divided_by", "number": n}
