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
    id: int

@dataclass(kw_only=True)
class Voivodeship(EconomyAtlasBase):
    pass

@dataclass(kw_only=True)
class Powiat(EconomyAtlasBase):
    region_id: int



@dataclass(kw_only=True)
class AdministrationArea(EconomyAtlasBase):
    powiat_id: int
    area_type: AdministrationUnit
    location: tuple[float, float] | None = None








