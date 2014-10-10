import CentroRepository
import QuerysRepository
from PatologiaRepository import get_by_id
print(CentroRepository.get_by_name("c"))
print(QuerysRepository.mortalidad_temprana_patologia(get_by_id(1)))

