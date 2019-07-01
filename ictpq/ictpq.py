import numpy as np
import scipy as sc
import qutip as qt
import matplotlib.pyplot as plt

def purity(rho):
	"""
	Calculate the purity of a quantum state (normalized in the process). 

	Parameters
	----------
	rho : :class:`qutip.Qobj`
		Density matrix of a quantum system.

	Returns
	----------
	purity_rho : float
		Purity of the quantum system, p (p=1 if pure, 1/N<=p<1 if mixed).
	"""
	purity_rho = ((rho*rho).unit()).tr()
	return purity_rho