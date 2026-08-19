from dataclasses import dataclass
from enum import Enum

class AdministrationUnit(Enum):

    MIASTO = 'miasto'
    GMINA_WIEJSKA = 'gmina wiejska'
    GMINA_MIEJSKO_WIEJSKA = 'gmina miejsko-wiejska'
    MIASTO_W_GMINIE = 'miasto w gminie miejsko-wiejskiej'
    OBSZAR_WIEJSKI_W_GMINIE = 'obszar wiejski w gminie miejsko-wiejskiej'

@dataclass(kw_only=True)
class EconomyAtlasBase:
    area: float | None = None
    population: int | None = None
    pkb: float | None = None
    name: str

@dataclass
class Voivodeship(EconomyAtlasBase):
    region_id: int


@dataclass
class Powiat(EconomyAtlasBase):
    powiat_id: int
    region_id: int



@dataclass
class AdministrationArea(EconomyAtlasBase):
    administration_area_id: int
    powiat_id: int
    type: AdministrationUnit
    location: tuple[float, float] | None








