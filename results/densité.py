import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv('shipman-times-comparison.csv')

# Afficher un aperçu pour vérification
print(df.head())

# Tracer les distributions KDE pour chaque colonne
plt.figure(figsize=(10, 6))

sns.kdeplot(df['Shipman'].dropna(), label='Shipman', shade=True, color='red')
sns.kdeplot(df['Comparison'].dropna(), label='Medecins généralistes', shade=True, color='blue')

# Mise en forme du graphique
plt.title("Densité des heures de décès")
plt.xlabel("Heure du décès")
plt.ylabel("Densité")
plt.xlim(0, 23)
plt.grid(True)
plt.legend()
plt.show()
