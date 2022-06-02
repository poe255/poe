"""
03 p44 pdf22
Construire un script qui vérifie que le jour saisi est dans le weekend
	Bonus : utiliser un/des tableau(x)
"""

week = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

day = input("entrer un jour de la semaine : ")
dayL = day.lower()#converti la chaine de caractere en minuscule


if dayL == week[5] or dayL == week[6] :
	print(day + " est un jour du weekend !")
elif dayL == week[0] or dayL == week[1] or dayL == week[2] or dayL == week[3] or dayL == week[4]:
	print(day + " n'est pas un jour du weekend !")
else:
	print(day + " n'est pas un jour de la semaine")
