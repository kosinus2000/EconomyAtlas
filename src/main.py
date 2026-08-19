from src.models import population_model
from src.repositories.voivodeship_repository import InMemoryVoivodeshipRepository

woj = population_model.Voivodeship(name='Dolnosclaskie', region_id=1, area = None, population = None, pkb = None)
pow = population_model.Powiat(name='lubinski', region_id=1, powiat_id=1, area = None, population = None, pkb = None)
city  = population_model.AdministrationArea(name='wroclaw', administration_area_id=1, powiat_id=1, type=population_model.AdministrationUnit.MIASTO, area = None, population = None, pkb = None, location=None)

voiRep = InMemoryVoivodeshipRepository()
voiRep.add(woj)
voiRep.get_by_id(1)
voiRep.get_by_name('dupa')