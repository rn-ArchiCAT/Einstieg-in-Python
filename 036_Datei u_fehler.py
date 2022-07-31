#Initialisierung
Schleife_x = 1

#while-Schleife
while Schleife_x != 0:

    #Eingabe
    print("Geben Sie einen inch-Wert ein:")
    Eingabe = input()

    try:
        #Eingabe
        Eingabe_int = float(Eingabe)
        print("Sie haben die Zahl", Eingabe_int,"richtig eingegeben")
        #Berechnung
        Ergebnis = Eingabe_int * 2.54
        #Ausgabe
        print("Der Wert:",Eingabe_int,"inch wurde in",Ergebnis,"cm umgerechnet.")
        #Initialisierung
        Schleife_x = 0

    except:
        #Ausgabe
        print("Sie haben die Zahl", Eingabe,"falsch eingegeben")
        #Initialisierung
        Schleife_x = 1

print("Ende des Programms")
