#Eingabe
print("Geben Sie Ihr Gehalt in Euro ein:")

#Variablen
a=input()
a_float=float(a)

#Verzweigung
if a_float>2500:
    b=22
else:
    b=18

#Berechnung
c=a_float*b/100

#Ausgabe
print(a)
print("Steuersatz:",b)
print("Es ergibt sich eine Steuer von",c,"Euro")
