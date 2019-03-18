class AttributeMaker:
    def __init__(self, new_name, new_return):
        self.name = new_name.replace(" ","")
        self._return = new_return

    def identify(self):
        if self._return == "String":
            self._return = '""'
        elif self._return == "Integer":
            self._return = 0
        return self._return

    def __str__(self):
        self.identify()
        return f"       self.{self.name} = {self._return}"