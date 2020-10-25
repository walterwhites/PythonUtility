from pip._vendor.distlib.compat import raw_input


def integer_input(value):
    try:
        val = int(value)
        if not 0 < val < 100000:
            val = input("the branch should be a number between 0 and 100000, try again \n > ")
            integer_input(val)
        return val
    except ValueError:
        val = input("the branch should be a number, try again \n > ")
        integer_input(val)


def question(name, completer):
    completer.initCompleter(completer.complete)
    answer = raw_input(name)
    completer.autocomplete()
