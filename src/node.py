from typing import Optional,Any

class Node:
    def __init__(self,value: Any | None= None,
                 left: Optional['Node'] = None,
                 right: Optional['Node'] = None) -> None:
        self.value = value
        self.left = left
        self.right = right