from Completer.Completer import Completer


class SuiteCompleter(Completer):
    suites = ['acceptance', 'api', 'integration']

    def __init__(self):
        super().__init__()

    def complete(self, text, state):
        options = [x for x in self.suites if x.startswith(text)]
        try:
            return options[state]
        except IndexError:
            return None
