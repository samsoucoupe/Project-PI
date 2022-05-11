Cases = []
taille_min=11
taille_max=51
taille=31
n = 20
ct = 1

texte_recomendation = "Recommandation : \n\n\
    Pour commencer vous pouvez lancer le fichier créateur.py pour visualiser la version sans le Tkinter.\n\n\
        Ensuite, pour la partie affichage, je conseille de lance avec une taille de 31, même si la version avec 51 est plus impressionnante mais plus longue.\n"
texte_couleur="Couleur : \n\n\
    Vous avez différentes couleurs pour les patterns.\n\n\
        La recommandation est de choisir multi, car c'est avec celle-ci que la compréhension est la meilleure.\n\
            Ensuite, il y a des couleurs prédéfinies plus classique \n\
                Pour finir perso pour choisir une couleur personnelle."
class param:
    def __init__(self):
        self.couleur = None
        self.taille=31