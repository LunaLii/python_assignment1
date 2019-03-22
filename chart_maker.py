import matplotlib.pyplot as plt


class ChartMaker:
    #Luna
    def create_bar_chart(self,all_num):
        name_list = ["ClassNum", "AttributeNum", "MethodNum"]
        sizes = all_num
        plt.bar(range(len(sizes)), sizes, tick_label=name_list)
        plt.title("The numbers of class, attributes and methods")
        plt.show()

    def create_pie_chart(self, all_num):
        plt.figure(figsize=(5, 5))  # blank pie chart will 5 inch by 5inch
        labels = ["ClassNum", "AttributeNum", "MethodNum"]  # creating a labels for class
        values = all_num  # adding values to the labels
        explode = [0.05, 0, 0]  # this is used to highlight the biggest percent
        # creating a function to create a pie chart
        plt.pie(values, labels=labels, autopct="%.1f%%", explode=explode)  # autopct is a 'paramater'
        plt.show()  # to show the blank diag
