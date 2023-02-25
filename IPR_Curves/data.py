# Sort data here

PI = 11.5767 # stb/day-spi
Pavg = 3973.25 # psia
Pb = 1610.0 # psia
Qv = 10354.715 # stb/d
Qb = 27358.6363 # stb/d

margin = 7

# Bottomhole pressure
Pwf = [3973.25, 1610, 1600, 1550, 1500, 1450, 1400, 1350, 1300, 1250, 1200, 1150, 1100, 
       1050, 1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 
       250, 200, 150, 100, 50, 0]

# Flowrate
Qo = []

# Uploads data to data.txt file
with open("data.txt", "w") as fileobj:
    fileobj.write("Pressure Flowrate \n")
    for x in Pwf:
        # Calculates for Qo above and below the bubble point pressure (Pb)
        if x >= Pb: # Above
            y = PI * (Pavg - x)
        else: # Below
            y = Qb + Qv*(1 - 0.2*(x/Pb) - 0.8*(x/Pb)**2)
        Qo.append(y)
    
        fileobj.writelines(f"{x}") # Writes Qo

        # Calculates no of spaces to separate data and writes required spaces to data.txt
        n_space = (margin - len(str(x))) + 2
        for i in range(n_space):
            fileobj.write(" ")
        
        fileobj.write(f"{y} \n") # Writes Pwf