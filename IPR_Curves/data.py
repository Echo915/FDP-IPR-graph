# Sort data here

PI = 11.5767 # stb/day-spi
Pavg = 4473 # psia
Pb = 1610.0 # psia
Qv = (PI * Pb) / 1.8 # stb/d
Qb = PI * (Pavg - Pb) # stb/d

margin = 7

# Bottomhole pressure
Pwf = [4473, 1610] + [a for a in range(1600, -1, -50)]

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