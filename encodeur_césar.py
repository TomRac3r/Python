# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:54:03 2018

@author: Thomas
"""

"""Projet 7 : encodeur César """

#################################################################
###                       SECTION IMPORT                      ###
#################################################################

import string

#################################################################
###              SECTION DEFINITION DES CONSTANTES            ###
#################################################################

jeu_de_charactere = string.printable[:-5]   #charactères sur lesquels on va pouvoir faire un encodage
sub_char = jeu_de_charactere[-3:] + jeu_de_charactere[:-3]  #jeu de charactèes décaler de 3 charactères
##on colle les 3 derniers charactères [-3:] au début de la liste où l'on a retiré les 3 derniers charactères [:-3]
MSG_TEST = 'Message de test'
DICO_ENCRYPT = {}
for i, k in enumerate(jeu_de_charactere):
    v = sub_char[i]
    DICO_ENCRYPT[k]= v

#################################################################
###              SECTION DEFINITIN DES FONCTIONS              ###
#################################################################

def encrypter(texte_clair):
    """Fonction assurant le cryptage du texte en se servant du décalage instaurer 
    dans la partie "section  définition des constantes". Ici le décalage est de 3 
    charactères"""  

#################################################################
###                 SECTION MAIN DU PROGRAMME                 ###
#################################################################

encrypter(MSG_TEST)

#################################################################
###                         FIN                               ###
#################################################################