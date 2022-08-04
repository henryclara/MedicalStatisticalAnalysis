#!/usr/bin/python

# This code calculates the confidence interval for two sets of binary data

from scipy.stats import t
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# As input, the function uses the sample sizes n1 and n2, and the number of positive outcomes (np1 and np2) 
# within each sample population. p is the desired confidence interval.

def ConfInt(np1, np2, n1, n2, p):

	p1 = np1 / n1
	p2 = np2 / n2	

	Sp = np.sqrt( ( p1 * ( 1 - p1 )) / n1 + ( p2 * ( 1 - p2 )) / n2 )

	if ( n1 < 30 ) or ( n2 < 30 ):
		score = t.ppf( p + (1 - p) / 2 , n1 + n2 - 2 )
	else:
		score = norm.ppf(p + (1 - p) / 2)

	lower = (p2 - p1) - score * Sp
	upper = (p2 - p1) + score * Sp
	
	meandiff = p1 - p2

	return meandiff, [ lower, upper ]
