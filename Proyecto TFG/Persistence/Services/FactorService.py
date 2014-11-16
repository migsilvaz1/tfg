from Persistence.Repositories import FactorRepository


def get_all():
    return FactorRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return FactorRepository.get_by_id(ide)
    else:
        raise TypeError("El id debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return FactorRepository.get_by_name(name)
    else:
        raise TypeError("El nombre debe ser str")


def create(factor):
    if factor.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    FactorRepository.create(factor)


def update(factor):
    if factor.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(factor.id, int):
        raise TypeError("El id debe ser int")
    FactorRepository.update(factor)


def delete(factor):
    raise NotImplementedError("Esta opcion no se implementa")
