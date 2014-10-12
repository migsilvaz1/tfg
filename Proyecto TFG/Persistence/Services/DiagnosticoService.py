from Persistence.Repositories import DiagnosticoRepository


def get_all():
    return DiagnosticoRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return DiagnosticoRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return DiagnosticoRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def create(diagnostico):
    if diagnostico.nombre == "" or not isinstance(diagnostico.idepisodio, int):
        raise TypeError("La entidad tiene campos en blanco")
    DiagnosticoRepository.create(diagnostico)


def update(diagnostico):
    if diagnostico.nombre == "" or not isinstance(diagnostico.idepisodio, int) or not isinstance(centro.id, int):
        raise TypeError("La entidad no esta bien construida")
    DiagnosticoRepository.update(diagnostico)


def delete(diagnostico):
    raise NotImplementedError("Esta opcion no se implementa")
