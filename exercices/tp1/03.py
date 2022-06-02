"""
02 p59 pdf30
Ecrire un algorithme permettant de donnée la valeur absolue d'un chiffre

03 p60 pdf30
Ecrire un script permettant de déterminer l'état d'un guichet
	Ouvert
	Fermé
En fonction du jour
	Semaine (ouvert)
	Weekend (fermé)
De l'heure
	8h-13h et 14h-17h ouvert
	Autre heures fermé

Puis faire la même chose mais ouvert le samedi matin 
"""
from lib import number

week = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

day = input("entrer un jour de la semaine : ")
dayL = day.lower()#converti la chaine de caractere en minuscule

heure = input("entrer l'heure : ")


lenght = len(heure)
h = ""
m = ""
switch = True
i=0
while i < lenght:
	if number.isNumber(heure[i:i+1]):
		if switch:
			h = h + heure[i:i+1]
		else:
			m = m  + heure[i:i+1]
	else:
		switch = False

	i += 1
else:
	h = int(h)
	m = int(m)


h = h *60
heure = h+m
"""
8h = 460
13h = 780
14h = 840
17h = 1020
"""
if dayL == week[5] or dayL == week[6] :
	print(" Fermé !")
elif dayL == week[0] or dayL == week[1] or dayL == week[2] or dayL == week[3] or dayL == week[4]:
	if (heure>460 and heure<780) or (heure>840 and heure<1020):
		print("ouvert !")
	else:
		print("fermé")
else:
	print(day + " n'est pas un jour de la semaine")
