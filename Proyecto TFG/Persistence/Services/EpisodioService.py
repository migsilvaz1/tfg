from Persistence.Repositories import EpisodioRepository, PacienteRepository, ServicioRepository, PatologiaRepository, CentroRepository


def get_all():
    return EpisodioRepository.get_all()


def get_by_id(ide):
    if isinstance(ide, int):
        return EpisodioRepository.get_by_id(ide)
    else:
        raise TypeError("El id debe ser int")


def get_by_name(name):
    if isinstance(name, str):
        return EpisodioRepository.get_by_name(name)
    else:
        raise TypeError("El nombre debe ser str")


def create(episodio):
    if episodio.nombre == "":
        raise TypeError("EL nombre no puede estar en blanco")
    if not isinstance(episodio.idpaciente, int):
        raise TypeError("Debe tener un paciente asociado")
    if not isinstance(episodio.idpatologia, int):
        raise TypeError("Debe tener una patologia asociada")
    if not isinstance(episodio.idcentro, int):
        raise TypeError("Debe tener un centro asociado")
    if not isinstance(episodio.idservicio, int):
        raise TypeError("Debe tener un servicio asociado")
    return EpisodioRepository.create(episodio)


def update(episodio):
    if not isinstance(episodio.id, int):
        raise TypeError("El id debe ser int")
    if episodio.nombre == "":
        raise TypeError("EL nombre no puede estar en blanco")
    if not isinstance(episodio.idpaciente, int):
        raise TypeError("Debe tener un paciente asociado")
    if not isinstance(episodio.idpatologia, int):
        raise TypeError("Debe tener una patologia asociada")
    if not isinstance(episodio.idcentro, int):
        raise TypeError("Debe tener un centro asociado")
    if not isinstance(episodio.idservicio, int):
        raise TypeError("Debe tener un servicio asociado")
    EpisodioRepository.update(episodio)


def delete(episodio):
    raise NotImplementedError("Esta opcion no se implementa")


def get_paciente(episodio):
    if not isinstance(episodio.idpaciente, int):
        raise TypeError("No tiene un paciente asociado")
    return PacienteRepository.get_by_id(episodio.idpaciente)


def get_servicio(episodio):
    if not isinstance(episodio.idservicio, int):
        raise TypeError("No tiene un servicio asociado")
    return ServicioRepository.get_by_id(episodio.idservicio)


def get_patologia(episodio):
    if not isinstance(episodio.idpatologia, int):
        raise TypeError("No tiene una patologia asociada")
    return PatologiaRepository.get_by_id(episodio.idpatologia)


def get_centro(episodio):
    if not isinstance(episodio.idcentro, int):
        raise TypeError("No tiene un centro asociado")
    return CentroRepository.get_by_id(episodio.idcentro)


def get_pruebas(episodio):
    if not isinstance(episodio.id, int):
        raise TypeError("El id debe ser int")
    if episodio.nombre == "":
        raise TypeError("EL nombre no puede estar en blanco")
    if not isinstance(episodio.idpaciente, int):
        raise TypeError("Debe tener un paciente asociado")
    if not isinstance(episodio.idpatologia, int):
        raise TypeError("Debe tener una patologia asociada")
    if not isinstance(episodio.idcentro, int):
        raise TypeError("Debe tener un centro asociado")
    if not isinstance(episodio.idservicio, int):
        raise TypeError("Debe tener un servicio asociado")
    return EpisodioRepository.get_pruebas(episodio)


def get_diagnosticos(episodio):
    if not isinstance(episodio.id, int):
        raise TypeError("El id debe ser int")
    if episodio.nombre == "":
        raise TypeError("EL nombre no puede estar en blanco")
    if not isinstance(episodio.idpaciente, int):
        raise TypeError("Debe tener un paciente asociado")
    if not isinstance(episodio.idpatologia, int):
        raise TypeError("Debe tener una patologia asociada")
    if not isinstance(episodio.idcentro, int):
        raise TypeError("Debe tener un centro asociado")
    if not isinstance(episodio.idservicio, int):
        raise TypeError("Debe tener un servicio asociado")
    return EpisodioRepository.get_diagnosticos(episodio)


def get_procedimientos(episodio):
    if not isinstance(episodio.id, int):
        raise TypeError("El id debe ser int")
    if episodio.nombre == "":
        raise TypeError("EL nombre no puede estar en blanco")
    if not isinstance(episodio.idpaciente, int):
        raise TypeError("Debe tener un paciente asociado")
    if not isinstance(episodio.idpatologia, int):
        raise TypeError("Debe tener una patologia asociada")
    if not isinstance(episodio.idcentro, int):
        raise TypeError("Debe tener un centro asociado")
    if not isinstance(episodio.idservicio, int):
        raise TypeError("Debe tener un servicio asociado")
    return EpisodioRepository.get_procedimientos(episodio)


