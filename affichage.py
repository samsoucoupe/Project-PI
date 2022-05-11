from tkinter import *
from math import *
from constantes import *


class Aff_TK():
    
    def __init__(self,taille,param):
        self.taille=taille
        self.change=False
        self.fenetre = Tk()
        self.param=param
        self.fenetre.title("Labyrinthe")
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
        def inverse_hexa(hexa):
            hexa=hexa[1:]
            liste_normal=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
            liste_inverse=['f','e','d','c','b','a','9','8','7','6','5','4','3','2','1','0']
            hexa_inverse=""
            for elt in hexa:
                index=liste_normal.index(elt)
                hexa_inverse=hexa_inverse+liste_inverse[index]
            hexa_inverse="#"+hexa_inverse
            return hexa_inverse
        def inverse_couleur(couleur):
            liste_normal=["red","green","blue","yellow","purple","orange"]
            liste_inverse=["green","red","orange","purple","yellow","blue"]
            return liste_inverse[liste_normal.index(couleur)]
        if self.param.couleur[0]=="#":
            couleur_joueur=inverse_hexa(self.param.couleur)
        else:couleur_joueur=inverse_couleur(self.param.couleur)
        self.canvas.create_oval(joueur.a*n,joueur.o*n,joueur.a*n+n,joueur.o*n+n,fill = couleur_joueur)
        
    def resize(self,val):
        self.taille=int(val)
        self.change=True
         
    def fin(self):
        """Crée une fenetre de fin du jeu """
        txt="Vous avez gagne"
        fenetre_fin=Toplevel()
        fenetre_fin.title("Fin")
        Label(fenetre_fin,text=txt).pack()

if __name__ != '__main__':
    print("import de l'affichage check")