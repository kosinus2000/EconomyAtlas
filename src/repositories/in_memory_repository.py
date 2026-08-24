from repositories.repository import Repository, NotFoundError, T


class InMemoryRepository(Repository[T]):

    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def get_by_id(self, item_id: int) -> T:
        for item in self._items:
            if item.id == item_id:
                return item
        raise NotFoundError(f"Entity with id {item_id} not found")

    def get_by_name(self, name: str) -> T:
        for item in self._items:
            if item.name == name:
                return item
        raise NotFoundError(f"Entity with name {name} not found")

    def get_all(self) -> list[T]:
        return self._items.copy()