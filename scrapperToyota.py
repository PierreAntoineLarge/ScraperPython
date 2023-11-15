from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

automobilePropreData = ''

for num in range(5):
    step = num
    linkToScrap = 'https://www.automobile-propre.com/marque/toyota/actualites/page/'+  str(step) + '/' 
    research = requests.get(linkToScrap)
    automobilePropreData += research.text
    
soup = BeautifulSoup(automobilePropreData, 'html.parser')  

h3_tags = soup.find_all('h3')

words_in_h3 = []

for h3_tag in h3_tags:
    words_in_h3.extend(h3_tag.text.split())

# Nettoyage de la liste en supprimant les mots de trois lettres et moins
cleaned_words_list = [mot for mot in words_in_h3 if len(mot) > 3]

# Utilisation de Counter pour compter le nombre d'occurrences de chaque mot
compteur = Counter(cleaned_words_list)

liste_triee_full = sorted(compteur.items(), key=lambda x: x[1], reverse=True)

liste_triee = liste_triee_full[:50]

# Divisez la liste triée en deux listes séparées pour l'axe x et l'axe y
mots, occurrences = zip(*liste_triee)

# Créez un diagramme barres
plt.bar(mots, occurrences, color='skyblue')
plt.xlabel('Mots')
plt.ylabel('Occurrences')
plt.title('Occurrences de mots')
plt.xticks(rotation=45, ha='right')  # Rotation des étiquettes sur l'axe x pour une meilleure lisibilité
plt.tight_layout()

# Affichez le diagramme
plt.show()





