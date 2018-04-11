# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

"""Programmer avec Python en s'amusant, Projet 3 'Un jeu de devinette'"""
import random

#import antigravity
#import this

#################################################################
#################################################################
##                      BLOC INTER-LIGNE                       ##
#################################################################
#################################################################

def bonjour_random():
    """Fonction affichant un bonjour random parmis 4 choix =)"""
    nb_rand = random.randint(1, 5)
    if (nb_rand == 1):
        print('Yo !')
    elif (nb_rand == 2):
        print('Wesh alors !')
    elif (nb_rand == 3):
        print('Mes salutations camarade !')
    elif (nb_rand == 4):
        print('#YOLO')
    elif (nb_rand == 5):
        import this
              
#################################################################
#################################################################
##                      BLOC INTER-LIGNE                       ##
#################################################################
#################################################################
        
def nombre_random() :
    """Fonction pour faire un nombre random dans l'intervalle [0, 10]"""
    nb_random = random.randint(0, 10)
    return nb_random

#################################################################
#################################################################
##                      BLOC INTER-LIGNE                       ##
#################################################################
#################################################################

def devinette_nombre():
    """Fonction permettant un petit jeu de devinette, on génére un nb_random puis on le compare avec
    un nombre saisi par l'utilisateur (nbr_du_joueur) / On affiche aussi le nb_esai avec un simple
    incrément à chaque tentative."""
    nb_random = random.randint(0, 3)
    nb_essai = 0
    INVITE = 'Saisi un nombre : ' 
#INVITE est en majuscules car c'est une constante, 
##convention d'écriture : variable=minuscules / CONSTANTES=MAJUSCULES
    while True:
        nbr_du_joueur = input(INVITE)
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
    return nb_essai

#################################################################
#################################################################
##                      BLOC INTER-LIGNE                       ##
#################################################################
#################################################################      
         
def jouer():
    """Fonction permettant le jeu 'devinette_nombre' avec un pseudo-menu !"""
    comptr_partie = 0
    while True :
        CONTINUER = 'Veux-tu coninuer à jouer ?! 1 pour oui / 2 pour non : '
        saisie_continuer = input(CONTINUER)
        if (int(saisie_continuer) == 1):
            print("Et c'est parti pour un tour !")
            comptr_partie = comptr_partie + 1
            print('Tu as déjà fait ', comptr_partie, 'partie(s) !')
            devinette_nombre()
        elif (int(saisie_continuer) == 2):
            print('Aurevoir !')
            break  
    return print('Tu as fait ',comptr_partie, ' partie(s) au total !')
    
#################################################################
#################################################################
##                      BLOC INTER-LIGNE                       ##
#################################################################
#################################################################
bonjour_random()
jouer()