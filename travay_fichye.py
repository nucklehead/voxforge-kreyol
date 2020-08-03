import json
import uuid
from zipfile import ZipFile

from werkzeug.datastructures import FileStorage


def kreye_metadata_fichye(non_fichye: str):
    with ZipFile(non_fichye, mode='r') as fichyeZip:
        metadata = {
            'abrejistreman': {},
            'pwofil': {}
        }
        with fichyeZip.open('debug.json') as fichyeAndan:
            metadata['abrejistreman'] = json.load(fichyeAndan)['prompts']
        with fichyeZip.open('profile.json') as fichyeAndan:
            metadata['pwofil'] = json.load(fichyeAndan)

    return metadata


def anrejistre_fichye_sou_disk(fichye: FileStorage) -> str:
    non_fichye = f'{uuid.uuid4()}.zip'
    with open(non_fichye, 'wb') as fichye_local:
        gwose_moso = 4096
        while True:
            moso = fichye.stream.read(gwose_moso)
            if len(moso) == 0:
                return non_fichye
            fichye_local.write(moso)
