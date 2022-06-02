"""
02 p86 pdf43
Ecrire un algorithme permettant de saisir les notes d'une classe
La saisie s'arrête lorsque l'utilisateur tape "-1"
Le programme renvoie
	La moyenne
	La médiane
	Le nombre de note au dessus de la moyenne
"""

notes = []

i = 0

while i >= 0:
	i = int(input("nouvelle note : "))
	if i>-1:
		notes.append(i)
	

print(notes)