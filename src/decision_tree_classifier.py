from binary_tree import BinaryTree
import numpy as np

from numpy.typing import NDArray

class DecisionTreeClassifier(BinaryTree):
    def __init__(self,termination_criterion,splitting_rule) -> None:
        super().__init__()


    def terminate(self):
        ...

    def _construct_subtree(self,v,x:NDArray,y:NDArray):

        if self.terminate():
            return np.argmax(np.bincount(y) / len(y))

        
        s_v = self._split(v)
        vt,vf = ...

    def _sucessors(self):
        ...

    def fit(self,y:NDArray):
        ...
    def predict(self):
        ...
    def _split(self,v):
        ''
        pz = np.bincount(len(y))
        ...






 





