#Definition der Funktion
def steuer(z):
    print("Gehalt:", z)
    if z > 2500:
        Abschlag=z*22/100
    else:
        Abschlag=z*18/100
    return Abschlag


# Hauptprogramm
a = steuer(1800)
print("Es ergibt sich eine Steuerbetrag von",a,"Euro")

b = steuer(2200)
print("Es ergibt sich eine Steuerbetrag von",b,"Euro")

c = steuer(2500)
print("Es ergibt sich eine Steuerbetrag von",c,"Euro")

d = steuer(2900)
print("Es ergibt sich eine Steuerbetrag von",d,"Euro")

# Hauptprogramm LÖSUNG
print("Gehalt: 1800, Steuer:", steuer(1800))
print("Gehalt: 2200, Steuer:", steuer(2200))
print("Gehalt: 1800, Steuer:", steuer(2500))
print("Gehalt: 2200, Steuer:", steuer(2900))
