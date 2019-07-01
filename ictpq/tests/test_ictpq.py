import numpy as np
import scipy as sc
import qutip as qt
from numpy.testing import assert_, assert_equal, assert_almost_equal
from ictpq.ictpq import *

def test_purity():
	"""
	Test the `purity` function for a normalized quantum state. 
	"""
	psi = qt.basis(3,1)
	rho = qt.ket2dm(psi)
	assert_equal(purity(rho),1.)
