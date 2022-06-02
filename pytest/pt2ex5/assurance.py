
def fidelite(couleur, ancient):
	if ancient > 5:
		if couleur =="vert":
			return "bleu"
		elif couleur == "orange":
			return "vert"
		elif couleur == "rouge":
			return "orange"
		else:
			return "mauvaise couleur"
	else:
		return couleur

def calculCouleur(age, permis, nbrAccident, ancien ):
	if (age < 25 and permis >= 2) or (age >= 25 and permis < 2 ):
		if nbrAccident == 0:
			return(fidelite("orange", ancien))
		elif nbrAccident == 1:
			return(fidelite("rouge", ancien))
		else:
			return("refusé")

	elif age >= 25 and permis >= 2:
		if nbrAccident == 0:
			return(fidelite("vert", ancien))
		elif nbrAccident == 1:
			return(fidelite("orange", ancien))
		elif nbrAccident == 2:
			return(fidelite("rouge", ancien))
		else:
			return("refusé")
	else: #age < 25 et permis < 2
		if nbrAccident == 0:
			return(fidelite("rouge", ancien))
		else:
			return("refusé")
"""
ageU = int(input("age : "))
nbrAccidentU = int(input("accident : "))
ancienU = int(input("ancienneté du contrat : "))
permisU = int(input("titulaire du permis depuis : "))

calculCouleur(ageU, permisU, nbrAccidentU, ancienU)

"""