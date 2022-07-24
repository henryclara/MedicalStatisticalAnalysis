#!/usr/bin/python

# ConfInt( np1, np2, n1, n2, p )
# Here, np1 and np2 are the proportion of "True"s in the question, n1 and n2 are the sample sizes and p is for the calculation of the confidence interval (e.g. 90%).

from ConfidenceInterval import ConfInt

print(ConfInt(16.0 / 79.0, 9.0 / 10.0, 79, 10, 0.95))

