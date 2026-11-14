from typing import List

from sqlalchemy.orm import Session
from mappers import gmina_orm_to_dataclass, powiat_orm_to_dataclass, voivodeship_orm_to_dataclass
from models.population_model import Voivodeship
from models.sqlalchemy_models import VoivodeshipORM, GminaORM, PowiatORM
from repositories.repository import Repository, T, NotFoundError

MAPPERS = {
    VoivodeshipORM: voivodeship_orm_to_dataclass,
    PowiatORM: powiat_orm_to_dataclass,
    GminaORM: gmina_orm_to_dataclass,
}

class PostgresRepository(Repository[T]):

    def __init__(self, session: Session, orm_type):
        self.session = session
        self.orm_type = orm_type

    def get_mapper(self, orm_type):
        return MAPPERS[orm_type]

    def add(self, item: T) -> None:
        orm = self.orm_type(id=item.id, name=item.name)
        self.session.add(orm)
        self.session.commit()

    def get_by_id(self, item_id:int )-> T:
        orm = self.session.query(self.orm_type).get(item_id)
        if orm is None:
            raise NotFoundError(f'Not found: {item_id}')
        mapper = self.get_mapper(self.orm_type)
        return mapper(orm)

    def get_all(self) -> list[T]:
        orms = self.session.query(self.orm_type).all()
        mapper = self.get_mapper(self.orm_type)
        return [mapper(orm) for orm in orms]

    def get_by_name(self, name: str) -> T:
        orm = self.session.query(self.orm_type).filter(
            self.orm_type.name == name
        ).first()
        if orm is None:
            raise NotFoundError(f'Not found: {name}')
        mapper = self.get_mapper(self.orm_type)
        return mapper(orm)