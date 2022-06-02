"""
04(05) p61 pdf31
Ecrire un code qui permet de créer une pyramide à "n" ligne tel que :
	*
	**
	***
	****
	*****
	******
	*******
Puis tel sue :
	*
	**
	*0*
	*00*
	*000*
	*0000*
	*00000*
	********
"""

n = 1
L = 8

L = L +1 #ajuster la taille de la pyramide

while n < L:
	print("*" *n)
	n +=1

n = 1
while n < L:
	
	if n > 2 and n < (L-1):
		print("*" + ("o" *(n-2)) + "*")
	else:
		print("*" *n)

	n +=1

