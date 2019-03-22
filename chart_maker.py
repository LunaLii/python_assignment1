import matplotlib.pyplot as plt


class ChartMaker:
    #Luna
    def create_total_bar(self,all_num):
        name_list = ["ClassNum", "AttributeNum", "MethodNum"]
        sizes = all_num
        plt.bar(range(len(sizes)), sizes, tick_label=name_list)
        plt.title("The numbers of class, attributes and methods")
        plt.show()
