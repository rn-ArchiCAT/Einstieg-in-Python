#Modul random importieren
import random

#Zufallsgenerator initialisieren
random.seed()

#Zufallswerte und Berechnung
a=random.randint(1,10)
b=random.randint(1,10)
c=a+b
print("Die Aufgabe",a,"+",b)

#Eingabe
print("Bitte eine Zahl eingeben:")
z=input()
zahl=int(z)

#Mehrfache Verzweigung, logische Operatoren
if zahl == c:
    print(zahl,"ist richtig")
elif zahl < 0 or zahl > 100:
    print(zahl,"ist ganz falsch")
elif c-1 <= zahl <= c+1:
    print(zahl,"ist ganz nahe dran")
else:
    print(zahl,"ist falsch")

#Ende
print("Das Ergebnis:",c)
