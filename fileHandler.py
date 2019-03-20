import docx


class PrintClass:               #class name changed
    relationship_list = []      #################

    def __init__(self,file):
        self.class_file = file

    #Luna   load data from .docx file
    def read_word_file(self):
        file = docx.Document(self.class_file)
        content = []
        for para in file.paragraphs:
            content.append(para.text + "\n")
        return content

    def read_txt_file(self): #################################
        file = open(self.class_file, 'r').readlines()
        return file

    def class_handler(self):    #I drectly use self.class_file in this function
        if ".txt" in self.class_file[-4:]:     #identify the file type
            file_content = self.read_txt_file()
        elif ".docx" in self.class_file[-5:]:
            file_content = self.read_word_file()
        classList = [[]]
        for i, m in enumerate(file_content[1:-1]):
            if m == "\n":
                if i != len(file_content[1:-1]) - 1:
                    classList.append([])
            else:
                classList[-1].append(m)
        self.relationship_list = classList[0]
        class_list = classList[1:]
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
                temp_relationship = "        # "+first_c_name.lower() + ' -> ' + second_c_name.lower() + "\n" \
                                    + "        self." + first_c_name.lower() + " = " + "None"
                all_relationship.append(temp_relationship)
        return all_relationship

    def output_class(self, class_item):
        class_name = self.get_class_name(class_item)

        result = "class " + class_name + ":\n    def __init__(self"

        for listItem in self.get_attributes(class_item):
            result += ', ' + listItem

        result += '):\n'
        for listItem in self.get_attributes(class_item):
            result += '        self.' + listItem + ' = ' + listItem + '\n'
        for list_item in self.get_relationship(class_name):
            result += list_item + '\n'

        result += '\n'
        for listItem in self.get_methods(class_item):
            result += '    def ' + listItem + '(self):\n        # Todo: incomplete\n        pass\n'
            result += '\n'
        return result

    def outputClasses(self):
        files = []
        for classItem in self.class_handler():
            files.append(self.get_class_name(classItem) + '.py')
        for classItem, file in zip(self.class_handler(), files):
            result = self.output_class(classItem)
            with open(file, "w") as output:
                output.write(result)

PrintClass('uml.docx').outputClasses()
# printClass('classDiagram.txt').class_handler()
# c = printClass('classDiagram.docx')
# c.read_word_file('classDiagram.docx')


