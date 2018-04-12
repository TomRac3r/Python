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

jeu_de_caractere = string.printable[:-5]   #caractères sur lesquels on va pouvoir faire un encodage
sub_car = jeu_de_caractere[-3:] + jeu_de_caractere[:-3]  #jeu de caractèes décaler de 3 caractères
##on colle les 3 derniers caractères [-3:] au début de la liste où l'on a retiré les 3 derniers caractères [:-3]
MSG_TEST = "J'adore les monty Python"

DICO_ENCRYPT = {}
for i, k in enumerate(jeu_de_caractere):
    #print(i, k)
    v = sub_car[i]
    #print(v)
    DICO_ENCRYPT[k] = v
    #print(DICO_ENCRYPT)
for c in string.printable[-5:]: #on rajoute les caractères spéciaux a la fin du dico
    DICO_ENCRYPT[c] = c
    #print(DICO_ENCRYPT)
    
DICO_DECRYPT ={}
for i, k in enumerate(sub_car):
    v = jeu_de_caractere[i]
    DICO_DECRYPT[k] = v
for c in string.printable[-5:]:
    DICO_DECRYPT[c] = c
    
#################################################################
###              SECTION DEFINITIN DES FONCTIONS              ###
#################################################################

def encrypter(texte_clair, vardico_crypt):
    """Fonction assurant le cryptage du texte en se servant du décalage instaurer 
    dans la partie "section  définition des constantes". Ici le décalage est de 3 
    charactères"""  
    textesecret = [] #liste vide pour stocker les charactères une fois cryptés
    for k in texte_clair:
        v = vardico_crypt[k] #on parcourt le texte à encrypter pour stocker chaque charactères dans 
                             #une liste
        #print(v)
        textesecret.append(v) #on stock les charactères chiffrés dans la liste de sortie
    return ''.join(textesecret) #on renvoi le texte crypté

#####################SEPARATION FONCTIONS########################
    
def decrypter(textesecret, vardico_decrypt):
    """Fonction assurant le décryptage du texte en se servant du décalage instaurer 
    dans la partie "section  définition des constantes". Ici le décalage est de 3 
    charactères"""  
    texteclair = [] #liste vide pour stocker les charactères une fois cryptés
    for k in textesecret:
        v = vardico_decrypt[k] #on parcourt le texte à encrypter pour stocker chaque charactères dans 
                             #une liste
        #print(v)
        texteclair.append(v) #on stock les charactères chiffrés dans la liste de sortie
    return ''.join(texteclair) #on renvoi le texte crypté

#################################################################
###                 SECTION MAIN DU PROGRAMME                 ###
#################################################################

textesecret = encrypter(MSG_TEST, DICO_ENCRYPT)
print(MSG_TEST)
print(textesecret)
texteclair = decrypter(textesecret, DICO_DECRYPT)
print(texteclair)
#################################################################
###                         FIN                               ###
#################################################################