from tkinter import *
from constantes import *

class Joueur():
    def __init__(self,o0,a0) :
        self.o=o0
        self.a=a0
        self.visible=False
        self.fini=False

    def fin(self,arrivee):
        return (self.o,self.a)==arrivee
    
        
        
    def deplacer(self,Cases,fen,taille):   
           
        def up(p=None):
            if self.o>0:
                if Cases[self.o-1][self.a].val!=0:
                    self.o-=1
                    self.draw(Cases,fen)
                    
        def down(p=None):
            if self.o<taille-1:
                if Cases[self.o+1][self.a].val!=0:
                    self.o+=1
                    self.draw(Cases,fen)
                    
        def left(p=None):
            if self.a>0:
                if Cases[self.o][self.a-1].val!=0:
                    self.a-=1
                    self.draw(Cases,fen)
                    
        def right(p=None):
            if self.a < taille-1:
                if Cases[self.o][self.a+1].val!=0 :
                    self.a+=1
                    self.draw(Cases,fen)
                

        
                  
        fen.fenetre.bind("<Up>" , up)
        fen.fenetre.bind("<Down>", down)
        fen.fenetre.bind("<Left>", left)
        fen.fenetre.bind("<Right>", right)
        
        if self.fini:
            self.visible=False
            fen.fenetre.unbind("<Up>")
            fen.fenetre.unbind("<Down>")
            fen.fenetre.unbind("<Left>")
            fen.fenetre.unbind("<Right>")
        

            
    
    def draw(self,Cases,fen):
        
        if (self.o,self.a)==(taille-1,taille-2):  
            fen.fenetre.label("fini")
        else:
            fen.Dessin(Cases,self)
        
            
    