from cmd import Cmd
from controller import Controller

class Command(Cmd):
    controller = Controller()

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>>"
        self.my_name = "unknown"

    # Luna
    def do_load(self, file):
        """
        Syntax: load [file]
        Load the file and decide whether to display the PlantUML content or not
        :param file: a .txt or .docx file for PlantUML
        :return:
        """
        class_content = self.controller.load_file(file)
        if class_content:
            answer = input("Do you want to display the PlantUML content?" +
                           "\n [Y/N]"
                           "\n>>>")
            if answer.upper() == "Y":
                print(class_content)
            elif answer.upper() == "N":
                print("The PlantUML content does not been displayed.")

    # Clement
    def do_save(self,file):
        """
        Syntax: save [file]
        Saves the file entered (either a .txt or docx file)
        :param file: a .txt (for a text file) or .docx (for a word document) file e.g. myWordDocument.docx
        Specifies the name and file type (.txt (text file) or .docx (Microsoft Word file)) being saved. e.g. myTextDocument.txt (text file)
        :return: none
        """
        self.controller.save_file(file)

    # Rajan
    # Change commands and options: Luna: /a; Rajan: /p; Clement: /l
    def do_display(self, option):
        """
        Syntax: display [/a | /p | /l]
        Display bar chart, pie chart or line graph
        :param option: /a: display bar chart, /p: display pie chart, /l: display line graph
        :return: none
        """
        if option and option.strip():
            if option == "/a":
                self.controller.create_bar_chart()
            elif option == "/p":
                self.controller.create_pie_chart()
            elif option == "/l":
                self.controller.create_line_chart()
        else:
            print("please choose one")


if __name__ == "__main__":
    command = Command()
    command.cmdloop()

