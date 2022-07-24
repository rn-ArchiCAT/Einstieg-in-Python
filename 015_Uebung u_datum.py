print("Tag des Datums eingeben:")
Tag=input()
Tag_int=int(Tag)
print(Tag)

print("Monat des Datums eingeben:")
Monat=input()
Monat_int=int(Monat)
print(Monat)

print("Jahr des Datums eingeben:")
Jahr=input()
Jahr_int=int(Jahr)
print(Jahr)

#Datenbank Anzahl Tage im Monat
if Monat_int == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    LetzterTag = 31

elif Monat_int == 4 or 6 or 9 or 11:
    LetzterTag = 30

elif Monat_int == 2:
    LetzterTag = 28

#Beziehung zum letzten Tag im Monat
if Tag_int < LetzterTag:
    BeziehungLetzterTag = "KLEINER"
else:
    BeziehungLetzterTag = "GRÖßER"

#Schaltjahr
if Jahr_int%4 == 0 and Jahr_int%100 != 0:
    Schaltjahr = "EIN"
elif Jahr_int%400 == 0:
    Schaltjahr = "EIN"
else:
    Schaltjahr = "KEIN"

#Bedingung Richtiges Datum
if Tag_int >= 1 and Tag_int < LetzterTag:
    Datum=("Richtiges Datum")
else:
    Datum=("Falsches Datum")

if Monat_int >= 1 and Monat_int <= 12:
    Datum=("Richtiges Datum")
else:
    Datum=("Falsches Datum")

#Ausgabe
print("Letzter Tag im Monat:",LetzterTag)
print("Tag des Datums ist:",BeziehungLetzterTag,"als der letzte Tag im Monat")
print("Jahr des Datums ist:",Schaltjahr,"Schaltjahr")
print(Datum)
