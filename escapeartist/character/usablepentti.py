"""
Abstraction allowing Pentti to have a common interface towards user
"""

from abc import ABC, abstractmethod

class UsablePentti(ABC):

    @abstractmethod
    def escape_maze(self, limit: int = 10000):
        """
        Calling this function will run the algorithm that makes Pentti escape the maze.

        """
        pass