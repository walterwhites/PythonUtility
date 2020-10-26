from pip._vendor.distlib.compat import raw_input
import readline


class Completer:
    choices = []

    def initCompleter(self, completer):
        if 'libedit' in readline.__doc__:
            readline.parse_and_bind("bind ^I rl_complete")
        else:
            readline.parse_and_bind("tab: complete")
        delims = readline.get_completer_delims()
        readline.set_completer_delims(delims.replace('/', ''))
        readline.set_completer(completer)

    def autocomplete(self, completer, name):
        print(name)
        answer = raw_input(" > ")
        while answer not in completer.choices:
            answer = raw_input(" > ")
        return answer

    def complete(self, text, state):
        options = [x for x in self.choices if x.startswith(text)]
        try:
            return options[state]
        except IndexError:
            return None
