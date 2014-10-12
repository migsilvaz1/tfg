from Persistence.Repositories import RadiologoRepository


def get_all():
    return RadiologoRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return RadiologoRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return RadiologoRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def create(radiologo):
    if radiologo.nombre == "":
        raise TypeError("La entidad tiene campos en blanco")
    RadiologoRepository.create(radiologo)


def update(radiologo):
    if radiologo.nombre == "" or not isinstance(radiologo.id, int):
        raise TypeError("La entidad no esta bien construida")
    RadiologoRepository.update(radiologo)


def delete(radiologo):
    raise NotImplementedError("Esta opcion no se implementa")