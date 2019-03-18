from file_reader import FileReader

class Controller:
    file = FileReader()

    def load_file(self, infile, temp_file=''):
        try:
            if ".txt" in infile[-4:]:
                self.file.add_file(infile)
                self.file.read_txt_file()
                self.file.find_classes()
                self.file.printProgram()
            elif ".csv" in infile[-4:]:
                self.file.read_csv_file(infile,temp_file)
                self.file.read_txt_file()
                self.file.find_classes()
                self.file.printProgram()
            else:
                message = "incorrect file format, please see help load"
                raise NameError(message)

        except NameError as e:
            print(e)
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(e)


x = Controller()
x.load_file("test.csv",temp_file='t.txt')