import matplotlib.pyplot as plt


class ChartMaker:
    # Luna
    def create_bar_chart(self,all_num):
        name_list = ["Class", "Attribute", "Method"]
        numbers = all_num
        size = range(len(numbers))
        plt.bar(size, numbers, tick_label=name_list)
        plt.ylabel("Number")
        plt.xlabel("Elements of class diagram")
        plt.title("The Total Numbers of Three Elements in The Class Diagram")
        plt.show()

    # Rajan
    def create_pie_chart(self, all_num):
        plt.figure(figsize=(5, 5))
        labels = ["ClassNum", "AttributeNum", "MethodNum"]
        values = all_num
        explode = [0.05, 0, 0]
        plt.pie(values, labels=labels, autopct="%.1f%%", explode=explode)
        plt.show()