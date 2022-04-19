import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree

from sklearn import metrics
from sklearn.tree import DecisionTreeRegressor

url = "https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv"
dataset = pd.read_csv(url)
dataset.head()
print(dataset.shape)
dataset.describe()

plt.scatter(dataset["alcohol"],dataset["residual sugar"])
plt.ylabel("alcohol")
plt.xlabel("residual sugar`")
plt.show()

dataset.head()
X = dataset.iloc[:,6].values
y = dataset.iloc[:,-6].values
print(X)
print(y)
xtrain,xtest,ytrain,ytest = train_test_split(X.reshape(-1,1),y,test_size=0.2,random_state=0)
regres = DecisionTreeRegressor()
regres.fit(xtrain,ytrain)
tree.plot_tree(regres)
ypred =regres.predict(xtest)
df = pd.DataFrame({"realnost":ytest, "predskaz":ypred})
print(ypred)
print(df)
print("kvad osh  ", metrics.mean_squared_error(ytest,ypred))
print("abs osh  ",metrics.mean_absolute_error(ytest,ypred))
print(metrics.mean_absolute_error(ytest,ypred)/np.average(y)*100)