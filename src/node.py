from typing import Optional,Any

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
        # choldren
        self.left = left
        self.right = right