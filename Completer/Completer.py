from pip._vendor.distlib.compat import raw_input
import readline


class Completer:

    def initCompleter(self, completer):
        readline.set_completer(completer)
        readline.parse_and_bind("tab: complete")

    def autocomplete(self):
        while 1:
            a = raw_input(" > ")
