import docx
from validator import Validator


class PrintClass:

    def __init__(self):
        self.relationship_list = []
        self.class_name_list = []
        self.num_all_attribute_list = []
        self.num_all_method_list = []
        self.compo_1_to_1 = []
        self.aggr_1_to_1 = []
        self.compo_1_to_many = []
        self.aggr_1_to_many = []
        self.association_list = []
        self.dependency_list = []
        # self.all_relationship_list = []


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
        if ".txt" in file_name[-4:]:
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
        class_list = class_list[1:]
        return class_list

    def get_class_name(self, class_array):
        for listItem in class_array:
            if "class" in listItem:
                temp_class = listItem[:listItem.index(" {")]
                class_name = temp_class.split(' ')[1]
                return class_name

    def get_attributes(self, class_array):
        attributes = []
        for listItem in class_array:
            if ":" in listItem and "(" not in listItem:
                result = listItem.split(' ')
                attributes.append(result[4])
        num_attribute = len(attributes)
        self.num_all_attribute_list.append(num_attribute)
        return attributes

    def get_methods(self, class_array):
        methods = []
        for listItem in class_array:
            if "(" in listItem:
                methods.append(listItem[:listItem.index("\n")-2].strip())
        num_method = len(methods)
        self.num_all_method_list.append(num_method)
        return methods

    #Luna
    def get_relationship(self, class_name):
        all_relationship = []
        temp_relationship = []
        for a_relationship in self.relationship_list:
            r_class_name = a_relationship.split(" ")
            first_c_name = r_class_name[0]
            second_c_name = r_class_name[-1].replace("\n", "")
            if class_name == first_c_name:

                temp_relationship += self.get_relationship_type(a_relationship,second_c_name)
                # if len(a_relationship.split(" ")) == 3:
                #     if "*--" in a_relationship:
                #         self.compo_1_to_1.append(second_c_name)
                #         temp_relationship += "        # self. my_" + second_c_name.lower() + " ->" + second_c_name \
                #                              + "\n" + "        self." + second_c_name.lower() + " = " + "None \n"
                #     elif "o--" in a_relationship:
                #         self.aggr_1_to_1.append(second_c_name)
                #     elif "<--" in a_relationship:
                #         self.association_list.append(second_c_name)
                #     elif "<.." in a_relationship:
                #         self.dependency_list.append(second_c_name)
                # else:
                #     if '"1" *-- "many"' in a_relationship:
                #         self.compo_1_to_many.append(second_c_name)
                #         temp_relationship += "        # self. my_" + second_c_name.lower() + ": list" + " ->" + second_c_name \
                #                              + "\n" + "        self." + second_c_name.lower() + " = " + "None\n"
                #     elif '"1" o-- "many"' in a_relationship:
                #         self.aggr_1_to_many.append(second_c_name)
                # self.get_relationship_type(a_relationship,second_c_name)
                #     for r in self.compo_1_to_many:
                #         temp_relationship += "        # self. my_" + r.lower() + ": list" + " ->" + r \
                #                             + "\n" + "        self." + r.lower() + " = " + "None\n"
                #     for r in self.compo_1_to_1:
                #         temp_relationship += "        # self. my_" + r.lower() + " ->" + r\
                #                             + "\n" + "        self." + r.lower() + " = " + "None \n"
        # all_relationship.append(temp_relationship)
        return temp_relationship
        # self.all_relationship_list = all_relationship

    def get_relationship_type(self,a_relationship,name):
        result = ''
        if len(a_relationship.split(" ")) == 3:
            if "*--" in a_relationship:
                self.compo_1_to_1.append(name)
                result += "        # self. my_" + name.lower() + " ->" + name \
                     + "\n" + "        self." + name.lower() + " = " + "None \n"
            elif "o--" in a_relationship:
                self.aggr_1_to_1.append(name)
            elif "<--" in a_relationship:
                self.association_list.append(name)
            elif "<.." in a_relationship:
                self.dependency_list.append(name)
        else:
            if '"1" *-- "many"' in a_relationship:
                self.compo_1_to_many.append(name)
                result = "        # self. my_" + name.lower() + ": list" + " ->" + name \
                          + "\n" + "        self." + name.lower() + " = " + "None\n"
            elif '"1" o-- "many"' in a_relationship:
                self.aggr_1_to_many.append(name)
        return result


    def output_class(self, class_item):
        class_name = self.get_class_name(class_item)
        self.class_name_list.append(class_name)
        attribute_list = self.get_attributes(class_item)
        method_list = self.get_methods(class_item)
        relationship_list = self.get_relationship(class_name)
        # print(relationship_list)
        result = "class " + class_name + ":\n    def __init__(self"

        for listItem in attribute_list:
            result += ', ' + listItem

        result += '):\n'

        if not Validator.validate_class_name(class_name):    #call the validate function
            result += "     # the class name is in wrong format \n"

        for listItem in attribute_list:
            result += '        self.' + listItem + ' = ' + listItem + '\n'

        for list_item in relationship_list:
            result += list_item


        result += '\n'
        for listItem in method_list:
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
        print("Files are saved")

    def get_all_num(self):
        class_num = len(self.class_name_list)
        attribute_num = sum(self.num_all_attribute_list)
        method_num = sum(self.num_all_method_list)
        all_num = [class_num, attribute_num, method_num]
        return all_num

    # def get_num_attribute(self):
    #     num_attribute = len(self.get_attributes())
    #     self.num_attribute_list.append(num_attribute)


# printClass('classDiagram.txt').class_handler()
# c = printClass('classDiagram.docx')
# c.read_word_file('classDiagram.docx')
#

#
# print(c.class_name_list)

# c.outputClasses()


