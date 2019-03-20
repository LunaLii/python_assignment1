import docx


class printClass:
    relationship_list = []
    all_relationship_list = []

    def __init__(self, classFile):
        self.classFile = classFile

    def read_word_file(self, file_name):
        file = docx.Document(file_name)
        content = []
        for para in file.paragraphs:
            content.append(para.text + "\n")
        # print(content[0:])


    def class_handler(self, classDiagramFile):
        file = open(classDiagramFile, 'r').readlines()
        classList = [[]]
        for i, m in enumerate(file[1:-1]):  # remove 1st and last character
            if m == "\n":
                if i != len(file[1:-1]) - 1:
                    classList.append([])
            else:
                classList[-1].append(m)
        self.relationship_list = classList[0]
        class_list = classList[1:]
        return class_list

    def get_class_name(self, classArray):
        for listItem in classArray:
            if "class" in listItem:
                temp_class =  listItem[:listItem.index(" {")]
                class_name = temp_class.split(' ')[1]
                return class_name

    def get_attributes(self, classArray):
        attributes = []
        for listItem in classArray:
            if ":" in listItem and "(" not in listItem:
                result = listItem.split(' ')
                attributes.append(result[4])
        return attributes

    def get_methods(self, classArray):
        methods = []
        for listItem in classArray:
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

    def output_class(self, classItem):
        class_name = self.get_class_name(classItem)
        # self.get_relationship(class_name)

        result = "class " + class_name + ":\n    def __init__(self"

        for listItem in self.get_attributes(classItem):
            result += ', ' + listItem

        result += '):\n'
        for listItem in self.get_attributes(classItem):
            result += '        self.' + listItem + ' = ' + listItem + '\n'
        for list_item in self.get_relationship(class_name):
            result += list_item + '\n'

        result += '\n'
        for listItem in self.get_methods(classItem):
            result += '    def ' + listItem + '(self):\n        # Todo: incomplete\n        pass\n'
            result += '\n'
        return result

    def outputClasses(self):
        files = []
        for classItem in self.class_handler(self.classFile):
            files.append(self.get_class_name(classItem) + '.py')
        for classItem, file in zip(self.class_handler(self.classFile), files):
            result = self.output_class(classItem)
            with open(file, "w") as output:
                output.write(result)

printClass('uml.txt').outputClasses()
printClass('classDiagram.txt').class_handler('uml.txt')
# c = printClass('classDiagram.docx')
# c.read_word_file('classDiagram.docx')


