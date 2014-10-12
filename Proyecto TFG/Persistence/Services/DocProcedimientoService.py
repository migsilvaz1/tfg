from Persistence.Repositories import BlobRepository
from Persistence.Domain import Procedimiento


def upload_doc(referenced_to, path):
    data = BlobRepository.load_from_path(path)
    BlobRepository.save_blob(data, 'documentos_procedimiento', referenced_to)


def get_by_id(ide):
    if isinstance(ide, int):
        return BlobRepository.get_blob_by_id(ide, 'documentos_procedimiento', 'doc')
    else:
        raise TypeError("El id debe ser un integer")


def get_all_docs_from_entity(procedimiento, path):
    if isinstance(procedimiento, Procedimiento):
        lista = BlobRepository.getall_blob_from_entity('id_procedimiento', procedimiento, 'documentos_procedimiento', 'doc')
        for i in lista:
            BlobRepository.rebuild_blob(i, path)
    else:
        raise TypeError("Se debe introducir un procedimiento")
