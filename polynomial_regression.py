
import operator

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # To read data

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

###random data
##np.random.seed(0)
##x = 2 - 3 * np.random.normal(0, 1, 20)
##y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)
### increasing the existing matrix by one additional dimension
##x = x[:, np.newaxis]
##y = y[:, np.newaxis]

#manually data
y=np.array([1,2,8,18,35,45,47,63,74,99])
x=np.array([3,6,9,12,24,28,34,38,68,89])
# increasing the existing matrix by one additional dimension
x = x[:, np.newaxis]
y = y[:, np.newaxis]

polynomial_features= PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(x)

#linear regression
model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)

#regresja liniowa
linear_regressor = LinearRegression()

linear_regressor.fit(x, y)
y_pred = linear_regressor.predict(x) #predictable value y


#mean squared error
#rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
#mse= np.mean((y - y_poly_pred)**2)
mse= mean_squared_error(y, y_poly_pred)
print('Mean square error: ',mse)
#R square value
r2 = r2_score(y,y_poly_pred)
print('R square value: ',r2)

#two-stage polynomial (degree=2)
polynomial_features= PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(x)
mse= mean_squared_error(x_poly,y)
print(mse)


#Plot
plt.title('Aproximation')
plt.plot(x, y_pred, color='blue', linewidth=1.5) #linear regression
plt.scatter(x, y, s=10,color='black')
#sorting value x
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)

#mean square error
#mse = np.sqrt(mean_squared_error(y,y_poly_pred))
#mse=  mean_squared_error(y, y_poly_pred)
#mse= np.mean((y - y_poly_pred)**2)
print('Mean square error in polynomial regression: ',mse)
#R square value
r2 = r2_score(y,y_poly_pred)
print('R square value: ',r2)


plt.plot(x, y_poly_pred, color='m') #polynomial regression
plt.show()

