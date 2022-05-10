from constantes import *
from createur import *
from affichage import Aff_TK
from option import option
from joueur import Joueur

class main():
    def __init__(self,taille,ct):
        self.taille=taille
        self.ct = ct
        self.ctComplex = 0                    
          
        self.Cases = []
        
    
        self.p = option(self.taille)
        self.param = self.p.param
        
        
        self.p.launch()
        self.taille = self.param.taille
        
        copy(self.taille,self.Cases,self.param)
        
        
        self.f=Aff_TK(self.taille)
        self.joueur=Joueur(1,0)
        self.ctComplexMax = self.taille/3 
        
    def launch(self):
        self.f.Dessin(self.Cases,self.joueur)
        if not toutes_les_valeur(self.Cases,self.taille):
            Creer(self.Cases,self.taille)
        elif self.ctComplex<self.ctComplexMax:
            self.ctComplex=Complex(self.Cases,self.ctComplex,self.taille)
        else:
            self.joueur.visible=True
            self.f.Dessin(self.Cases,self.joueur)
            return self.play()
        self.f.fenetre.after(15,self.launch)
        
    def play(self):
        if self.joueur.fin((self.taille-2,self.taille-1)):
            print("fini")
            self.joueur.fini=True
            return self.joueur.deplacer(self.Cases,self.f,self.taille)
        else:
            self.joueur.deplacer(self.Cases,self.f,self.taille)
            self.f.fenetre.after(15,self.play)

        
        
    def Dessiner_les_patern(self):
        self.f.Dessin(self.Cases)
            

M=main(taille,ct)
#M.Dessiner_les_patern()
M.launch()


M.f.fenetre.mainloop()