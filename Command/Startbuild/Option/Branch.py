from Command.Startbuild.Option.Option import Option


class Branch(Option):
    _name = "b"
    _value = "master"

    def __init__(self):
        super().__init__()