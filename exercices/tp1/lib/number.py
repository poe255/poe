def isNumber(nbr):
	try:
	    float(nbr) #essaie de convertir la chaine de caractère en nombre décimal
	except ValueError:
	    return False #return false en cas d'erreur sinon true
	else:
		return True