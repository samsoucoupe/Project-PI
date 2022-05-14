from tkinter import *
from constantes import *
from tkinter.colorchooser import askcolor
class option():
    def __init__(self,taille):
        self.taille = taille
        self.param = param()
        self.vals = ["multi","red","green","blue","yellow","purple","orange","perso"]
        self.fenetre_option = Tk()
        self.fenetre_option.title('Option')
        self.fenetre_option.resizable(width=False, height=False)#non resizable
        self.info = Label(self.fenetre_option,text=texte_recomendation).pack()

        self.scale = Scale(self.fenetre_option, variable=self.taille,orient='horizontal',from_=taille_min, to=taille_max, resolution=2,length=200,label="Taille du labyrinth",cursor='question_arrow',command=self.resize)
        self.scale.set(self.taille)
        self.scale.pack()
        self.info_couleur = Label(self.fenetre_option,text=texte_couleur).pack()
        self.couleur_Var = StringVar()
        self.couleur_Var.set(self.vals[0])
        self.param.couleur =  self.couleur_Var

        self.quelle_couleur()
        for i in range(len(self.vals)):
            self.b = Radiobutton(self.fenetre_option, text=self.vals[i], variable=self.couleur_Var,value=self.vals[i],cursor='question_arrow', command=self.quelle_couleur)
            self.b.pack(side='left', expand=1)


        self.h=50*len(self.vals)
        self.l=100*len(self.vals)
        self.Valider = Button(self.fenetre_option, text='Valider',cursor='rtl_logo', command=self.fenetre_option.destroy).place(x=self.l/2,y=self.h*0.9)
        
        
        
        
        self.fenetre_option.geometry(f'{self.l}x{self.h}')
        

    def resize(self,val):
       self.param.taille=int(val)

       
    def launch(self):
        self.fenetre_option.mainloop()
    
    
    def quelle_couleur(self):
        couleur = self.couleur_Var.get()
        if couleur == self.vals[-1]:
            couleur = askcolor()
            self.param.couleur = couleur[1]
        else:
            self.param.couleur = couleur
        

    
if __name__ != '__main__':
    print("import fenetre option  check")