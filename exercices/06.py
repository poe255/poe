"""
06 p70 pdf35
Traduire le code génétique suivant à l'aide d'un dictionnaire
Arnm = "UUUUUAUUGUUUUCUUUU"
Sachant que
	UUU = F
	UUC = F
	UUA = L
	UUG = L
	UCU = S
"""



arnm = "UUUUUAUUGUUUUCUUUU"
adn = ""
x = 0
y = 3
lenght = len(arnm)


def deCode(value):
	code = {
		"UUU": "F",
		"UUC": "F",
		"UUA": "L",
		"UUG": "L",
		"UCU": "S"
	}
	for n in code:
		if value == n:	
			return code[value] # quand le segment est trouvé renvoyé la valeur


while x<lenght:
	adn = adn + deCode(arnm[x:y]) #x et y définisse la partie de la chaine de caractère à utilisé 
	x +=3
	y +=3
else:
	print("Version codé : " + arnm + "\nVersion décodé : " + adn)