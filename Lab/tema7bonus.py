from scipy.stats import binom
from scipy.stats import geom
from scipy.stats import poisson
import matplotlib.pyplot as plt
import math
import numpy as np
import random

def ex7():
    #a
    N=100000
    lam1 = np.random.randint(0,100000)
    lam2 = np.random.randint(0,100000)
    x = np.random.exponential(scale=lam1, size=N)
    y = np.random.exponential(scale=lam2, size=N)
    plt.hist(x)
    plt.hist(y)
    plt.show()
    
    #c
 
    x_values = np.linspace(0, 5, 100)
    y_values = (lam1 + lam2) * np.exp(-(lam1 + lam2) * x_values)
    plt.plot(x_values, y_values)
    plt.show()

ex7()

def ex8():
    N = 100000
    durataTram = 4
    durataBus = 8

    tram = np.random.exponential(scale=durataTram, size=N)
    bus = np.random.exponential(scale=durataBus, size=N)

    probA = np.mean(tram >= 5)
    print("Probabilitatea ca un calator sa astepte tramvaiul mai mult de 5 min: ", probA)

    probB = np.mean((tram >= 5) | (bus >= 5))
    print("Probabilitatea ca un calator sa astepte tramvaiul sau autobuzul mai mult de 5 min:", probB)


ex8()