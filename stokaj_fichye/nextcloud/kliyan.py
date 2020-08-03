import io
import os

from requests import Request, Session
from flask import Flask
from werkzeug.datastructures import FileStorage

LYEN_NEXTCLOUD = os.environ.get('LYEN_NEXTCLOUD', default='https://nextcloud.webo.hosting/remote.php/dav/files')
NON_ITILIZATE_NEXTCLOUD = os.environ.get('NON_ITILIZATE_NEXTCLOUD', default='kourye-e')
MOD_PAS_NEXTCLOUD = os.environ.get('MOD_PAS_NEXTCLOUD', default='mopass')

otorizasyon = (NON_ITILIZATE_NEXTCLOUD, MOD_PAS_NEXTCLOUD)


def stoke_fichye_a(app: Flask, non_fichye: str, non_fichye_local: str):
    sesyon = Session()
    reket_pou_kreye_dosye = Request('MKCOL', f'{LYEN_NEXTCLOUD}/{NON_ITILIZATE_NEXTCLOUD}/{app.name}',
                                    auth=otorizasyon).prepare()
    sesyon.send(reket_pou_kreye_dosye)

    headers = {'Content-type': 'application/octet-stream'}
    with open(non_fichye_local, 'rb') as fichye_local:
        reket_pou_telechaje = Request('PUT', f'{LYEN_NEXTCLOUD}/{NON_ITILIZATE_NEXTCLOUD}/{app.name}/{non_fichye}',
                                      headers=headers,
                                      data=fichye_local,
                                      auth=otorizasyon).prepare()

        repons = sesyon.send(reket_pou_telechaje)
    repons.raise_for_status()
