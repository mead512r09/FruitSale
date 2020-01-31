import matplotlib.pyplot as plt
from clementines2019 import total_clementines2019, total_clementines2018, total_clementines2017



def clementines():
        #name = "Clementine Sales Over 3 Years"
        print(total_clementines2017)
        print(total_clementines2018)
        print(total_clementines2019)

        labels = '2019', '2018', '2017'
        sizes = [total_clementines2019,total_clementines2018, total_clementines2017 ]
        tot = sum(sizes)/100.0
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct=lambda x: "%d" % round(x*tot), shadow=True,
                startangle=90)
        ax1.axis('equal')
        plt.title("Total Clementines Sold Over 3 Years")


        plt.show()

