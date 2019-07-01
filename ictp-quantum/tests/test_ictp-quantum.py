import numpy as np
import scipy as sc
import qutip as qt
from numpy.testing import assert_, assert_equal, assert_almost_equal
from ictp-quantum import purity

def test_purity():
"""
Thest the `purity` function for a normalized quantum state. 
"""
	psi = qt.basis(3,1)
	rho = qt.ket2dm(psi)
	assert_equal(purity(rho),1.)