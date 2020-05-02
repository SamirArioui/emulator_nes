from abc import abstractmethod, ABC
from typing import List


class MemoryOwnerMixin(ABC):
    # TODO check we have correct amount if memory
    @property
    def memory_start_location(self) -> int:
        """
        inclusive
        """
        pass

    @property
    def memory_end_location(self) -> int:
        """
        inclusive
        """
        pass

    @abstractmethod
    def get_memory(self) -> List[int]:
        pass

    def get(self, position: int) -> int:
        """
        get int at a given position and size
        """
        return self.get_memory()[position - self.memory_start_location]

    def set(self, position: int, value: int):
        """
        get int at a given position and size
        """
        self.get_memory()[position - self.memory_start_location] = value
