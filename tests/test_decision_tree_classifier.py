
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

myTree = DTC(max_depth = 10, splitting_rule='gini')
myTree.fit(X_train,y_train)
y_hat = myTree.predict(X_test)
accuracy = np.mean(y_hat == y_test)
print ("DecisionTreeClassifier: tree accuracy =", accuracy*100)

sklearn_tree = SklearnDTC(max_depth=10, criterion='gini', random_state=42)
sklearn_tree.fit(X_train, y_train)
y_hat_sklearn = sklearn_tree.predict(X_test)
accuracy_sklearn = np.mean(y_hat_sklearn == y_test)
print("Sklearn DecisionTreeClassifier: tree accuracy =", accuracy_sklearn*100)