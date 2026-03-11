from typing import Optional,Any
import numpy as np

class Node:
    def __init__(self,
                 depth: int,
                 x: Any,
                 y: Any,
                 left: Optional['Node'] = None,
                 right: Optional['Node'] = None,
                 ) -> None:
        self.depth = depth
        # feature and label vectors
        self.x = x
        self.y =y
        # split parameters
        self.j, self.xi = None,None
        # children
        self.left = left
        self.right = right
        # regional predictor function
        self.g: int | None = None
        # def loss(self):
        #     if(len(self.y)==0):
        #         return 0
        #     return np.sum(np.power(self.y - self.y.mean(),2))