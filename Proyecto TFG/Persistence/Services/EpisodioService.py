from Persistence.Repositories import EpisodioRepository, PacienteRepository, ServicioRepository, PatologiaRepository, CentroRepository


def get_all():
    return EpisodioRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return EpisodioRepository.get_by_id(ide)
    else:
        raise TypeError("El dato debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return EpisodioRepository.get_by_name(name)
    else:
        raise TypeError("El dato debe ser str")


def create(episodio):
    if episodio.nombre == "" or not isinstance(episodio.idpaciente, int) or not isinstance(episodio.idpatologia, int) \
            or not isinstance(episodio.idcentro, int) or not isinstance(episodio.idservicio, int):
        raise TypeError("La entidad tiene campos en blanco")
    EpisodioRepository.create(episodio)


def update(episodio):
    if episodio.nombre == "" or not isinstance(episodio.idpaciente, int) or not isinstance(episodio.idpatologia, int) \
            or not isinstance(episodio.idcentro, int) or not isinstance(episodio.idservicio, int) or not isinstance(episodio.id, int):
        raise TypeError("La entidad no esta bien construida")
    EpisodioRepository.update(episodio)


def delete(episodio):
    raise NotImplementedError("Esta opcion no se implementa")


def get_paciente(episodio):
    if episodio.nombre == "" or not isinstance(episodio.idpaciente, int) or not isinstance(episodio.idpatologia, int) \
            or not isinstance(episodio.idcentro, int) or not isinstance(episodio.idservicio, int) or not isinstance(episodio.id, int):
        raise TypeError("La entidad no esta bien construida")
    return PacienteRepository.get_by_id(episodio.idpaciente)


def get_servicio(episodio):
    if episodio.nombre == "" or not isinstance(episodio.idpaciente, int) or not isinstance(episodio.idpatologia, int) \
            or not isinstance(episodio.idcentro, int) or not isinstance(episodio.idservicio, int) or not isinstance(episodio.id, int):
        raise TypeError("La entidad no esta bien construida")
    return ServicioRepository.get_by_id(episodio.idservicio)


def get_patologia(episodio):
    if episodio.nombre == "" or not isinstance(episodio.idpaciente, int) or not isinstance(episodio.idpatologia, int) \
            or not isinstance(episodio.idcentro, int) or not isinstance(episodio.idservicio, int) or not isinstance(episodio.id, int):
        raise TypeError("La entidad no esta bien construida")
    return PatologiaRepository.get_by_id(episodio.idpatologia)


def get_centro(episodio):
    if episodio.nombre == "" or not isinstance(episodio.idpaciente, int) or not isinstance(episodio.idpatologia, int) \
            or not isinstance(episodio.idcentro, int) or not isinstance(episodio.idservicio, int) or not isinstance(episodio.id, int):
        raise TypeError("La entidad no esta bien construida")
    return CentroRepository.get_by_id(episodio.idcentro)


def get_pruebas(episodio):
    if episodio.nombre == "" or not isinstance(episodio.idpaciente, int) or not isinstance(episodio.idpatologia, int) \
            or not isinstance(episodio.idcentro, int) or not isinstance(episodio.idservicio, int) or not isinstance(episodio.id, int):
        raise TypeError("La entidad no esta bien construida")
    return EpisodioRepository.get_pruebas(episodio)


def get_diagnosticos(episodio):
    if episodio.nombre == "" or not isinstance(episodio.idpaciente, int) or not isinstance(episodio.idpatologia, int) \
            or not isinstance(episodio.idcentro, int) or not isinstance(episodio.idservicio, int) or not isinstance(episodio.id, int):
        raise TypeError("La entidad no esta bien construida")
    return EpisodioRepository.get_diagnosticos(episodio)


def get_procedimientos(episodio):
    if episodio.nombre == "" or not isinstance(episodio.idpaciente, int) or not isinstance(episodio.idpatologia, int) \
            or not isinstance(episodio.idcentro, int) or not isinstance(episodio.idservicio, int) or not isinstance(episodio.id, int):
        raise TypeError("La entidad no esta bien construida")
    return EpisodioRepository.get_procedimientos(episodio)


