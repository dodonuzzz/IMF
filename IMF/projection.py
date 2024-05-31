import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

# IMF.xlsx dosyasını okuma
df = pd.read_excel('IMF.xlsx')

# Veriyi özellikler ve hedef değişken olarak ayırma
X = df['YIL'].values.reshape(-1,1)
y = df['TÜRKİYE ($)'].values.reshape(-1,1)

# Lineer regresyon modelini eğitme
regressor = LinearRegression()
regressor.fit(X, y)

# Tahmin etmek istediğiniz yıllar
future_years = np.array(range(2030, 2051)).reshape(-1,1)

# Gelecek yıllar için tahmin yapma
future_preds = regressor.predict(future_years)

# Tahminleri yazdırma
for year, pred in zip(future_years, future_preds):
    print(f"Yıl: {year[0]}, Tahmin: {pred[0]}")
