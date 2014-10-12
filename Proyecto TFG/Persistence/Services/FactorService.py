from Persistence.Repositories import FactorRepository


def get_all():
    return FactorRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return FactorRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return FactorRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def create(factor):
    if factor.nombre == "":
        raise TypeError("La entidad tiene campos en blanco")
    FactorRepository.create(factor)


def update(factor):
    if factor.nombre == "" or not isinstance(factor.id, int):
        raise TypeError("La entidad no esta bien construida")
    FactorRepository.update(factor)


def delete(factor):
    raise NotImplementedError("Esta opcion no se implementa")
