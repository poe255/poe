from index import bissextile
from index import jourValide
from index import lendemain
import pytest


"""
https://www.calendrier.best/annee-bissextile.html#:~:text=Pour%20v%C3%A9rifier%20si%20une%20ann%C3%A9e,100%3D20%2C4).
1900	Non
2000	Oui
2020	Oui
2022	Non
2024	Oui
2100	Non


def test_bisextille_0():
	assert bissextile() == 
"""


def test_bisextille_01():
	assert bissextile(1900) == False
def test_bisextille_02():
	assert bissextile(2000) == True
def test_bisextille_03():
	assert bissextile(2020) == True
def test_bisextille_04():
	assert bissextile(2022) == False
def test_bisextille_05():
	assert bissextile(2024) == True
def test_bisextille_06():
	assert bissextile(2100) == False

"""
def test_jourValide_0():
	assert jourValide() == 
"""

#valeur limite valide des années
def test_jourValide_01():
	assert jourValide(20,1,0) == True 

#valeur limite valide des jours	
def test_jourValide_02():
	assert jourValide(1,4,1993) == True
def test_jourValide_03():
	assert jourValide(30,4,1993) == True
def test_jourValide_04():
	assert jourValide(1,1,1993) == True
def test_jourValide_05():
	assert jourValide(31,1,1993) == True
def test_jourValide_06():
	assert jourValide(1,2,2024) == True
def test_jourValide_07():
	assert jourValide(29,2,2024) == True
def test_jourValide_08():
	assert jourValide(1,2,1900) == True
def test_jourValide_09():
	assert jourValide(28,2,1900) == True

#valeur limite valide des mois
def test_jourValide_10():
	assert jourValide(15,1,2000) == True
def test_jourValide_11():
	assert jourValide(15,12,2000) == True


#valeur limite non valide des années
def test_jourValide_01_false():
	assert jourValide(20,1,-1) == False 

#valeur limite non valide des jours	
def test_jourValide_02_false():
	assert jourValide(0,4,1993) == False
def test_jourValide_03_false():
	assert jourValide(31,4,1993) == False
def test_jourValide_04_false():
	assert jourValide(0,1,1993) == False
def test_jourValide_05_false():
	assert jourValide(32,1,1993) == False
def test_jourValide_06_false():
	assert jourValide(0,2,2024) == False
def test_jourValide_07_false():
	assert jourValide(30,2,2024) == False
def test_jourValide_08_false():
	assert jourValide(0,2,1900) == False
def test_jourValide_09_false():
	assert jourValide(29,2,1900) == False

#valeur limite non valide des mois
def test_jourValide_10_false():
	assert jourValide(15,0,2000) == False
def test_jourValide_11_false():
	assert jourValide(15,13,2000) == False

"""
def test_lendemain_():
	assert lendemain() ==
"""

def test_lendemain_01():
	assert lendemain(28,2,2024) == [29,2,2024]
def test_lendemain_02():
	assert lendemain(29,2,2024) == [1,3,2024]
def test_lendemain_03():
	assert lendemain(28,2,2023) == [1,3,2023]
def test_lendemain_():
	assert lendemain(30,4,2000) == [1,5,2000]
def test_lendemain_():
	assert lendemain(31,1,2000) == [1,2,2000]
def test_lendemain_():
	assert lendemain(31,12,2000) == [1,1,2001]
def test_lendemain_():
	assert lendemain(10,10,2010) == [11,10,2010]
def test_lendemain_():
	assert lendemain(35,35,35) == "jour non valide"