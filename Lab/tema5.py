import numpy as np
import random
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------------------------
#----------------------------------------EX 4-------------------------------------------------
#---------------------------------------------------------------------------------------------
# 

def ex4():
    N=100000
    x1 = x2 = x3 = x4 = x5 = x6 = x7 = 0


    for i in range(N):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
    
        #A  
        if x>=50:
            x1+=1
        #B
        if y >= 50:
            x2+=1
        #C    
        if x>=78 and y<=50:
            x3+=1
        #A si B      
        if(x>=50 and y>=50):
            x4+=1
        # A si C 
        if(x>=78 and x>=50 and y<=50):
            x5+=1
        #B si C        
        if(y>=50 and x>=78 and y<=50):
            x6+=1
            
        #A B si C        
        if(x>=50 and y>=50 and x>=78 and y<=50):
            x6+=1
            
        
    print("A independent de B:",x4/N,(x1*x2)/(N*N))
    print("A independent de C:", x5/N, (x1*x3)/(N*N))
    print("B independent de C:", x6/N, (x2*x3)/(N*N)) 
    print("A B C independente:", x7/N, (x1*x2*x3)/(N*N*N)) 


#---------------------------------------------------------------------------------------------
#-------------------------------------------EX 6----------------------------------------------
#---------------------------------------------------------------------------------------------


m=100
goal = 150
bet = 0.5
multiplier = 1
rulari = []   
N=10000

#0 = verde, 1=rosu, 2=negru
#dand mai multe valori pentru bet-ul initial, se poate observa ca daca ai mai multi bani initial ai sanse mai mici
#de a pierde (pierderea realizandu-se cand pica negru de log2(banii tai))    
#aceasta idee am implementat-o in vara sub forma unui bot ce joaca automat la ruleta ( mi-am pierdut 60% din bani :)) )
#o varianta ce produce mai putini bani dar care are sanse mai mici de a pierde este de a aplica fibonacci in loc de dublare

R = [(0,0),(1,1),(2,2),(3,1),(4,2),(5,1),(6,2),(7,1),(8,2),(9,1),(10,2),(11,2),(12,1),(13,2),(14,1),(15,2),(16,1),(17,2),(18,1),(19,1),(20,2),(21,1),(22,2),(23,1),(24,2),(25,1),(26,2),(27,1),(28,2),(29,2),(30,1),(31,2),(32,1),(33,2),(34,1),(35,2),(36,1)]

#programul joaca doar pe rosu
def play():
    play = random.choice(R)
    if play[1] == 1:
        return True
    return False

def game(m,bet,multiplier,goal):
    nrJocuri = 0
    while m>0 and m<goal:
        if play() == True:
            if bet*multiplier < m: #in cazul in care jucatorul nu este all in
                m+=bet*multiplier
                multiplier = 1
            else: #altfel, daca e all in, se dubleaza suma
                m=m*2 
        else:
            if bet*multiplier < m: #daca 
                m-=bet*multiplier
                multiplier*=2 #daca pierde dubleaza bet-ul pentru a isi recupera pierderea + un castig de 0.5
            else:
                m=0 #a intrat all in si a pierdut
                
        nrJocuri+=1
        
    if m==0:
        #print("Ai pierdut tot, fraiere",nrJocuri)
        return False,nrJocuri
    #print("Ai atins goal-ul, esti top",nrJocuri)
    return True,nrJocuri

   
def simulare(N):
    n=0
    for i in range(N):
        win, nrJocuri = game(m,bet,multiplier,goal)
        if win == True:
            n+=1
            
        rulari.append(nrJocuri)
      
      
    print("Win rate:",n/N)
      
    plt.hist(rulari, bins=1000)
    plt.show()  
    

#ex4()
simulare(N)


        
    
    
    

    