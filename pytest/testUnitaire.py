from monCode import factorielle
import pytest

def test_Facto120():
	assert factorielle(5)==120
def test_Facto0():
	assert factorielle(0)==1