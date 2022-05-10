from tkinter import *
from math import *
from constantes import *


class Aff_TK():
    
    def __init__(self,taille):
        self.taille=taille
        self.change=False
        self.fenetre = Tk()
        
        self.fenetre.resizable(width=False, height=False)#non resizable
        self.canvas = Canvas(self.fenetre,height = self.taille*n,width = self.taille*n)

        
    def Dessin(self,Cases,joueur):
        """ fonction d'affichage """

        self.canvas.delete('all')
        for i in range(self.taille):
            for j in range(self.taille):

                Cases[i][j].dessiner(self.canvas)
        if joueur.visible:
            self.affiche_joueur(joueur)
        self.canvas.pack()
        
    
    def affiche_joueur(self,joueur):
        #cree un cercle de diametre n au cordonee du joueur
        self.canvas.create_oval(joueur.a*n,joueur.o*n,joueur.a*n+n,joueur.o*n+n,fill = 'red')
        
    def resize(self,val):
        self.taille=int(val)
        self.change=True
         
