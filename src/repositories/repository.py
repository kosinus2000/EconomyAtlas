from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Repository(Generic[T], ABC):

    @abstractmethod
    def add(self, item: T)-> None:
        pass

    @abstractmethod
    def get_by_id(self, item_id: int)-> T:
        pass


    @abstractmethod
    def get_by_name(self, name: str) -> T:
        pass

    @abstractmethod
    def get_all(self) -> list[T]:
        pass

class NotFoundError(LookupError):
    pass