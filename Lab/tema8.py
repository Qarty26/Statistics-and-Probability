import numpy as np
import matplotlib.pyplot as plt

def ex4():
    n = 10000
    N = 100
    p = np.random.rand()
    #p = 0.5
    
    pasi = np.random.rand(n)
    values = np.where(pasi <= p, 1, -1)
    cumulativeSum = np.cumsum(values)
    
    nPoz = np.random.rand(n)
    valueNPoz = np.where(pasi <= p, 1, -1)
    
    #a
    plt.plot(cumulativeSum)
    plt.xlabel('Contor')
    plt.ylabel('Suma cumulativa')
    plt.show()
    
    #b
    plt.hist(valueNPoz, bins=100, density=True, color='blue' )
    plt.show()
    
    #c
    E = np.mean(values)
    patrat = np.square(values)
    niu = E
    sigma = np.sqrt(np.mean(patrat) - E**2)
    f = lambda x: 1/(np.sqrt(2*np.pi*sigma)) * np.exp((-(x-(n * niu))**2)/(2*n*sigma))
    x = np.linspace(-1, 1, N)
    y = f(x)
    plt.plot(x, y, color = 'black', label = 'f(x)')
    plt.show()
    
    
ex4()


def ex5():
    n = 1000
    N = 100
    
    pasi = np.random.rand(n)
    values = np.zeros(n)
    values[pasi < 0.25] = -1
    values[(pasi >= 0.25) & (pasi < 0.75)] = 0
    values[pasi >= 0.75] = 1
    cumulativeSum = np.cumsum(values)
    
    nPoz = np.random.rand(N)
    valuesNPoz = np.zeros(n)
    
    for i in range(N-1):
        if nPoz[i] < 0.25:
            valuesNPoz[i] = -1
        elif nPoz[i] >= 0.75:
            valuesNPoz[i] = 1
        else:
            valuesNPoz[i] = 0
        
    #a 
    plt.figure()
    plt.plot(np.arange(1, n+1), cumulativeSum)
    plt.xlabel('Contor')
    plt.ylabel('Suma cumulativa')
    plt.show()
    
    #b
    plt.hist(valuesNPoz, bins = 100, density = True, color='red')
    plt.show()

    #c
    E = np.mean(values)
    patrat = np.square(values)
    niu = E
    sigma = np.sqrt(np.mean(patrat) - E**2)
    f = lambda x: 1/(np.sqrt(2*np.pi*sigma)) * np.exp((-(x-(n * niu))**2)/(2*n*sigma))
    x = np.linspace(-1, 1, N)
    y = f(x)
    plt.plot(x, y, color = 'black', label = 'f(x)')
    plt.show()

    
ex5()