from models import population_model
from repositories.in_memory_repository import InMemoryRepository


voi_repo = InMemoryRepository[population_model.Voivodeship]()
voi_repo.add(population_model.Voivodeship(id=1, name="dolnośląskie"))
print(voi_repo.get_by_id(1))

pow_repo = InMemoryRepository[population_model.Powiat]()
pow_repo.add(population_model.Powiat(id=1, name="lubiński", region_id=1))
print(pow_repo.get_all())