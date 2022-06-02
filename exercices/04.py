"""
04 p48 pdf24
-> boucle while
Recopier 50 fois
	"Le python c'est chouette"

Faire le décompte d'une bombe qui explose à la fin 

"""
import time

i = 0
while i<50:
	print("Le python c'est chouette")
	i += 1

i=10
while i>0:
	print("La bombe va explosé dans : " + str(i) + "s")
	i -= 1
	time.sleep(1)
else:
	print("BOOM !")