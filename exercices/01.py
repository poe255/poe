"""
01 p39 pdf20
Ecrire un script qui :
	Demande de renseigner un chiffre
	Renvoie si le chiffre est supérieur à 50 ou non
"""
#demande un nombre et le récupère comme une chaine de caractère
from lib import number

nbr = input("renseigner un chiffre : ")


if number.isNumber(nbr):
	x = float(nbr)#converti la chaine de caractère en nombre décimal
	if x>50:
		print(str(nbr) + " est supérieur à 50 !")#utilise la valeur initial pour l'affichage pour éviter des affichages type  : "5.0"
	elif x == 50:
		print("50 est égale à 50")
	else:
		print(str(nbr) + " est inférieur à 50 !")
else:
	print("Ceci n'est pas un nombre valide")#la valeur entrée n'est pas un nombre
