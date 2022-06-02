"""
07 p96 pdf48
Ecrire un programme qui récupère dans un fichier 
	La longueur d'un rectangle
	La largeur d'un rectangle
Qui renvoi l'aire
Et écrit dans un autre fichier l'aire
"""
from lib import number


def readLineValue(line):
	error = False
	newLine = ""
	lenght = len(line)
	i=0
	write = False
	while i < lenght:
		if write:
			if line[i:i+1] == " " or line[i:i+1] == "\n": #vérifie  les espaces et retour a ligne 
				pass
			elif line[i:i+1] == "," or line[i:i+1] == ".": #converti les , en .
				newLine = newLine + "."
			elif number.isNumber(line[i:i+1]): #vérifie si c'est un chifre 
				newLine = newLine + line[i:i+1]
			else:
				error = True
				newLine = line[i:i+1]
				break
		else:
			if line[i:i+1] == "=":
				write = True
		i+=1
	
	if error:
		return [True, newLine]
	else:
		try:
			int(newLine) 
		except ValueError:
			return [False, float(newLine)] 
		else:
			return [False, int(newLine)]


f = open("ressource/dim.txt")
L = 0
l = 0
error = False
#lire les lignes et récupérer la Longueur et la largeur
for i in range(2):
	line = f.readline()
	lineNbr = readLineValue(line)

	if lineNbr[0]:
		print("Le caractère \"" + str(lineNbr[1]) + "\" n'est pas accepté ligne : " + str(i+1))
		error = True
	else:
		if i == 0:
			L = lineNbr[1]
		else: 
			l = lineNbr[1]


if error:
	f.close()
else:
	aire = L * l
	print("Aire du rectangle = " + str(aire))
	f.close()

	f = open("ressource/aire.txt", "w")
	f.write("Aire du rectangle = " + str(aire))
	f.close()