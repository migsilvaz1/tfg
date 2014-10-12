from Persistence.Repositories import RelationsRepository
from Persistence.Domain import Material, Procedimiento, Episodio, Complicacion, PruebaDiagnostica


def add_material_to_procedimiento(procedimiento, material):
    if not isinstance(procedimiento, Procedimiento) or not isinstance(material, Material):
        raise TypeError("no se han introducidos los datos correctos")
    else:
        RelationsRepository.delete_procedimiento_mataterial(procedimiento, material)


def remove_material_from_procedimiento(procedimiento, material):
    if not isinstance(procedimiento, Procedimiento) or not isinstance(material, Material):
        raise TypeError("no se han introducidos los datos correctos")
    else:
        RelationsRepository.delete_procedimiento_mataterial(procedimiento, material)


def add_procedimiento_to_episodio(episodio, procedimiento):
    if not isinstance(procedimiento, Procedimiento) or not isinstance(episodio, Episodio):
        raise TypeError("no se han introducidos los datos correctos")
    else:
        RelationsRepository.create_episodio_procedimiento(episodio, procedimiento)


def remove_procedimiento_from_episodio(episodio, procedimiento):
    if not isinstance(procedimiento, Procedimiento) or not isinstance(episodio, Episodio):
        raise TypeError("no se han introducidos los datos correctos")
    else:
        RelationsRepository.delete_episodio_procedimiento(episodio, procedimiento)


def add_complicacion_to_procedimiento(complicacion, procedimiento):
    if not isinstance(procedimiento, Procedimiento) or not isinstance(complicacion, Complicacion):
        raise TypeError("no se han introducidos los datos correctos")
    else:
        RelationsRepository.create_complicacion_procedimiento(complicacion, procedimiento)


def remove_complicacion_from_procedimiento(complicacion, procedimiento):
    if not isinstance(procedimiento, Procedimiento) or not isinstance(complicacion, Complicacion):
        raise TypeError("no se han introducidos los datos correctos")
    else:
        RelationsRepository.delete_complicacion_procedimiento(complicacion, procedimiento)


def add_pdiagnostica_to_episodio(episodio, pdiagnostica):
    if not isinstance(episodio, Episodio) or not isinstance(pdiagnostica, PruebaDiagnostica):
        raise TypeError("no se han introducidos los datos correctos")
    else:
        RelationsRepository.create_episodio_pdiagnostica(episodio, pdiagnostica)


def remove_pdiagnostica_to_episodio(episodio, pdiagnostica):
    if not isinstance(episodio, Episodio) or not isinstance(pdiagnostica, PruebaDiagnostica):
        raise TypeError("no se han introducidos los datos correctos")
    else:
        RelationsRepository.delete_episodio_procedimiento(episodio, pdiagnostica)