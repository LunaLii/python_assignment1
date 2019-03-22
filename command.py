from cmd import Cmd
from controller import Controller
import sys


class Command(Cmd):
    controller = Controller()

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>>"
        self.my_name = "unknown"

    def do_load(self, file):
        """
        Syntax: load [file]
        :param file: a .txt or .docx file
        :return: none
        """
        class_content = self.controller.load_file(file)
        if class_content:
            answer = input("Do you want to display the class content?" +
                           "\n [Y/N]"
                           "\n>>>")
            if answer.upper() == "Y":
                print(class_content)
            elif answer.upper() == "N":
                print("The class content does not been displayed.")

    def do_save(self,file):
        self.controller.save_file(file)

    def do_display(self, option):
        if option and option.strip():
            if option == "/a":
                self.controller.create_bar_chart()
            elif option == "/p":
                self.controller.create_pie_chart()
        else:
            print("please choose one")


if __name__ == "__main__":
    command = Command()
    command.cmdloop()

