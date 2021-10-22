import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, svm
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression
from sklearn import tree
from sklearn.neural_network import MLPRegressor
import pandas as pd

data= datasets.load_boston()

X = data.data
y = data.target
result = {}
MSE = []

# 最小二乘法
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=i)
    reg0 = linear_model.LinearRegression()
    reg0.fit(X_train,y_train)
    y_pred = reg0.predict(X_test)
    MSE.append(mean_squared_error(y_test,y_pred))

result["LSQ"]=MSE
MSE = []

# 岭回归
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=i)
    reg1 = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
    reg1.fit(X_train,y_train)
    y_pred = reg1.predict(X_test)
    MSE.append(mean_squared_error(y_test, y_pred))

result["ridge"]=MSE
MSE=[]

for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=i)
    reg2 = linear_model.Lasso()
    reg2.fit(X_train, y_train)
    y_pred = reg2.predict(X_test)
    MSE.append(mean_squared_error(y_test, y_pred))

result["lasso"]=MSE
MSE=[]


for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=i)
    regr = svm.SVR()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_test)
    MSE.append(mean_squared_error(y_test, y_pred))

result["svm"] = MSE
MSE = []

for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=i)
    regk = KNeighborsRegressor(n_neighbors=5, weights='distance')
    regk.fit(X_train, y_train)
    y_pred = regk.predict(X_test)
    MSE.append(mean_squared_error(y_test, y_pred))

result["KNN"] = MSE
MSE = []

for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=i)
    regp = PLSRegression(10)
    regp.fit(X_train, y_train)
    y_pred = regp.predict(X_test)
    MSE.append(mean_squared_error(y_test, y_pred))

result["PLS"] = MSE
MSE = []

for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=i)
    regt = tree.DecisionTreeRegressor()
    regt.fit(X_train, y_train)
    y_pred = regt.predict(X_test)
    MSE.append(mean_squared_error(y_test, y_pred))

result["tree"] = MSE
MSE = []

pd = pd.DataFrame(result)
pd.to_excel(r"1.xlsx")


