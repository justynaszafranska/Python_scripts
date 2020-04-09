import operator
import math 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # To read data

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

#dane randomowe
np.random.seed(0)
x = 2 - 3 * np.random.normal(0, 1, 20)
y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)
# zwiększanie istniejącej macierzy o jeden dodatkowy wymiar
x = x[:, np.newaxis]
y = y[:, np.newaxis]

#dane wpisane ręcznie
##y=np.array([1,2,8,18,35,45,47,63,74,99])
##x=np.array([3,6,9,12,24,28,34,38,68,89])
### zwiększanie istniejącej macierzy o jeden dodatkowy wymiary
##x = x[:, np.newaxis]
##y = y[:, np.newaxis]

###wczytywanie danych csv
##data = pd.read_csv('data.csv')
###wartosc konwertowane do numpy array
##x = data.iloc[:, 0].values.reshape(-1, 1)
##y = data.iloc[:, 1].values.reshape(-1, 1)

#wielomian dwustopniowy (degree=2)
polynomial_features= PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(x)


#regresja liniowa
model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)

#regresja liniowa
linear_regressor = LinearRegression()

# wykonywanie regresji liniowej
linear_regressor.fit(x, y)
y_pred = linear_regressor.predict(x) #wartosc przewidywalna y


#błąd sredniokwadratowy
rms = np.sqrt(mean_squared_error(y, y_pred))
print('Błąd średniokwadratowy wynosi regresji liniowej: ',rms)
#wartosc R kwadrat
r2 = r2_score(y,y_pred)
print('Wartość R kwadrat wynosi: ',r2)


#WYKRES
plt.title('Aproksymacja')
plt.plot(x, y_pred, color='blue', linewidth=1.5) #regresja liniowa 
plt.scatter(x, y, s=10,color='black')
# sortowanie wartość x 
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)


#błąd sredniokwadratowy
rms = np.sqrt(mean_squared_error(y, model.predict(x_poly)))
print('Błąd średniokwadratowy wynosi regresji wielomianowej: ',rms)
#wartosc R kwadrat
r2 = r2_score(y,model.predict(x_poly))
print('Wartość R kwadrat wynosi: ',r2)


plt.plot(x, y_poly_pred, color='m') #regresja wielomianowa
plt.show()


