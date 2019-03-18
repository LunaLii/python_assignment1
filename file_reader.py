import re
import csv
from class_maker import ClassMaker


class FileReader:
    def __init__(self):
        self.the_file = ""
        self.class_content = []
        self.all_my_classes = []
        self.my_relationship_content = []

    def add_file(self, file_name):
        self.the_file = file_name

    def read_csv_file(self, infile_name, outfile_name):
        with open(outfile_name, "w") as my_output_file:
            with open(infile_name, "r") as my_input_file:
                [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
            my_output_file.close()
        self.the_file = outfile_name

    def read_txt_file(self):
        with open(self.the_file, "rt") as my_file:
            contents = my_file.read()
            class_results = re.split(r"class", contents)
            for result in class_results:
                self.class_content.append(result)
            ##################################################
            temp_relationship = class_results[0]
            relationship = list(filter(None,temp_relationship.split('\n')))
            relationship.remove((relationship[0]))
            self.my_relationship_content = relationship
            class_results.remove(class_results[0])
            self.class_content = class_results
        return self.class_content


    def find_classes(self):
        for class_info in self.class_content:
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


