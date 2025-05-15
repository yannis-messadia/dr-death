import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('shipman-times-comparison.csv')  

print(df['Shipman'])

plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='Hour', hue='Shipman', shade=True, common_norm=False, palette=['red', 'blue'])

plt.title("Densité des heures de décès : Shipman vs autres médecins")
plt.xlabel("Heure du décès (0-23)")
plt.ylabel("Densité")
plt.xlim(0, 23)
plt.grid(True)
plt.show()