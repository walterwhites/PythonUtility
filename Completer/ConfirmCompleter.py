from Completer.Completer import Completer


class ConfirmCompleter(Completer):
    confirm = ['y', 'n']

    def __init__(self):
        super().__init__()

    def complete(self, text, state):
        options = [x for x in self.confirm if x.startswith(text)]
        try:
            return options[state]
        except IndexError:
            return None
