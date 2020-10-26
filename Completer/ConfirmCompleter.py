from Completer.Completer import Completer


class ConfirmCompleter(Completer):
    choices = ['y', 'n']

    def __init__(self):
        super().__init__()