from typing import TypeVar, Generic

from models.population_model import Voivodeship, AdministrationArea, Powiat
from models.sqlalchemy_models import VoivodeshipORM, PowiatORM, GminaORM


def voivodeship_orm_to_dataclass(orm: VoivodeshipORM) -> Voivodeship:
    return Voivodeship(
        id=orm.id,
        name=orm.name,
    )

def powiat_orm_to_dataclass(orm: PowiatORM) -> Powiat:
    return Powiat(
        id=orm.id,
        name=orm.name,
        region_id=orm.region_id
    )

def gmina_orm_to_dataclass(orm: GminaORM) -> AdministrationArea:
    return AdministrationArea(
        id=orm.id,
        name=orm.name,
        powiat_id=orm.powiat_id
    )