#!/usr/bin/python

# This code calculates the confidence interval for two sets of binary data

from scipy.stats import t
from scipy.stats import zscore
import matplotlib.pyplot as plt
import numpy as np

# As input, the function uses the sample sizes n1 and n2, and the number of positive outcomes (np1 and np2) within each sample population.

def ConfInt(np1, np2, n1, n2, p):

	s12 = np.sqrt((np1 * (1 - np1))/n1)
	s22 = np.sqrt((np2 * (1 - np2))/n2)
	
	Sp = np.sqrt(( s12 * (n1 - 1.0)**2 + s22 * (n2 - 1.0)**2 ) / (n1 + n2 - 2))

	if ( n1 < 30 ) or ( n2 < 30 ):
		score = t.ppf(p, n1 + n2 -2)
	else:
		print("Calculation of zscore needed")

	lower = np1 / n1 - np2 / n2 - score * Sp * np.sqrt( 1.0 / n1 + 1.0 / n2)
	upper = np1 / n1 - np2 / n2 + score * Sp * np.sqrt( 1.0 / n1 + 1.0 / n2)
	
	meandiff = np1 - np2

	return "( " + str(lower) + ", " + str(upper) + ")."
