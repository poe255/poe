"""
jour = int(input("jour : "))
mois = int(input("mois : "))
annee = int(input("année : "))
"""
def bissextile(an):
	if ((an%4) == 0 and (an%100) != 0) or ((an%400) == 0):
		return True
	else:
		return False



def jourValide(jour, mois, annee):
	mois30 = [4,6,9,11]
	mois31 = [1,3,5,7,8,10,12]
	if annee >= 0:
		if mois > 0 and mois < 13:
			if mois == 2 and bissextile(annee) == True and jour > 0 and jour < 30:
				return True
			elif mois == 2 and bissextile(annee) == False and jour > 0 and jour < 29:
				return True
			elif mois in mois30 and jour > 0 and jour < 31:
				return True
			elif mois in mois31 and jour > 0 and jour <= 31:
				return True
			else:
				return False
		else:
			return False
	else:
		return False


def lendemain(jour, mois, annee):
	mois30 = [4,6,9,11]
	mois31 = [1,3,5,7,8,10,12]

	if jourValide(jour, mois, annee):
		if mois == 2 and jour == 28 and bissextile(annee) == True:
			jour +=1
		elif (mois == 2 and jour == 29) or (mois == 2 and jour == 28):
			jour = 1
			mois += 1
		elif mois in mois30 and jour == 30:
			jour = 1
			mois += 1
		elif mois in mois31 and jour == 31:
			jour = 1
			mois += 1
		elif mois == 12 and jour == 31:
			jour = 1
			mois =1
			annee += 1
		else:
			jour +=1

		return [jour, mois, annee]
	else:
		return "jour non valide"
"""
print(lendemain(jour,mois,annee))
"""