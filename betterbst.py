from __future__ import annotations

from typing import List, Optional, Tuple, TypeVar
from algorithms.quicksort import quicksort

from data_structures.bst import BinarySearchTree
from data_structures.node import TreeNode

K = TypeVar("K")
I = TypeVar("I")


class BetterBST(BinarySearchTree[K, I]):
    def __init__(self, elements: List[Tuple[K, I]]) -> None:
        """
        Initialiser for the BetterBST class.
        We assume that the all the elements that will be inserted
        into the tree are contained within the elements list.

        As such you can assume the length of elements to be non-zero.
        The elements list will contain tuples of key, item pairs.

        First sort the elements list and then build a balanced tree from the sorted elements
        using the corresponding methods below.

        Args:
            elements(List[tuple[K, I]]): The elements to be inserted into the tree.

        Complexity:
            Best Case Complexity: O(NlogN * comp(K))
            Worst Case Complexity:  O(N^2 * comp(K))
        """
        super().__init__()
        new_elements: List[Tuple[K, I]] = self.__sort_elements(elements)
        self.__build_balanced_tree(new_elements)

    def __sort_elements(self, elements: List[Tuple[K, I]]) -> List[Tuple[K, I]]:
        """
        Recall one of the drawbacks to using a binary search tree is that it can become unbalanced.
        If we know the elements ahead of time, we can sort them and then build a balanced tree.
        This will help us maintain the O(log n) complexity for searching, inserting, and deleting elements.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to sort.

        Returns:
            list(Tuple[K, I]]) - elements after being sorted.

        Complexity:
            Best Case Complexity: O( NlogN * comp(K))

            Worst Case Complexity: O(N^2 * comp(K))

            where n is the number of elements in the list
            and K is the size of the sort Key, and comp(K) is the cost of comparison of keys K

            O(NlogN * comp(K)) is the best case complexity of quicksort

            O(N^2 * comp(K)) is the worst case complexity of quicksort
        """

        sorted_elements = []
        for item in elements:
            sorted_elements.append(item)
        quicksort(sorted_elements, sort_key=lambda x: x[0])

        return sorted_elements

    def __build_balanced_tree(self, elements: List[Tuple[K, I]]) -> None:
        """
        This method will build a balanced binary search tree from the sorted elements.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to use to build our balanced tree.

        Returns:
            None

        Complexity:
            (This is the actual complexity of your code,
            remember to define all variables used.)
            Best Case Complexity: O(n)

            Worst Case Complexity: O(n)

        Justification:
        where n is the number of elements in the elements list, the recursive function has
        a time complexity of O(1) for all of its operations, except for when it is calling itself.
        Overall the recursive function is called O(n) times.

        Complexity requirements for full marks:
            Best Case Complexity: O(n * log(n))
            Worst Case Complexity: O(n * log(n))
            where n is the number of elements in the list.
        """

        def recursive(list: List[Tuple[K, I]], depth: int) -> TreeNode[K, I] | None:

            if len(list) == 0:
                return None

            mid = len(list) // 2

            node = TreeNode(list[mid][0], list[mid][1], depth)

            left_side = list[:mid]
            right_side = list[mid + 1 :]

            node.left = recursive(left_side, depth + 1)  # type: ignore
            node.right = recursive(right_side, depth + 1)  # type: ignore

            return node

        root = recursive(elements, 1)

        self.root = root
        self.length = len(elements)


if __name__ == "__main__":
    bst = BetterBST([(0, "zero"), (2, "two"), (1, "one"), (6, "six"), (3, "three")])
