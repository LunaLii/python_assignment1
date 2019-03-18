import re
from class_maker import ClassMaker
class File_Reader:

    def __init__(self):
        self.my_file = ""
        self.my_class_content = []
        self.all_my_classes = []
        self.my_relationship_content = []

    def add_file(self, file_name):
        self.my_file = file_name

    def read_file(self):
        with open(self.my_file, "rt") as my_file:
            contents = my_file.read()
            class_results = re.split(r"class", contents)
            for result in class_results:
                self.my_class_content.append(result)
            temp_relationship = class_results[0]
            relationship = list(filter(None,temp_relationship.split('\n')))
            relationship.remove((relationship[0]))
            self.my_relationship_content = relationship
            class_results.remove(class_results[0])
            self.my_class_content = class_results
        return self.my_class_content


    def find_classes(self):
        for class_info in self.my_class_content:
            class_name = class_info.split(' ')[1]
            attributes = []
            methods = []
            relationship = []
            for line in class_info.split("\n"):
                if line.find(":") != -1:
                    attributes.append(line)
            for line in class_info.split("\n"):
                if line.find("(") != -1:
                    methods.append(line)
            for a_relationship in self.my_relationship_content:
                if a_relationship.find(class_name) != -1:
                    relationship.append(a_relationship)
            self.add_class(class_name, attributes, methods, relationship)

    def add_class(self, class_name, attributes, methods, relationship):
        new_class = ClassMaker(class_name, attributes, methods, relationship)
        new_class.add_class_attributes()
        new_class.add_class_methods()
        new_class.add_class_relationships()
        self.all_my_classes.append(new_class)

    def printProgram(self):
        for x in self.all_my_classes:
            x.print_class()