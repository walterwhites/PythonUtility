class Option:
    _name = None
    _value = None

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def format(self): return None
