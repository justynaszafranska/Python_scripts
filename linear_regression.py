import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression ,ElasticNet

#loading CSV data
data = pd.read_csv('data.csv')

#convert to numpy array
X = data.iloc[:, 0].values.reshape(-1, 1)
Y = data.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class

#linear regression
linear_regressor.fit(X, Y)

Y_pred = linear_regressor.predict(X)

#plot
plt.scatter(X, Y,  color='black')
plt.plot(X, Y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())
plt.title('Linear regression')
plt.show()

#coefficient of determination R square
regrEN = ElasticNet(normalize=True)
regrEN.fit(X,Y)
print ('Coefficient of determination: ',regrEN.score(X,Y))
