from Command.Startbuild.Option.Option import Option


class Stage(Option):
    _name = "s"
    _value = "stage"

    def __init__(self):
        super().__init__()

    def format(self):
        if self._value == 1:
            self._value = "stage-1"
        else:
            self._value = "stage-oc-" + str(self._value)
