#Eingabe
print("Geben Sie Ihr Gehalt in Euro ein:")
print("Sind Sie ledig oder verheiratet?:")


#Variablen Eingabe
Gehalt=input()
Gehalt_int=int(Gehalt)
Familienstand=input()

#Bedingung
if Gehalt_int > 4000 and Familienstand=="ledig":
    Steuersatz=26

if Gehalt_int > 4000 and Familienstand=="verheiratet":
    Steuersatz=22

if Gehalt_int <= 4000 and Familienstand=="ledig":
    Steuersatz=22

if Gehalt_int <= 4000 and Familienstand=="verheiratet":
    Steuersatz=18


#Berechnung
Abschlag=Gehalt_int*Steuersatz/100

#Ausgabe
print(Gehalt)
print(Familienstand)
print("Steuersatz:",Steuersatz)
print("Es ergibt sich eine Steuer von",Abschlag,"Euro")
