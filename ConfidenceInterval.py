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
		tscore = round(score,2)
		zscore = "N/A"
	else:
		score = norm.ppf(p + (1 - p) / 2)
		tscore = "N/A"
		zscore = round(score,2)

	lower = (p2 - p1) - score * Sp
	upper = (p2 - p1) + score * Sp
	
	statement = ""

	if ( lower < 0 and upper < 0 ) or ( lower > 0 and upper > 0 ):
		statement = "It is highly likely that there is a true difference in the proportion of people who answered 'yes' between those who took the first aid course less than and more than 12 months previously."
		sigdiff = "ja"
	else:
		statement = "It is highly likely that there is no true difference in the proportion of people who answered 'yes' between those who took the first aid course less than and more than 12 months previously."
		sigdiff = "nein"

	meandiff = p1 - p2

	CI = [round(lower,2), round(upper,2)]

	return "The difference between the means is " + str(meandiff) + ". There is a " + str(int(p*100)) + "% chance that the confidence interval of " + str([lower, upper]) + " contains the true difference in the proportion of people who answered 'yes' between those who took the First Aid Course less than and more than 12 months previously. " + statement, tscore, zscore, round(meandiff,2), CI, sigdiff 
