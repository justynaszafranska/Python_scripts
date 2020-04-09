import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression ,ElasticNet

#wczytanie danych csv
data = pd.read_csv('data.csv')

#wartosc konwertowane do numpy array
X = data.iloc[:, 0].values.reshape(-1, 1)
Y = data.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class

# wykonywanie regresji liniowej
linear_regressor.fit(X, Y)

Y_pred = linear_regressor.predict(X)

#wykres
plt.scatter(X, Y,  color='black')
plt.plot(X, Y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())
plt.title('Regresja liniowa')
plt.show()

#Współczynnik determinacji R^2
regrEN = ElasticNet(normalize=True)
regrEN.fit(X,Y)
print ('Współczynnik determinacji wynosi: ',regrEN.score(X,Y))
