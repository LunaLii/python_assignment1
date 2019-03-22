from fileHandler import PrintClass
from chart_maker import ChartMaker


class Controller:
    file = PrintClass()
    chart = ChartMaker()

    def load_file(self, infile):
        try:
            if ".txt" in infile[-4:] or ".docx" in infile[-5:]:
                content = self.file.class_handler(infile)
                return content

            else:
                message = "incorrect file format, please see help load"
                raise NameError(message)

        except NameError as e:
            print(e)
        except FileNotFoundError:
            print("File not found")
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



# x = Controller()
# # x.load_file("uml.txt")
# x.save_file("uml.txt")
# print(sum(x.file.num_all_attribute_list))
# print(len(x.file.class_name_list))
# print(sum(x.file.num_all_method_list))

