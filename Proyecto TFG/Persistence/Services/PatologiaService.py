from Persistence.Repositories import PatologiaRepository


def get_all():
    return PatologiaRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return PatologiaRepository.get_by_id(ide)
    else:
        raise TypeError("El id debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return PatologiaRepository.get_by_name(name)
    else:
        raise TypeError("El nombre debe ser str")


def create(patologia):
    if patologia.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    PatologiaRepository.create(patologia)


def update(patologia):
    if patologia.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(patologia.id, int):
        raise TypeError("El id debe ser int")
    PatologiaRepository.update(patologia)


def delete(patologia):
    raise NotImplementedError("Esta opcion no se implementa")


def get_episodios(patologia):
    if patologia.nombre == "":
        raise TypeError("El nombre no puede estar en blanco")
    if not isinstance(patologia.id, int):
        raise TypeError("El id debe ser int")
    return PatologiaRepository.get_procedimientos(patologia)