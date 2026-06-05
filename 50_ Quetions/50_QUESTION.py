import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
#Chargement des données
dataset = pd.read_csv("C:\\Users\\sm720\\Desktop\\Mini_P\\Mini_P\\DATA\\healthcare-dataset-stroke-data.csv")
#Affichage des données
print(dataset.head(10))
# Q1. Créer un DataFrame à partir d’un dictionnaire python
data = {'gender': ['Male', 'Famale'], 'age': [5, 82]}
df = pd.DataFrame(data)
print(df)
# Q2. Vérifier la forme, la taille et les types des données
df.shape      # (lignes, colonnes)
df.size       # total d’éléments
df.dtypes     # types des colonnes
df.info()     # résumé complet
print("Shape (lignes, colonnes) :", df.shape)
# 2. Nombre total d’éléments (cells)
print("Size (total d'éléments) :", df.size)
# 3. Types de chaque colonne
print("Types des colonnes :")
print(df.dtypes)
# 4. Résumé complet
print("\nRésumé (info) :")
df.info()
# Q3. Obtenir les 5 premières et les 5 dernières lignes
df.head()     # premières lignes
df.tail()     # dernières lignes
# Afficher les 5 premières lignes (par défaut)
print(df.head())
# Afficher les 3 premières lignes (par exemple)
print(df.head(3))
# Afficher les 5 dernières lignes (par défaut)
print(df.tail())
# Afficher les 2 dernières lignes (par exemple)
print(df.tail(2))
df.head() # by default the command returns first five rows of the DataFrame
df.head().plot.bar() # the bar chart of heads of the DataFrame
#Q4. Renommer des colonnes
df.rename(columns={'Âge': 'Age'}, inplace=True)
print(df.columns)
# Q5. Réinitialiser et définir l’index
#df.reset_index(drop=True, inplace=True)     # réinitialiser
#df.set_index('gender', inplace=True)           # définir 'Nom' comme index
# 📂 Lecture et écriture de fichiers
# Q6. Lire et écrire des fichiers CSV/Excel
#df = pd.read_csv('fichier.csv')
#df.to_csv('nouveau.csv', index=False)
#df = pd.read_excel('fichier.xlsx')
df.to_excel('nouveau.xlsx', index=False)
# 🧬 Gestion des données catégorielles
# Q7. Gérer des données catégorielles
#df['type'] = df['type'].astype('categorie')
# 🧹 Données manquantes et doublons
# Q8. Détecter et gérer les données manquantes
df.isnull().sum()       # détection
# 1. Détection : compter les valeurs manquantes par colonne
print("Nombre de valeurs manquantes par colonne :")
print(df.isnull().sum())
# On peut aussi obtenir le total de toutes les valeurs manquantes :
print("Total de valeurs manquantes dans tout le DF :", df.isnull().sum().sum())
#df.fillna(valeur)       # remplissage
df.dropna()             # suppression
# 3. Suppression : éliminer les lignes (ou colonnes) qui contiennent des NaN
# Supprimer les lignes qui ont **au moins un** NaN (par défaut) :
df_dropped = df.dropna()
print("\nDataFrame après dropna (suppression des lignes avec NaN) :")
print(df_dropped)
df_cols_dropped = df.dropna(axis=1)
print("\nDataFrame après suppression des colonnes contenant des NaN :")
print(df_cols_dropped)
# Q9. Détecter et supprimer les doublons
df.drop_duplicates(inplace=True)
# Q10. Remplacer des valeurs spécifiques
df.replace({'ancien': 'nouveau'}, inplace=True)
# 🔄 Tri et indexation
# Q11. Trier par colonnes
# 1. Lire le CSV dans un DataFrame
df = pd.read_csv("C:/Users/sm720/Desktop/Mini_P/Mini_P/DATA/healthcare-dataset-stroke-data.csv")
# 2. Créer df_sorted en triant par 'age' décroissant
df_sorted = df.sort_values(by='age', ascending=False)
# 3. Afficher df_sorted
print(df_sorted)
# Afficher les noms de colonnes pour voir ce qu’ils sont
# print("Colonnes avant nettoyage:", df.columns)
# Nettoyer les noms de colonnes
df.columns = df.columns.str.strip()  # enlever les espaces
df.columns = df.columns.str.replace('age', 'age')  # renommer l’accentué
# (ou faire d’autres remplacements selon les besoins)
# print("Colonnes après nettoyage:", df.columns)
# Q12. Réinitialiser l’index
df.reset_index(drop=True)
# Q13. Sélectionner des lignes selon des conditions
df_filtered = df[df['age'] == 79]
print(df_filtered)
# 🧪 Filtrage et conditions
# Q14. Filtrer selon plusieurs conditions
df_filtered = df[(df['age'] > 25) & (df['gender'] == 'Male')]
print(df_filtered)
# Q15. Utiliser la méthode query()
df_filtered = df.query("age > 25 and gender == 'Female'")
print(df_filtered)
# Q16. Appliquer une fonction personnalisée ligne par ligne
#df.apply(lambda row: row['Age'] * 2, axis=1)
df_new = df.apply(lambda row: row['age'] * 2, axis=1)
print(df_new)
# 📊 Agrégations et regroupements
# Q17. Agrégations groupées
moyenne_age_par_genre = df.groupby('gender')['age'].mean()
print(moyenne_age_par_genre)
# Q18. Compter les éléments par groupe
df['gender'].value_counts(normalize=True)
# Q19. Classer à l’intérieur d’un groupe
df['rang'] = df.groupby('gender')['age'].rank(ascending=False, method='dense')
print(df)
# 🧬 Fusion et remodelage
# Q20. Fusionner deux DataFrames
#df_merged = pd.merge(df1, df2, on='Nom')
# Q21. Concaténer plusieurs DataFrames
# Concaténation verticale (ajouter les lignes de df2 sous celles de df1)
#df_vert = pd.concat([df1, df2], axis=0)  
#print("Verticalement :")
#print(df_vert)
# Concaténation horizontale (ajouter les colonnes de df2 à droite de celles de df1)
#df_horiz = pd.concat([df1, df2], axis=1)
#print("\nHorizontalement :")
#print(df_horiz)
#pd.concat([df1, df2], axis=0)     # verticalement
#pd.concat([df1, df2], axis=1)     # horizontalement
# Q22. Transformer avec pivot/melt
#df_pivoted = df.pivot(index='gender', columns='ever_married', values='age')
#print(df_pivoted)
# 📅 Opérations sur les dates
# Q23. Convertir une colonne en datetime
#df['Date'] = pd.to_datetime(df['Date'])
#print(df)
#print(df.dtypes)
# Q24. Extraire année, mois, jour, heure
#df['Année'] = df['Date'].dt.year
#df['Heure'] = df['Date'].dt.hour
df = pd.DataFrame({
'Date': pd.to_datetime(['2025-09-24 14:30:00', '2025-09-25 09:15:00'])
})
# Extraction des composants de la date
df['Année'] = df['Date'].dt.year
df['Mois'] = df['Date'].dt.month
df['Jour'] = df['Date'].dt.day
df['Heure'] = df['Date'].dt.hour
print(df)
# Q25. Filtrer selon une plage de dates
#df[df['Date'].between('2024-01-01', '2024-12-31')]
df_filtré = df[df['Date'].between('2024-01-01', '2024-12-31')]
print(df_filtré)
# Q26. Créer une colonne avec le jour de la semaine
df['Jour'] = df['Date'].dt.day_name()
print(df)
# Q27. Définir la colonne date comme index
df.set_index('Date', inplace=True)
## 🧪 Opérations avancées
# Q28. Créer une colonne combinée
#df['Nom_Complet'] = df['Prénom'] + ' ' + df['Nom']
# Q29. Utiliser np.where pour des catégories conditionnelles
# Créer une colonne “Groupe” selon la condition : si l’âge > 30 → “Senior”, sinon “Junior”
df['Groupe'] = np.where(df['age'] > 30, 'Senior', 'Junior')
print(df[['age', 'Groupe']].head())
# Q30. Mapper des valeurs via dictionnaire
df['Code'] = df['Ville'].map({'Nouakchott': 'NKC', 'Kaédi': 'KDI'})
# Q31. Modifier du texte (ex. minuscules)
df['Ville'] = df['Ville'].str.lower()
# Q32. Séparer une colonne texte en plusieurs
df[['Prénom', 'Nom']] = df['Nom_Complet'].str.split(' ', expand=True)
# 📈 Statistiques et fenêtres
# Q33. Calculer la corrélation
df.corr()
# Q34. Sommes ou produits cumulés
df['Cumulé'] = df['Valeur'].cumsum()
# Q35. Moyennes mobiles (rolling mean)
df['Rolling'] = df['Valeur'].rolling(window=3).mean()
# Q36. Différence ou pourcentage de changement
df['Diff'] = df['Valeur'].diff()
df['%Change'] = df['Valeur'].pct_change()
# Q37. Détecter valeurs aberrantes avec IQR
Q1 = df['Valeur'].quantile(0.25)
Q3 = df['Valeur'].quantile(0.75)
IQR = Q3 - Q1
df_outliers = df[(df['Valeur'] < Q1 - 1.5*IQR) | (df['Valeur'] > Q3 + 1.5*IQR)]
# Q38. Moyenne, médiane, écart-type, variance
df['Valeur'].mean()
df['Valeur'].median()
df['Valeur'].std()
df['Valeur'].var()
# 🔍 Analyse exploratoire
# Q39. Décrire rapidement un DataFrame
df.describe()
## Q40. Compter les occurrences d’une catégorie
df['Type'].value_counts()
# Q41. Obtenir les valeurs uniques + nombre
df['Type'].unique()
df['Type'].nunique()
# Q42. Skewness et kurtosis
df['Valeur'].skew()
df['Valeur'].kurt()
# Q43. Résumé synthétique avec info()
df.info()
# Q44. Évaluer la mémoire utilisée
df.memory_usage(deep=True)
## 📊 Visualisation
# Q45. Histogramme ou boxplot
df['Âge'].plot.hist()
df['Âge'].plot.box()
# Q46. Graphique en barres par catégorie
df['Type'].value_counts().plot.bar()
# Q47. Série temporelle avec index date
df['Valeur'].plot()
# Q48. Carte de corrélation avec seaborn
import seaborn as sns
sns.heatmap(df.corr(), annot=True)
# Q49. Graphiques avec matplotlib et taille
import matplotlib.pyplot as plt
df['Âge'].plot(figsize=(10,5))
plt.title('Distribution des âges')