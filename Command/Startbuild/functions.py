import os


def integer_input(value):
    try:
        val = int(value)
        if not 0 <= val < 100000:
            val = input("the branch should be a number between 0 and 100000, try again \n > ")
            integer_input(val)
        return val
    except ValueError:
        val = input("the branch should be a number, try again \n > ")
        integer_input(val)


def get_stage(value):
    return "-s stage-oc-" + value


def question(name, completer):
    os.system('clear')
    completer.initCompleter(completer.complete)
    answer = completer.autocomplete(completer, name)
    return answer
