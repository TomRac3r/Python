# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

#import antigravity
#import this

mon_invite = 'Propose un nombre : '
y = random.randint(0, 10)

while True:
    nbr_du_joueur = input(mon_invite)
    if (y == int(nbr_du_joueur)):
        print("gg mon gral ! t'as trouvé")
        break
    elif (int(nbr_du_joueur) > y):
        print('ton nombre est plus grand ! essaye encore...')
    elif (int(nbr_du_joueur) < y):
        print('ton nombre est plus petit...essaye encore !')
