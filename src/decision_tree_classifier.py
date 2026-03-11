import numpy as np

from numpy.typing import NDArray
from binary_tree import BinaryTree
from node import Node

class DecisionTreeClassifier(BinaryTree):
    def __init__(self,termination_criterion,splitting_rule) -> None:
        super().__init__()


    def terminate(self):
        ...

    def _loss_fn(self):
        ...

    def _construct_subtree(self,v,x:NDArray,y:NDArray):

        if self.terminate():
            return np.argmax(np.bincount(y) / len(y))

        
        s_v = self._split(v)
        vt,vf = ...

    def _sucessors(self):
        ...

    def fit(self,X:NDArray,y:NDArray):
        ...
    def predict(self):
        ...
    
    def _data_split(self,x,y,feature,threshold):
        mask = x[:,feature]<=threshold
        x_true, x_false = x[mask,:],x[~mask,:]
        y_true, y_false = y[mask,:],y[~mask,:]
        return x_true,y_true,x_false,y_false

    def _split(self,node:Node):
        x = node.x
        y = node.y
        n,m = x.shape
        best_feature = 0
        best_threshold = x[0,0]
        # best_split_val = node.CalculateLoss()
        best_loss = ...

        # for each feature
        for feature_idx in range(0,m):
            # for each data point
            for i in range(0,n):
                threshold = x[i,feature_idx]
                x_true,y_true,x_false,y_false = self._data_split(x,y,feature_idx,threshold)
                tmp_true = Node(0,x_true,y_true)
                tmp_false = Node(0,x_false,y_false)
                loss_true,loss_false = ...
                split_loss = loss_true + loss_false
                if split_loss < best_loss:
                    best_loss = split_loss
                    best_feature = feature_idx
                    best_threshold = threshold
                
        return best_feature,best_threshold









 





