#Initialisierung
Eingabe_int = 1

#while-Schleife
while Eingabe_int != 0:

    #Eingabe
    print("Geben Sie einen inch-Wert ein:")
    Eingabe = input()
    Eingabe_int = int(Eingabe)

    #Berechnung
    Ergebnis = Eingabe_int * 2.54

    if Eingabe_int != 0:
        #Ausgabe
        print("Der Wert:",Eingabe_int,"inch wurde in",Ergebnis,"cm umgerechnet.")
