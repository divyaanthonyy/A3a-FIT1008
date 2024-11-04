from __future__ import annotations
from data_structures.bst import BSTInOrderIterator, BinarySearchTree
from data_structures.heap import MaxHeap

from data_structures.heap import MaxHeap
from data_structures.node import TreeNode

"""
Ensure you have read the introduction and task 1 and understand what 
is prohibited in this task.
This includes:
The ban on inbuilt sort methods .sort() or sorted() in this task.
And ensure your treasure data structure is not banned.

"""
from abc import ABC, abstractmethod
from typing import List, cast

from config import Tiles
from treasure import Treasure, generate_treasures


class Hollow(ABC):
    """
    DO NOT MODIFY THIS CLASS
    Mystical troves of treasure that can be found in the maze
    There are two types of hollows that can be found in the maze:
    - Spooky Hollows: Each of these hollows contains unique treasures that can be found nowhere else in the maze.
    - Mystical Hollows: These hollows contain a random assortment of treasures like the spooky hollow however all mystical hollows are connected, so if you remove a treasure from one mystical hollow, it will be removed from all other mystical hollows.
    """

    # DO NOT MODIFY THIS ABSTRACT CLASS
    """
    Initialises the treasures in this hollow
    """

    def __init__(self) -> None:
        self.treasures = self.gen_treasures()
        self.restructure_hollow()

    @staticmethod
    def gen_treasures() -> List[Treasure]:
        """
        This is done here, so we can replace it later on in the auto marker.
        This method contains the logic to generate treasures for the hollows.

        Returns:
            List[Treasure]: A list of treasures that can be found in the maze
        """
        return generate_treasures()

    @abstractmethod
    def restructure_hollow(self):
        pass

    @abstractmethod
    def get_optimal_treasure(self, backpack_capacity: int) -> Treasure | None:
        pass

    def __len__(self) -> int:
        """
        After the restructure_hollow method is called, the treasures attribute should be updated
        don't create an additional attribute to store the number of treasures in the hollow.
        """
        return len(self.treasures)


class SpookyHollow(Hollow):

    def restructure_hollow(self) -> None:
        """
        Re-arranges the treasures in the hollow from a list to a new
        data structure that is better suited for the get_optimal_treasure method.

        The new treasures data structure can't be an ArrayR or list variant (LinkedList, python list, sorted list, ...).
        No lists! Breaching this will count as a major error and lose up to 100% of the marks of the task!

        Returns:
            None - This method should update the treasures attribute of the hollow

        Complexity:
            (This is the actual complexity of your code,
            remember to define all variables used.)
            Best Case Complexity: O(n log n)
            Worst Case Complexity: O(n log n)

            where n is the number of items in the list

            log n is the depth of the binary search tree

        Complexity requirements for full marks:
            Best Case Complexity: O(n log n)
            Worst Case Complexity: O(n log n)
            Where n is the number of treasures in the hollow
        """

        spooky_structure = BinarySearchTree[float, Treasure]()
        i = 0

        for treasure in cast(List[Treasure], self.treasures):
            ratio = treasure.value / treasure.weight
            ratio = ratio * -1  # To make the InOrder iterator return the values in descending order
            spooky_structure[ratio] = treasure

        self.treasures = spooky_structure

    def get_optimal_treasure(self, backpack_capacity: int) -> Treasure | None:
        """
        Removes the ideal treasure from the hollow
        Takes the treasure which has the greatest value / weight ratio
        that is less than or equal to the backpack_capacity of the player as
        we can't carry treasures that are heavier than our backpack capacity.

        Ensure there are only changes to the treasures contained in the hollow
        if there is a viable treasure to take. If there is a viable treasure
        only remove that treasure from the hollow, no other treasures should be removed.

        Returns:
            Treasure - the ideal treasure that the player should take.
            None - if all treasures are heavier than the backpack_capacity
            or the hollow is empty

        Complexity:
            (This is the actual complexity of your code,
            remember to define all variables used.)
            Best Case Complexity: O(log n)
            Worst Case Complexity: O(n)

            where n is the number of treasures in the hollow


        Complexity requirements for full marks:
            Best Case Complexity: O(log(n))
            Worst Case Complexity: O(n)
            where n is the number of treasures in the hollow
        """

        for node in self.treasures:
            item: Treasure = node.item

            if item.weight <= backpack_capacity:
                del self.treasures[node.key]
                return item

        return None

    def __str__(self) -> str:
        return Tiles.SPOOKY_HOLLOW.value

    def __repr__(self) -> str:
        return str(self)


class MysticalHollow(Hollow):

    def restructure_hollow(self):
        """
        Re-arranges the treasures in the hollow from a list to a new
        data structure that is better suited for the get_optimal_treasure method.

        The new treasures data structure can't be an ArrayR or list variant (LinkedList, python list, sorted list, ...).
        No lists! Breaching this will count as a major error and lose up to 100% of the marks of the task!

        Returns:
            None - This method should update the treasures attribute of the hollow

        Complexity:
            (This is the actual complexity of your code,
            remember to define all variables used.)
            Best Case Complexity: O(n)
            Worst Case Complexity: O(n)

        Complexity requirements for full marks:
            Best Case Complexity: O(n)
            Worst Case Complexity: O(n)
            Where n is the number of treasures in the hollow

            The best and worst case complexities are both O(n)
            as the complexity is dependent on the heapify function, which
            is O(n) is both best and worst case scenarios.

        """
        heap: MaxHeap[Treasure] = MaxHeap.heapify(self.treasures)
        self.treasures = heap

    def get_optimal_treasure(self, backpack_capacity: int) -> Treasure | None:
        """
        Removes the ideal treasure from the hollow
        Takes the treasure which has the greatest value / weight ratio
        that is less than or equal to the backpack_capacity of the player as
        we can't carry treasures that are heavier than our backpack capacity.

        Ensure there are only changes to the treasures contained in the hollow
        if there is a viable treasure to take. If there is a viable treasure
        only remove that treasure from the hollow, no other treasures should be removed.

        Returns:
            Treasure - the ideal treasure that the player should take.
            None - if all treasures are heavier than the backpack_capacity
            or the hollow is empty

        Complexity:
            (This is the actual complexity of your code,
            remember to define all variables used.)
            Best Case Complexity: O(log n)

            The best case complexity occurs when the first treasure
            returned by get.max() is the optimal treasure. Therefore the
            time complexity is O(1) multiplied by the complexity of
            the get_max() function which is O(log n)

            Worst Case Complexity: O(n log n)

            The worst case complexity occurs when all of the treasures
            in the hollow are heavier than the backpack capacity, which
            means that the get_max() function will run n times (n is the number
            of elements in self.treasures), resulting in a complexity of
            O(n log n)

            Placing back the temporarily removed treasures has a worst time complexity
            of O(n log n)

        Complexity requirements for full marks:
            Best Case Complexity: O(log n)
            Worst Case Complexity: O(n log n)
            Where n is the number of treasures in the hollow
        """

        temp = []
        found_item: None | Treasure = None

        while len(self.treasures) > 0:
            item = self.treasures.get_max()
            if item.weight <= backpack_capacity:
                found_item = item
                break
            else:
                temp.append(item)

        for item in temp:
            self.treasures.add(item)

        return found_item

    def __str__(self) -> str:
        return Tiles.MYSTICAL_HOLLOW.value

    def __repr__(self) -> str:
        return str(self)


if __name__ == "__main__":
    spook = SpookyHollow()
    butt = spook.get_optimal_treasure(10)
    print("BOO", butt)
