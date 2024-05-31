import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('ENFLASYON.xlsx')

df = df.dropna()

ortalama_gelir = df['TÜRKİYE/KÜRESEL'].mean()
max_gelir = df['TÜRKİYE/KÜRESEL'].max()
min_gelir = df['TÜRKİYE/KÜRESEL'].min()

print(ortalama_gelir)
print(max_gelir)
print(min_gelir)

plt.plot(df['YIL'], df['TÜRKİYE/KÜRESEL'])
plt.show()
