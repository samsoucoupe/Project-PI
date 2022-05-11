from tkinter import *
from random import randint
from math import *
from constantes import *


listes_passe=[]

class case():
    def __init__(self,val,i,j,param):
        self.bas = True
        self.droite = True
        self.val = val
        self.x = i
        self.y = j
        self.param = param
        if param.couleur == "multi":
            self.color = convertEnHex(randint(50,250),randint(50,250),randint(50,250))
        elif param.couleur == None:
            self.color="black"
        else:
            self.color = param.couleur
            
    def __str__(self):
        return str(self.val)
    
    def dessiner(self,canvas):
        "seule fonction graphique"
        j = self.x * n
        i = self.y * n
        if self.val == 0: self.color = 'black'
        
        canvas.create_rectangle(i,j,i+n,j+n,fill = self.color,width = 0)
        #if self.val != 0:
            #canvas.create_text(i+n/2,j+n/2,text = self.val,fill = 'black')
        
def Creer(Cases,taille):
    # creer un nouveau chemin
    x = randint(0,taille-2) + 1

    if x%2 == 0:
        y = randint(0,((taille-1) / 2)) * 2 + 1    
    else:
        y = randint(0,ceil((taille-2) / 2)) * 2 + 2
    
    if x >=taille-1 or y >=taille-1:
        return
    
    if Cases[x-1][y].val == 0:
        case1 = Cases[x][y-1]
        case2 = Cases[x][y+1]
    else:
        case1 = Cases[x-1][y]
        case2 = Cases[x+1][y]
        
    val = case2.val
    
    if case1.val != case2.val:
        Cases[x][y].val=case1.val
        Cases[x][y].color = case1.color
        for i in range(taille-1):
            for j in range(taille):
                if Cases[i][j].val == val:
                    Cases[i][j].val = case1.val 
                    Cases[i][j].color = case1.color

                    
def pattern(Cases,x,taille,param):
    """ cree un patern sous la forme
    ## 
    #. 
    ## 
    ou # = mur
    . une case vide avec une valeur et une couleur defini au depart
    """
    global ct
    Cases.append([])
    Cases.append([])
    alt = 0
    for i in range(taille):
        Cases[x].append(case(0,x,i,param))
        
    for i in range(taille):
        if alt!=0:listes_passe.append((x,i))
        if i == taille-1 or x == taille-2: alt = 0
        Cases[x+1].append(case(alt,x+1,i,param))
        if alt != 0: alt = 0
        else:
            alt = ct
            ct=ct+1

def copy(taille,Cases,param):
    """ 
    ## ## ## ## #
    #. #. #. #. #
    ## ## ## ## #
    """
    for i in range(0,taille,2):
        pattern(Cases,i,taille,param)
    
    Cases[1][0].val = Cases[1][1].val
    Cases[1][0].color = Cases[1][1].color
    
    Cases[taille-2][taille-1].val = Cases[taille-2][taille-2].val
    Cases[taille-2][taille-1].color = Cases[taille-2][taille-2].color

def convertEnHex(r,g,b):
    d = '0123456789abcdef'
    rr = d[r//16]+d[r%16]
    gg = d[g//16]+d[g%16]
    bb = d[b//16]+d[b%16]
    return '#' + rr + gg + bb 

def Complex(Cases,ctComplex,taille):
    """
    ouvre taille/3 cases
    pour passer d'un chemin a plusieurs chemin
    """

    val = Cases[1][0].val
    color = Cases[1][0].color
    
    x = randint(0,taille-2) + 1

    if x%2 == 0:
        y = randint(0,((taille-1) / 2)) * 2 + 1    
    else:
        y = randint(0,ceil((taille-2) / 2)) * 2 + 2
        
    if x >=taille-1 or y >=taille-1:
        return ctComplex
    if Cases[x][y].val == 0:
        Cases[x][y].val = val
        Cases[x][y].color = color
        return ctComplex +1
    return ctComplex
    
        
def toutes_les_valeur(Cases,taille):
    """ return si toutes cases on la meme valeur de
    ce sert du faite de la suppresion des doublon des ensembles
    """
    e=set()
    for i in range(taille):
        for j in range(taille):
            if Cases[i][j].val!=0:
                e.add(Cases[i][j].val)
    return len(e)==1

def affiche_Cases(Cases):
    for i in range(taille-1):
        for j in range(taille-1):
            v=Cases[i][j].val
            if v==0:
                print("#",end="|")
            else:
                print(f"{v:0>3}",end="|")
        print()  




if __name__ == '__main__':
    parame=param()
    Cases=[]
    ctComplex = 0
    copy(taille=taille,Cases=Cases,param=parame)
    print("Patern initial")

    affiche_Cases(Cases)
    print('-----------------------------------------------------')
    
    while not toutes_les_valeur(Cases,taille):
        Creer(Cases,taille)
    
    print("Patern complexe")
    affiche_Cases(Cases)
    print('-----------------------------------------------------')
    
    while ctComplex<=3:
        ctComplex=Complex(Cases,ctComplex,taille)

    print("Patern final")
    affiche_Cases(Cases)
    
else:
    print("import du createur check")