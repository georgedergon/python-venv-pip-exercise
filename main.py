import matplotlib.pyplot as plt
import pandas as pd
# Beispiel-Daten: Zahlen von 0 bis 9 und ihre Quadrate
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [i**2 for i in x]  # Quadratzahlen
z = [i**3 for i in x]  # Kubikzahlen
# Liniendiagramm erstellen
plt.plot(x, y, label='Quadratzahlen')
plt.plot(x, z, label='Kobikzahlen')

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Quadratzahlen & von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('Quadrat')

# Legende anzeigen
plt.legend()

# Diagramm anzeigen
# plt.show()
plt.savefig("diagramm.png")

df = pd.DataFrame({"Zahl":x,"Quadrat":y,"Kubik":z})
df.to_csv("Diagramm.csv",index=False)