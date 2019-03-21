from fileHandler import PrintClass


class Controller:
    file = PrintClass()

    def load_file(self, infile):
        # try:
        #     if ".txt" in infile[-4:]:

                content = self.file.class_handler(infile)
                return content
            # elif ".docx" in infile[-5:]:
            #     file_content = self.file.read_word_file(infile)
            #     return self.file.class_handler(file_content)
            # else:
            #     message = "incorrect file format, please see help load"
            #     raise NameError(message)

        # except NameError as e:
        #     print(e)
        # except FileNotFoundError:
        #     print("File not found")
        # except Exception as e:
        #     print(e)

    def save_file(self,file_name):
        class_list = self.load_file(file_name)
        self.file.outputClasses(class_list)


# x = Controller()
# x.load_file("uml.txt")
# x.save_file("uml.txt")