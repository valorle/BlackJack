# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:31:46 2017

@author: barthes
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img=mpimg.imread("test-01-carreau.png")

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,5),dpi=120)
imgplot = ax1.imshow(img)
ax1.axis('off')
ax2.axis('off')
imgplot = ax2.imshow(img)

ax1.text(10,300,'Joueur WWWW gagne')
ax2.text(10,300,'Joueur WWWW perd')