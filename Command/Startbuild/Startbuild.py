from Command.Command import Command
from Command.Startbuild.Option.Stage import Stage
from Command.Startbuild.Option.Branch import Branch
from Command.Startbuild.Option.TestPath import TestPath


class Startbuild(Command):
    _name = "start-build"
    _attributes: {} = {
        "s": Stage,
        "p": TestPath,
        "b": Branch,
    }

    def formatOption(self, option):
        if self._attributes[option].getValue(self._attributes[option]) is not None:
            self._attributes[option].format(self._attributes[option])
        return self

    def setOption(self, option, value):
        if option in self._attributes:
            self._attributes[option].setValue(self._attributes[option], value)
            self.formatOption(option)
