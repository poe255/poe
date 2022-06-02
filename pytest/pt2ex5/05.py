import random

nbrRand = random.randint(1,100)


for i in range(3):
	print("il reste " + str(3-i) + " tentative")
	nbrUser = int(input("entre un nombre : "))
	if nbrUser == nbrRand:
		print("la valeur est bonne")
		break
	elif nbrUser > nbrRand:
		print("la valeur entrée est plus grande que le nombre a trouvé")
	else:
		print("la valeur entrée est plus basse que le nombre a trouvé")
else:
	print("la valeur était : ", nbrRand)