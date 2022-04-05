import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

my_dict = {'YearsExperience': [1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7, 3.9, 4.0, 4.0, 4.1, 4.5, 4.9, 5.1, 5.3, 5.9, 6.0, 6.8, 7.1, 7.9, 8.2, 8.7,
                               9.0, 9.5, 9.6, 10.3, 10.5],
           'Salary': [39343.00, 46205.00, 37731.00, 43525.00, 39891.00, 56642.00, 60150.00, 54445.00, 64445.00, 57189.00, 63218.00, 55794.00, 56957.00, 57081.00, 61111.00, 67938.00, 66029.00, 83088.00, 81363.00, 93940.00, 91738.00, 98273.00, 101302.00,
                      113812.00, 109431.00, 105582.00, 116969.00, 112635.00, 122391.00, 121872.00]
}
dataset = pd.DataFrame(my_dict)
dataset.head()
dataset.describe()
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print("\nLinearRegression()")
print(regressor.intercept_)
print(regressor.coef_)
#plt.scatter(dataset['YearsExperience'], dataset['Salary'], color = 'b', label='')
#plt.xlabel("Время")
#plt.ylabel("Рубли")
#plt.show()
y_pred = regressor.predict(X_test)
df = pd. DataFrame({'Actual': y_test, 'Predicted': y_pred})
df
df.plot(kind='bar')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
plt.scatter(X_test, y_test, color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()
