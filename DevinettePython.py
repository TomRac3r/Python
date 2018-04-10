# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

"""Programmer avec Python en s'amusant, Projet 3 'Un jeu de devinette'"""
import random

#import antigravity
#import this

def bonjour_random():
    """Fonction affichant un bonjour random =)"""
    nb_rand = random.randint(1, 3)
    if (nb_rand == 1):
        print('Yo !')
    elif (nb_rand == 2):
        print('Wesh alors !')
    elif (nb_rand == 3):
        print('Mes salutations camarade !')


def nombre_random() :
    """Fonction pour faire un nombre random dans l'intervalle [0, 10]"""
    nb_random = random.randint(0, 10)


def devinette_nombre():
    """Fonction permettant un petit jeu de devinette"""
    nb_essai = 0
    while True:
        nbr_du_joueur = input('Saisi un nombre : ')
        if (nb_random == int(nbr_du_joueur)):
            print("GG mon gral ! t'as trouvé")
            print('Tu as essayé ', nb_essai, ' fois avant de réussir!')
            break
        elif (int(nbr_du_joueur) > nb_random):
            print('Ton nombre est plus grand ! essaye encore...')
        elif (int(nbr_du_joueur) < nb_random):
            print('Ton nombre est plus petit...essaye encore !')
        nb_essai = nb_essai + 1
        print('Tu es déjà à ton ', nb_essai, ' essai...')
        
bonjour_random()        
