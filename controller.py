from fileHandler import PrintClass
from chart_maker import ChartMaker


class Controller:
    file = PrintClass()
    chart = ChartMaker()

    @staticmethod
    def load_file(infile):
        r"""
        >>> Controller.load_file("test_read_file.csv")
        Incorrect file type, please see help load
        >>> Controller.load_file("test2.docx")
        [['class ToyBox {\n', '    name : String\n', '}\n'], ['class Toy {\n', '}\n']]
        >>> Controller.load_file("C:\\Users\Luna\ICT\\test2.docx")
        File is not found
        """
        try:
            if ".txt" in infile[-4:] or ".docx" in infile[-5:]:
                content = Controller.file.class_handler(infile)
                return content

            else:
                message = "Incorrect file type, please see help load"
                raise NameError(message)

        except NameError as e:
            print(e)
        except FileNotFoundError:
            print("File is not found")
        except Exception as e:
            print(e)

    def save_file(self, file_name):
        class_list = self.load_file(file_name)
        self.file.outputClasses(class_list)

    def create_bar_chart(self):
        all_num = self.file.get_all_num()
        self.chart.create_bar_chart(all_num)

    def create_pie_chart(self):
        all_num = self.file.get_all_num()
        self.chart.create_pie_chart(all_num)

    def create_line_chart(self):
        all_num = self.file.get_all_num()
        self.chart.create_line_graph(all_num)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


# x = Controller()
# x.load_file("uml.txt")
# x.save_file("uml.txt")
# print(sum(x.file.num_all_attribute_list))
# print(len(x.file.class_name_list))
# print(sum(x.file.num_all_method_list))
# print(x.file.compo_1_to_many)
# print(x.file.compo_1_to_1)
# print(Controller.file.read_word_file("test.docx"))


