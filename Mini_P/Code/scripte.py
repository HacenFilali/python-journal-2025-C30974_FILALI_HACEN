# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 11:40:27 2025

@author: Hacen Filali
"""
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
#Chargement des données
dataset = pd.read_csv("C:\\Users\\Hacen Filali\\Desktop\\Mini_P\\DATA\\healthcare-dataset-stroke-data.csv")

#Affichage des données
print(dataset.head(10))
# Q1. Créer un DataFrame à partir d’un dictionnaire
data = {'gender': ['Male', 'Female'], 'Âge': [25, 30]}
df = pd.DataFrame(data)
# Q2. Vérifier la forme, la taille et les types des données
df.shape      # (lignes, colonnes)
df.size       # total d’éléments
df.dtypes     # types des colonnes
df.info()     # résumé complet