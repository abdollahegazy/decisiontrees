from collections import deque
from typing import List
from .node import Node

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    # def _build_tree(self,data: List[Any],start: int,end: int) -> Optional[Node]:
    #     if start > end:
    #         return None
    #     mid = (start + end) // 2
    #     node = Node(data[mid])
    #     node.left = self._build_tree(data,start,mid-1)
    #     node.right = self._build_tree(data,mid+1,end)
    #     return node

    def level_order(self) -> List[Node]:
        nodes = []
        q = deque([self.root])
        while q:
            node = q.popleft()

            if node:
                nodes.append(node)
                q.append(node.left)
                q.append(node.right)
        return nodes

    def __str__(self):
        lines = []
        def _build(node, prefix="", is_left=True):
            if not node:
                return
            if node.right:
                _build(node.right, prefix + ("│   " if is_left else "    "), False)
            connector = "└── " if is_left else "┌── "
            lines.append(prefix + connector + str(node.value))
            if node.left:
                _build(node.left, prefix + ("    " if is_left else "│   "), True)
        if self.root:
            _build(self.root, "", True)
        return "\n".join(lines)