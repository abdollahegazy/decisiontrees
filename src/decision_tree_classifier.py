import numpy as np

from numpy.typing import NDArray
from .binary_tree import BinaryTree
from .node import Node
from typing import Tuple

class DecisionTreeClassifier(BinaryTree):
    def __init__(self,max_depth:int,
                 splitting_rule:str='gini') -> None:
        super().__init__()
        self.max_depth = max_depth
        self.splitting_rule = splitting_rule

        if splitting_rule not in ['misclassification_impurity','gini','entropy']:
            raise ValueError("Enter valid splitting rule")

    def _loss_fn(self,y:NDArray):
        pz = np.bincount(y) / len(y)
        if self.splitting_rule == 'misclassification_impurity':
            return 1 - np.max(pz)
        elif self.splitting_rule == 'gini':
            return 1 - np.sum(pz**2)
        elif self.splitting_rule == 'entropy':
            return -1*sum(pz[pz>0]*np.log2(pz[pz>0]))

    def _construct_subtree(self,node:Node,max_depth:int):
        if node.depth == max_depth or len(np.unique(node.y)) == 1:
            node.g = int(np.argmax(np.bincount(node.y)))
            return
        
        feature_idx,threshold = self._optimal_split(node)
        node.j, node.xi = feature_idx, threshold #type:ignore 
        Xt, yt, Xf, yf = self._data_split(node.x, node.y, feature_idx, threshold)

        if(len(yt)>0):
            node.left = Node(node.depth+1,Xt,yt)
            self._construct_subtree(node.left, max_depth)

        if(len(yf)>0):
            node.right = Node(node.depth+1, Xf,yf)
            self._construct_subtree(node.right, max_depth)

    def fit(self,x:NDArray,y:NDArray):
        self.root = Node(0,x,y)
        self._construct_subtree(node=self.root,max_depth=self.max_depth)
    
    def _data_split(self,x,y,feature,threshold):
        mask = x[:,feature] <= threshold
        x_true, x_false = x[mask,:],x[~mask,:]
        y_true, y_false = y[mask],y[~mask]
        return x_true,y_true,x_false,y_false

    def _optimal_split(self,node:Node) -> Tuple[int,float]:
        x = node.x  
        y = node.y
        n,m = x.shape
        best_feature = 0
        best_threshold = x[0,0]
        best_loss = self._loss_fn(node.y)

        # for each feature
        for feature_idx in range(0,m):
            # for each data point
            for i in range(0,n  ):
                threshold = x[i,feature_idx]
                _,y_true,_,y_false = self._data_split(x,y,feature_idx,threshold)
                loss_true,loss_false = self._loss_fn(y_true), self._loss_fn(y_false)
                split_loss = (len(y_true)/n) * loss_true + (len(y_false)/n) * loss_false
                if split_loss < best_loss:
                    best_loss = split_loss
                    best_feature = feature_idx
                    best_threshold = threshold
                
        return best_feature,best_threshold
    def predict(self,x) -> NDArray:

        # want to work for matrix of data points, so we can vectorize the prediction
        def _predict(x):
            def _predict(x,node:Node):
                if not node.right and not node.left:
                    return node.g
                if x[node.j] <= node.xi and node.left:
                    return _predict(x, node.left)
                elif x[node.j] > node.xi and node.right:
                    return _predict(x, node.right)
            return _predict(x, self.root)


        return np.apply_along_axis(_predict,1,x)
                








 





