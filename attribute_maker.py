class AttributeMaker:
    def __init__(self, new_name, new_return):
        self.name = new_name.replace(" ","")
        self._return = new_return

    def identify(self):
        if self._return == "String":
            self._return = "str"
        elif self._return == "Integer":
            self._return = int
        return self._return

    def __str__(self):
        self.identify()
        return f"       self.{self.name}: {self._return}"