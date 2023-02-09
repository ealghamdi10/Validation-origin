from s1_bfs.graph import *


class HanoiConfiguration(TransitionRelation):
     # état du jeu
    def __init__(self, taille, nbre_disque):
        self.conf=[[k for k in range(nbre_disque)]]
        for k in range(nbre_disque-1):
            self.conf.append([])
        self.size=taille
    def config(self):
        return self.conf
    def taille(self):
        return self.size

    def __hash__(self):
        return 1

    # def __eq__(self, other):
    #     if len(self.conf)!=other.conf:
    #         return False
    #     for i in range(len(self.conf)):
    #         if len(self.conf[i]) != other.conf[i]:
    #             return False
    #         for k in range(len(self.conf[i])):
    #             if self.conf[i][k]!=other.conf[i][k]:
    #                 return False
    #     return True  

    def __eq__(self, other):
        return self.conf==other.conf

    '''
    Ce code définit une classe appelée "HanoiConfiguration" qui est une sous-classe 
    de "TransitionRelation" d'un module "graph" importé. La classe a un constructeur 
    qui initialise l'objet avec deux paramètres "taille" et "nbre_disque", ce qui crée 
    une liste bidimensionnelle "conf" représentant l'état du jeu. La classe possède également 
    des méthodes pour retourner la configuration et la taille du jeu, ainsi que des méthodes 
    pour définir le hachage et la comparaison d'égalité de l'objet.
    '''

