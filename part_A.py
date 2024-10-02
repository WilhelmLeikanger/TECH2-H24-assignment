# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:19:20 2024

@author: wilhe
"""

"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
import numpy as np
def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    xsum=0
    xsquares=0
    a=0
    for i in x:
        xsum+=i
        xsquares+=i**2
        a+=1
    xmean=xsum/a
    xmeansquares=xsquares/a
    variance=xmeansquares-(xmean**2)
    deviation=variance**0.5
    return deviation
def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.   
    """
    xsum=sum(x)
    xsquares=sum(i**2 for i in x)
    xmean=xsum/len(x)
    xmeansquares=xsquares/len(x)
    variance=xmeansquares-xmean**2
    deviation=variance**0.5
    return deviation
def main():
    values=[1,2,3,4,5]
    print(np.std(values))
    print(std_loops(values))
    print(std_builtin(values))
main()