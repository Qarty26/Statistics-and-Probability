from scipy.stats import binom
from scipy.stats import geom
from scipy.stats import poisson
import matplotlib.pyplot as plt
import math
import numpy as np
import random


#la un centru de recoltare a sangelui vin zilnic 200 de pacienti. 30 dintre pacienti au rh-ul negativ
#care este probabilitatea ca intr-o zi sa vina cu minim 20% mai multi pacienti cu rh negativ?

def ex3():
    N = 1000000
    n = 200
    lam = 30

    pois = np.random.binomial(n,lam/n,N)
    prob = np.mean(pois <= lam + (20/100 * lam))

    print("Probabilitatea de a veni mai mult de",lam + (20/100 * lam) ," de pacienti cu rh negativ =",(1 - prob)*100,"%")

ex3()


#la un restaurant timpul mediu de asteptare este de 45 de minute
#care este probabilitatea ca masa sa fie servita cu minim 10% mai repede?

def ex6():
    
    N = 10000
    lam = 45

    exp = np.random.exponential(scale=lam,size=N)
    prob = np.mean(exp <= lam - (10/100 * lam))

    print("Probabilitatea comenzii de a veni in sub",lam - (10/100 * lam) ,"minute este de",(prob)*100,"%")

ex6()