import docx
from validator import Validator


class PrintClass:

    def __init__(self):
        # self.class_file = ''
        self.relationship_list = []
        self.class_name_list = []
        self.class_list = []

    # def add_file(self,file):
    #     self.class_file = file

    #Luna   load data from .docx file
    def read_word_file(self,file_name):
        file = docx.Document(file_name)
        content = []
        for para in file.paragraphs:
            content.append(para.text + "\n")
        return content

    def read_txt_file(self,file_name):
        file = open(file_name, 'r').readlines()
        return file

    def class_handler(self,file_name):
        class_list = [[]]
        file_content = []
        if ".txt" in file_name[-4:]:  # identify the file type
            file_content = self.read_txt_file(file_name)
        elif ".docx" in file_name[-5:]:
            file_content = self.read_word_file(file_name)
        for i, m in enumerate(file_content[1:-1]):
            if m == "\n":
                if i != len(file_content[1:-1]) - 1:
                    class_list.append([])
            else:
                class_list[-1].append(m)
        self.relationship_list = class_list[0]
        self.class_list = class_list[1:]
        return self.class_list
        # return class_list

    def get_class_name(self, class_array):
        for listItem in class_array:
            if "class" in listItem:
                temp_class = listItem[:listItem.index(" {")]
                class_name = temp_class.split(' ')[1]
                self.class_name_list.append(class_name)
                return class_name

    def get_attributes(self, class_array):
        attributes = []
        for listItem in class_array:
            if ":" in listItem and "(" not in listItem:
                result = listItem.split(' ')
                attributes.append(result[4])
        return attributes

    def get_methods(self, class_array):
        methods = []
        for listItem in class_array:
            if "(" in listItem:
                methods.append(listItem[:listItem.index("\n")-2].strip())
        return methods

    def get_relationship(self, class_name):
        all_relationship = []
        for a_relationship in self.relationship_list:
            r_class_name = a_relationship.split(" ")
            first_c_name = r_class_name[0]
            second_c_name = r_class_name[-1].replace("\n", "")
            if class_name == first_c_name:
                temp_relationship = "        # "+first_c_name.lower() + ' -> ' + second_c_name.lower()
                if "many" in a_relationship:
                    temp_relationship += "[]"
                temp_relationship += "\n" + "        self." + first_c_name.lower() + " = " + "None"
                all_relationship.append(temp_relationship)
        return all_relationship

    def output_class(self, class_item):
        class_name = self.get_class_name(class_item)
        result = "class " + class_name + ":\n    def __init__(self"

        for listItem in self.get_attributes(class_item):
            result += ', ' + listItem

        result += '):\n'

        if Validator.validate_class_name(class_name):    #call the validate function
            pass
        else:
            result += "     # the class name is in wrong format \n"

        for listItem in self.get_attributes(class_item):
            result += '        self.' + listItem + ' = ' + listItem + '\n'
        for list_item in self.get_relationship(class_name):
            result += list_item + '\n'

        result += '\n'
        for listItem in self.get_methods(class_item):
            result += '    def ' + listItem + '(self):\n        # Todo: incomplete\n        pass\n'
            result += '\n'
        return result

    def outputClasses(self,class_list):
        files = []
        for classItem in class_list:
            files.append(self.get_class_name(classItem) + '.py')
        for classItem, file in zip(class_list, files):
            result = self.output_class(classItem)
            with open(file, "w") as output:
                output.write(result)
        print("files are saved")



# printClass('classDiagram.txt').class_handler()
# c = printClass('classDiagram.docx')
# c.read_word_file('classDiagram.docx')
#
# c= PrintClass()
# print(c.class_handler("uml.docx"))
# c.outputClasses()


