from scipy.stats import binom
from scipy.stats import geom
import matplotlib.pyplot as plt



#probabilitatea ca un startup sa esueze in primul an este de 90%. In Romania se infiinteaza anual 150000 de startup-uri. 
#Care este probabilitatea ca minim 15000 de startup-uri sa treaca de primul an?
def prob_succes(n, p, k):

    distributie_binomiala = binom(n, p)
    prob = distributie_binomiala.pmf(k)
    
    return prob

def ex3():
    n = 1500
    p = 0.1
    k = 150
    suma=0
    L=[]
    for i in range(k,n+1):
        probabilitate = prob_succes(n, p, i)
        suma+=probabilitate
        L.append(probabilitate)
        
    print(suma)
    plt.hist(L)
    plt.show()
    
#ex3()

#https://www.goodcarbadcar.net/bmw-europe-sales-figures/
#https://www.fox4news.com/news/carmakers-most-recalls-2022-how-to-check-for-recalls

#numar total de masini vandute de bmw intre 2006 si 2013 : 5.2mil
#numar total de rechemari 917,000
#probabilitate de rechemare = 17%


#ex6
L=[] 
def prob(n,p):
    distributie_geometrica = geom(p)
    for x in range(1, n + 1):
        L.append(distributie_geometrica.pmf(x))

def ex6():
    
    n=52
    p=0.17
    prob(n,p)
    plt.bar(range(1, n + 1), L)
    plt.xlabel('Numărul de Mașini Până la Primul Defect')
    plt.ylabel('Probabilitate')
    plt.show()

#ex6()
