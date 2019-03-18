from cmd import Cmd
from controller import Controller
import sys

class Command(Cmd):
    controller = Controller()

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>>"

    def do_load(self, file):
        class_content = self.controller.load_file(file)
        if class_content:
            answer = input("Do you want to display the class content?" +
                           "\n [Y/N]"
                           "\n>>>")
            if answer.upper() == "Y":
                print(class_content)
            elif answer.upper() == "N":
                print("The class content does not been displayed.")

