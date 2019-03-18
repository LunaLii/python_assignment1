class MethodMaker:
    def __init__(self, new_name, new_return):
        self.name = new_name.replace(" ","")
        self._return = new_return

    def __str__(self):
        if self._return == ")":
            self._return = "self)"

        return f"    def {self.name} ({self._return}:\n       pass"
