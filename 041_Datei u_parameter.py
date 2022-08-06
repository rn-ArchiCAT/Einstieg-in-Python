#Definition der Funktion
def steuer(z):
    if z > 2500:
        Abschlag=z*22/100
    else:
        Abschlag=z*18/100

    print(z)
    print("Es ergibt sich eine Steuer von",Abschlag,"Euro")

    
# Hauptprogramm
steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)
