import matplotlib.pyplot as plt

# Flowrate
Qo = []

# Bottomhole pressure
Pwf = []

# Obtains data from data.txt and assings data to Qo and Pwf
with open("data.txt", "r") as fileobj:
    data = fileobj.readlines()

    RANGE = len(data)
    for i in range(1, RANGE):
        # Seperates txt line into Qo and Pwf data
        value = data[i].split()

        # Updates Qo and Pwf
        Qo.append(float(value[1]))
        Pwf.append(float(value[0]))


# Plots graph of Pwf against Qo
plt.grid()
plt.title("Inflow Perfomance Relationship Curve")
plt.plot(Qo, Pwf, label = "Productivity Index")
plt.margins(x=0, y=0)

# Sets range of x-axis
plt.xlim(0, 45000)

# Creates annotation for a particular point xy (AOF in this case)
plt.annotate(text=f"AOF = {round(Qo[-2], 4)} stb/day)", 
             xy=(Qo[-2], Pwf[-2]), xytext=(15000, 750),
             arrowprops=dict(facecolor="black", shrink=0.03))

plt.xlabel("Flowrate (qo)")
plt.ylabel("Bottom hole pressure (Pwf)")
plt.legend()
plt.show()
