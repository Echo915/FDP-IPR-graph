# Run tests here
import matplotlib.pyplot as plt

def test_split_data(x):
    with open("data.txt", "r") as fileobj:
        lst = fileobj.readlines()
        choice = lst[x].split()
        return choice

def test_plot_graph():
    y = [3973.25, 1610.0, 1600.0, 1500.0, 1000.0, 500.0, 0.0]
    x = [0.0, 27358.636, 27474.083, 28593.404, 33231.274, 36271.257, 37713.351]

    plt.plot(x, y)
    plt.show()

def test_maximum_of_Pwf():
     Pwf = [3973.25, 1610, 1600, 1550, 1500, 1450, 1400, 1350, 1300, 1250, 1200, 1150, 1100, 
       1050, 1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 
       250, 200, 150, 100, 50, 0]

     print(max(Pwf))

x = [1] + [a for a in range(0, 10, 2)]
#x = [1, 2] + [3, 4]
print(x)