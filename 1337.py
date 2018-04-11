# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:10:36 2018

@author: Thomas
"""
""""Projet 6 : codeur 1337 5p34k =)"""

#################################################################
###                       SECTION IMPORT                      ###
#################################################################



#################################################################
###              SECTION DEFINITION DES CONSTANTES            ###
#################################################################

MESSAGE_TEST = input('Saisir un texte à coder : ')
TEST_SUBSTITUTION = [['a', '4'], ['e', '3'], ['l', '1'],['o', '0'],['t', '7']]

#################################################################
###              SECTION DEFINITIN DES FONCTIONS              ###
#################################################################

def codeur_1337(message, substitutions):
    """Fonction permettant de coder en leet/1337. On récupère un str puis on le code en 1337"""
    print('w3sh l3s kh3ys')
    print('')
    for s in substitutions:
        vieux_str = s[0]
        nouv_str = s[1]
        message = message.replace(vieux_str, nouv_str)
    print('Ceci est le message à coder : ', MESSAGE_TEST)
    print('')
    return print('Voici le message codé : ', message)
    
#################################################################
###                 SECTION MAIN DU PROGRAMME                 ###
#################################################################
    
codeur_1337(MESSAGE_TEST, TEST_SUBSTITUTION)