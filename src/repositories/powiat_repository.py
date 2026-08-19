from src.models import population_model
from src.repositories.repository import Repository, NotFoundError


class InMemoryPowiatRepository(Repository[population_model.Powiat]):
    def __init__(self) -> None:
        self._items: list[population_model.Powiat] = []

    def add(self, powiat: population_model.Powiat) -> None:
        self._items.append(powiat)

    def get_by_id(self, item_id: int) -> population_model.Powiat:

        for item in self._items:
            if item.powiat_id == item_id:
                return item
        raise NotFoundError('Item not found')

    def get_by_name(self, name: str) -> population_model.Powiat:
        for item in self._items:
            if item.name == name:
                return item

        raise NotFoundError('Item not found')

    def get_all(self) -> list[population_model.Powiat]:
        return self._items