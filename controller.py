from file_reader import File_Reader
class Controller:
    x = File_Reader()
    x.add_file("uml.txt")
    x.read_file()
    x.find_classes()
    x.printProgram()
