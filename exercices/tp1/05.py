"""
05 p62 pdf31
Programer les opérations de calcul élémentaire
	+
	-
	*
Ces opérations sont bien sûr interdites dans le script (incrémentation autorisé)
"""

def addition(val1, val2):
	for	i in range(val2):
		val1 += 1
	return val1

def soustraction(val1, val2):
	for	i in range(val2):
		val1 -= 1
	return val1
def multiplication(val1, val2):
	x=0
	for	i in range(val2):
		x = addition(x,val1)
	return x

print(addition(2,2))
print(soustraction(2,2))
print(multiplication(2,5))
