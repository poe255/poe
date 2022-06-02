from assurance import calculCouleur
import pytest

# calculCouleur(age, permis, nbrAccident, ancien)
ageSup = 50
ageInf = 20
permisSup = 4
permisInf = 1
nbrA0 = 0
nbrA1 = 1
nbrA2 = 2
nbrSup2 = 20
ancienSup = 6
ancienInf = 2

"""
def test_():
	assert calculCouleur() == ""
"""
def test_01():
	assert calculCouleur(ageSup, permisSup, nbrA0, ancienSup) == "bleu"
def test_02():
	assert calculCouleur(ageSup, permisInf, nbrA0, ancienSup) == "vert"
def test_03():
	assert calculCouleur(ageInf, permisSup, nbrA0, ancienSup) == "vert"
def test_04():
	assert calculCouleur(ageInf, permisInf, nbrA0, ancienSup) == "orange"
def test_05():
	assert calculCouleur(ageSup, permisSup, nbrA0, ancienInf) == "vert"
def test_06():
	assert calculCouleur(ageSup, permisInf, nbrA0, ancienInf) == "orange"
def test_07():
	assert calculCouleur(ageInf, permisSup, nbrA0, ancienInf) == "orange"
def test_08():
	assert calculCouleur(ageInf, permisInf, nbrA0, ancienInf) == "rouge"

def test_09():
	assert calculCouleur(ageSup, permisSup, nbrA1, ancienSup) == "vert"
def test_10():
	assert calculCouleur(ageSup, permisInf, nbrA1, ancienSup) == "orange"
def test_11():
	assert calculCouleur(ageInf, permisSup, nbrA1, ancienSup) == "orange"
def test_12():
	assert calculCouleur(ageInf, permisInf, nbrA1, ancienSup) == "refusé"
def test_13():
	assert calculCouleur(ageSup, permisSup, nbrA1, ancienInf) == "orange"
def test_14():
	assert calculCouleur(ageSup, permisInf, nbrA1, ancienInf) == "rouge"
def test_15():
	assert calculCouleur(ageInf, permisSup, nbrA1, ancienInf) == "rouge"
def test_16():
	assert calculCouleur(ageInf, permisInf, nbrA1, ancienInf) == "refusé"

def test_17():
	assert calculCouleur(ageSup, permisSup, nbrA2, ancienSup) == "orange"
def test_18():
	assert calculCouleur(ageSup, permisInf, nbrA2, ancienSup) == "refusé"
def test_19():
	assert calculCouleur(ageInf, permisSup, nbrA2, ancienSup) == "refusé"
def test_20():
	assert calculCouleur(ageInf, permisInf, nbrA2, ancienSup) == "refusé"
def test_21():
	assert calculCouleur(ageSup, permisSup, nbrA2, ancienInf) == "rouge"
def test_22():
	assert calculCouleur(ageSup, permisInf, nbrA2, ancienInf) == "refusé"
def test_23():
	assert calculCouleur(ageInf, permisSup, nbrA2, ancienInf) == "refusé"
def test_24():
	assert calculCouleur(ageInf, permisInf, nbrA2, ancienInf) == "refusé"

def test_25():
	assert calculCouleur(ageSup, permisSup, nbrSup2, ancienSup) == "refusé"
def test_26():
	assert calculCouleur(ageSup, permisInf, nbrSup2, ancienSup) == "refusé"
def test_27():
	assert calculCouleur(ageInf, permisSup, nbrSup2, ancienSup) == "refusé"
def test_28():
	assert calculCouleur(ageInf, permisInf, nbrSup2, ancienSup) == "refusé"
def test_29():
	assert calculCouleur(ageSup, permisSup, nbrSup2, ancienInf) == "refusé"
def test_30():
	assert calculCouleur(ageSup, permisInf, nbrSup2, ancienInf) == "refusé"
def test_31():
	assert calculCouleur(ageInf, permisSup, nbrSup2, ancienInf) == "refusé"
def test_32():
	assert calculCouleur(ageInf, permisInf, nbrSup2, ancienInf) == "refusé"

