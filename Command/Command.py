import subprocess
from typing import Dict, Any

from Command.Startbuild.Option.Option import Option


class Command:
    _name = None
    _attributes: Dict[Any, Option] = {}

    def build(self):
        for k, v in self._attributes.items():
            if v.getValue(v) is not None:
                self._name += " -" + k + " " + str(v.getValue(v))


    def setOption(self, option, value):
        if option in self._attributes:
            self._attributes[option] = value

    def getOption(self, option):
        if option in self._attributes.keys():
            return self._attributes[option]

    def getCommand(self):
        return self._name

    def launchCommand(self, command):
        output = subprocess.check_output(['bash', '-c', command])
