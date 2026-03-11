
import numpy as np
#import classification dataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from src import DecisionTreeClassifier as DTC

def makedata():
    X, y = load_iris(return_X_y=True)
    return train_test_split(X, y, test_size=0.5, random_state=42)


from sklearn.tree import DecisionTreeClassifier as SklearnDTC
X_train, X_test, y_train, y_test = makedata()
# regTree = DecisionTreeRegressor(max_depth = 10, random_state=0)
# regTree.fit(X_train,y_train)
# y_hat = regTree.predict(X_test)
# MSE2 = np.mean(np.power(y_hat - y_test,2))
# print ("DecisionTreeRegressor: tree loss =", MSE2)
myTree = DTC(max_depth = 10, splitting_rule='entropy')
myTree.fit(X_train,y_train)
y_hat = myTree.predict(X_test)
accuracy = np.mean(y_hat == y_test)
print ("DecisionTreeClassifier: tree accuracy =", accuracy)