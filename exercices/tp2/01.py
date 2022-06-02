"""
01 p85 pdf43
Coder une foction "purge" qui, avec entrée
	Une chaine de caractère
	Un caractère
Purge la chaine du caractère précisé
Exemple :
	Purge("bonjour", "o") => "Bnjur"
	Purge("j'ai horreur des espaces", " ") => "j'aihorreurdesespaces"
Dans un second temps même question mais avec le nombre de caractère à supprimer en paramètre
"""

def purge(strInput, toDel):
	strOutput = strInput.replace(toDel, "")
	return strOutput

def purge2(strInput, nbr):
	strOutput = strInput[nbr:len(strInput)]
	return strOutput

print(purge("bonjour", "o"))
print(purge2("bonjour", 3))