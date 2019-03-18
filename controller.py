from file_reader import File_Reader

class Controller:
    file = File_Reader()

    def load_file(self, file):
        try:
            if ".txt" in file[-4:]:
                self.file.add_file(file)
                class_content = self.file.read_file()
            else:
                message = "incorrect file format, please see help load"
                raise NameError(message)
            return class_content
        except NameError as e:
            print(e)
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(e)


