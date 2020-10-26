from Command.Startbuild.Option.Option import Option


class Stage(Option):
    _name = "s"
    _value = None

    def __init__(self):
        super().__init__()

    def format(self):
        if self._value == 0:
            self._value = "stage"
        elif self._value == 1:
            self._value = "stage-1"
        else:
            self._value = "stage-oc-" + str(self._value)
