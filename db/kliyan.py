from db.config import MONGO_DB


def anrejistre_metadata(metadata: dict):
    return MONGO_DB.db.metadata_anrejistreman.insert_one(metadata).inserted_id
