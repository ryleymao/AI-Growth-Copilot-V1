from __future__ import annotations
from typing import Optional, List


class TreeNode:
    def __init__(self, key: int, val):
        self.key: int = key
        self.val = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class TreeMap:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, key: int, val) -> None:
        """Insert or update key->val."""
        if self.root is None:
            self.root = TreeNode(key, val)
            return

        curr = self.root
        while True:
            if key < curr.key:
                if curr.left is None:
                    curr.left = TreeNode(key, val)
                    return
                curr = curr.left
            elif key > curr.key:
                if curr.right is None:
                    curr.right = TreeNode(key, val)
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int):
        """Return value for key or None if not found."""
        curr = self.root
        while curr is not None:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return None

    def remove(self, key: int) -> None:
        """Remove key if present."""
        self.root = self._remove_helper(self.root, key)

    def _remove_helper(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._remove_helper(node.left, key)
            return node
        elif key > node.key:
            node.right = self._remove_helper(node.right, key)
            return node
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            min_node = self._min_node(node.right)
            node.key, node.val = min_node.key, min_node.val
            node.right = self._remove_helper(node.right, min_node.key)
            return node

    def _min_node(self, node: TreeNode) -> TreeNode:
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def getInorderKeys(self) -> List[int]:
        result: List[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[TreeNode], out: List[int]) -> None:
        if node is not None:
            self._inorder(node.left, out)
            out.append(node.key)
            self._inorder(node.right, out)

    def printInorder(self) -> None:
        """Print keys in sorted order on one line."""
        def inorder(n: Optional[TreeNode]) -> None:
            if n is not None:
                inorder(n.left)
                print(n.key, end=" ")
                inorder(n.right)
        inorder(self.root)
        print()

    def contains(self, key: int) -> bool:
        current = self.root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return True
        return False

    def size(self) -> int:
        def count_nodes(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        return count_nodes(self.root)

    def height(self) -> int:
        def node_height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + max(node_height(node.left), node_height(node.right))
        return node_height(self.root)

    def isEmpty(self) -> bool:
        return self.root is None

    def minKey(self) -> Optional[int]:
        if self.root is None:
            return None
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.key

    def maxKey(self) -> Optional[int]:
        if self.root is None:
            return None
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.key

# tests for proper functioning
if __name__ == "__main__":
    t = TreeMap()
    t.insert(5, "root")
    t.insert(3, "left")
    t.insert(7, "right")

    print("Contains 5?", t.contains(5))
    print("Contains 4?", t.contains(4))
    print("Tree size:", t.size())
    print("Tree height:", t.height())
    print("Is tree empty?", t.isEmpty())
    print("Inorder traversal:")
    t.printInorder()
    print("Min key:", t.minKey())
    print("Max key:", t.maxKey())
