# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:54:03 2018

@author: Thomas
"""

"""Projet 7 : el famoso codeur César !

**La première partie du projet contient la définition des différentes constantes. Dans cette section, 
on découpe l'ensemble des caractères pour le ré-ajuster et en faire notre dictionnaire de codage et
de décodage (DICO_ENCYPT / DICO_DECRYPT).

**la deuxième partie pose les deux fonctions de cryptage et décryptage.

**Dans la partie MAIN du programme, on ouvre un fichier texte contenant du texte...que l'on veut
crypter, on crypte se texte pour le stocker dans un fichier (on a donc un fichier "_IN" avec le texte 
que l'on cryptera puis un fichier "_OUT" qui lui contiendra le texte crypté.
Finalement, on ouvrira le fichier contenant le texte crypté, pour vérifier le bon déroulement du 
programme"""

#################################################################
##########################SECTION IMPORT#########################
#################################################################

import string

#################################################################
################SECTION DEFINITION DES CONSTANTES################
#################################################################

jeu_de_caractere = string.printable[:-5]   #caractères sur lesquels on va pouvoir faire un encodage
sub_car = jeu_de_caractere[-3:] + jeu_de_caractere[:-3]  #jeu de caractèes décaler de 3 caractères
##on colle les 3 derniers caractères [-3:] au début de la liste où l'on a retiré les 3 derniers caractères [:-3]
#MSG_A_CRYPTER = input('Saisir un texte à crypter : \n')

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
#Il y a une méthode plus simple pour les DICO, il suffit de d'alterner v et k entre les deux DICO...
 
#################################################################
#################SECTION DEFINITION DES FONCTIONS################
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
    
def decrypter(texte_secret, vardico_decrypt):
    """Fonction assurant le décryptage du texte en se servant du décalage instaurer 
    dans la partie "section  définition des constantes". Ici le décalage est de 3 
    charactères"""  
    texteclair = []
    for k in texte_secret:
        v = vardico_decrypt[k] 
        texteclair.append(v) 
    return ''.join(texteclair) 


#################################################################
####################SECTION MAIN DU PROGRAMME####################
#################################################################

    
with open('crypto_text_in.txt', 'r') as fichier_open_read :
    textesecret = fichier_open_read.read()

txt_encrypt = encrypter(textesecret, DICO_ENCRYPT)
print(textesecret)
print('')
print(txt_encrypt)

with open('crypto_text_out.txt', 'w') as fichier_open_write :
    fichier_open_write.write(txt_encrypt)
    
##########################SEPARATEUR#############################
    
with open('crypto_text_out.txt', 'r') as fichier_open_read :
    texteencrypter = fichier_open_read.read()

textedecrypter = decrypter(texteencrypter, DICO_DECRYPT)
print('')
print(textedecrypter)

#################################################################
###########################_FIN_#################################
#################################################################