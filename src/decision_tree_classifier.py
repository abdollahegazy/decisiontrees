from binary_tree import BinaryTree
import numpy as np

from numpy.typing import NDArray

class DecisionTreeClassifier(BinaryTree):
    def __init__(self,termination_criterion,splitting_rule) -> None:
        super().__init__()


    def terminate(self):
        ...

    def _construct_subtree(self,v,x,y):

        if self.terminate():
            self.fit(x,y)
            return
        
        s_v = self._split(v)
        vt,vf = ...

    def _sucessors(self):
        ...

    def fit(self,x,y):
        ...
    def predict(self):
        ...
    def _split(self,v):
        ...






 





