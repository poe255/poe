"""
02 p43 pdf22
Construire un script qui vérifie que :
	Le premier chiffre saisi est supérieur à 100
	Et le deuxième est inférieur à 37
"""
from lib import number


nbr = input("renseigner un nombre : ")


if number.isNumber(nbr):
	x = float(nbr)#converti la chaine de caractère en nombre décimal
	if x>100:
		print(str(nbr) + " est supérieur à 100 !")#utilise la valeur initial pour l'affichage pour éviter des affichages type  : "5.0"
	elif x == 100:
		print("100 est égale à 100")
	else:
		print(str(nbr) + " est inférieur à 100 !")
else:
	print("Ceci n\'est pas un nombre valide")#la valeur entrée n'est pas un nombre


nbr = input("renseigner un nombre : ")


if number.isNumber(nbr):
	x = float(nbr)#converti la chaine de caractère en nombre décimal
	if x<37:
		print(str(nbr) + " est inférieur à 37 !")#utilise la valeur initial pour l'affichage pour éviter des affichages type  : "5.0"
	elif x == 37:
		print("37 est égale à 37")
	else:
		print(str(nbr) + " est supérieur à 37 !")
else:
	print("Ceci n\'est pas un nombre valide")#la valeur entrée n'est pas un nombre
