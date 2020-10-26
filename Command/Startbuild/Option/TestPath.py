from Command.Startbuild.Option.Option import Option


class TestPath(Option):
    _name = "p"
    _value = None

    def __init__(self):
        super().__init__()