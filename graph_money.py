import matplotlib.pyplot as plt
from money2019 import total_money2019, total_money2018, total_money2017


def money():

    #name = "Clementine Sales Over 3 Years"
    print(total_money2017)
    print(total_money2018)
    print(total_money2019)
    labels = '2019', '2018', '2017'
    sizes = [total_money2019,total_money2018,
             total_money2017 ]
    tot = sum(sizes)/100.0
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct=lambda x: "%d" % round(x*tot), shadow=True,
            startangle=90)
    ax1.axis('equal')
    plt.title("Total Dollar Amount Sold Over 3 Years")


    plt.show()
