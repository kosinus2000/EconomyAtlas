from src.models import population_model
from src.repositories.repository import Repository, NotFoundError

class InMemoryVoivodeshipRepository(Repository[population_model.Voivodeship]):
    def __init__(self) -> None:
        self._items: list[population_model.Voivodeship] = []

    def add(self, item: population_model.Voivodeship) -> None:
        self._items.append(item)

    def get_by_id(self, item_id: int) -> population_model.Voivodeship:

        for item in self._items:
            if item.region_id == item_id:
                return item

        raise NotFoundError('Voivodeship not found')


    def get_by_name(self, name: str) -> population_model.Voivodeship:
        for item in self._items:
            if item.name == name:
                return item
        raise NotFoundError('Voivodeship not found')

    def get_all(self) -> list[population_model.Voivodeship]:
        return self._items