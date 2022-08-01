#Schleife
for i in range (1,7):
    print("Zahl:",i)
    if 3 <= i <= 5:
        """
        ...bei Erfüllung der Bedingung wird print Ausgabe übersprungen
        und ein erneuter Schleifendurchlauf beginnt...
        """
        continue
    print("Quadrat:",i*i)
