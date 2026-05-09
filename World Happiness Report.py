#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# 1. Chargement DIRECT 
df = pd.read_csv('2019.csv')

# 2. On affiche pour fêter ça !
print("Fichier 2019 chargé avec succès !")
print("Colonnes disponibles :", df.columns.tolist())
display(df.head())

# 3. Le graphique de corrélation
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='GDP per capita', y='Score', color='teal')
plt.title('Richesse vs Bonheur (Données 2019)')
plt.show()


# In[22]:


plt.figure(figsize=(12, 6))

# Nuage de points avec les noms de colonnes EXACTS de 2019
sns.regplot(data=df, x='GDP per capita', y='Score', 
            scatter_kws={'alpha':0.5, 'color':'teal'}, 
            line_kws={'color':'red', 'label':'Tendance'})

plt.title('Corrélation entre PIB et Score de Bonheur (Données 2019)', fontsize=14)
plt.xlabel('Richesse (PIB par habitant)')
plt.ylabel('Score de Bonheur')
plt.legend()
plt.show()



# In[24]:


# 1. On calcule les moyennes avec les colonnes de 2019
mean_score = df['Score'].mean()
mean_gdp = df['GDP per capita'].mean()

# 2. Pays "Sages" : PIB < moyenne mais Bonheur > moyenne + 0.5
outliers_happy = df[(df['GDP per capita'] < mean_gdp) & (df['Score'] > mean_score + 0.5)]

# 3. Pays "Riches mais Tristes" : PIB > moyenne + 0.3 mais Bonheur < moyenne
outliers_unhappy = df[(df['GDP per capita'] > mean_gdp + 0.3) & (df['Score'] < mean_score)]

print("--- Pays Exceptionnellement Heureux (Malgré un PIB plus bas) ---")
# On utilise 'Country or region' au lieu de 'Country name'
print(outliers_happy[['Country or region', 'Score', 'GDP per capita']].head())

print("\n--- Pays Riches avec un Bonheur Inattendu (Plus bas que prévu) ---")
print(outliers_unhappy[['Country or region', 'Score', 'GDP per capita']].head())



# In[25]:


# 1. Adapter les noms des facteurs pour le fichier 2019
factors_2019 = ['GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices']

# 2. Calculer les corrélations avec la colonne 'Score'
correlations = df[factors_2019 + ['Score']].corr()['Score'].sort_values(ascending=False)

# 3. Générer le graphique
plt.figure(figsize=(10, 6))
# On retire 'Score' pour ne garder que les facteurs influents
correlations.drop('Score').plot(kind='barh', color='orange')

plt.title('Quels facteurs influencent le plus le bonheur ? (Données 2019)')
plt.xlabel('Force de la corrélation (Coefficient de Pearson)')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()


# In[ ]:




