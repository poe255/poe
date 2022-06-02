"""
05 p56 pdf25
-> boucle for
Recopier 50 fois
	"Le python c'est chouette"

Faire le décompte d'une bombe qui explose à la fin 
"""

import time


for i in range(50):
	print("Le python c'est chouette")


for i in range(10, 0, -1):
	print("La bombe va explosé dans : " + str(i) + "s")
	
	time.sleep(1)
else:
	print("BOOM !")