import logging
import os

from flask import Flask, request, make_response
from flask_restplus import Resource, Api
from flask_cors import CORS
from werkzeug.datastructures import FileStorage
from werkzeug.exceptions import BadRequest

from db.config import configure_mongo, MONGO_DB

from db.kliyan import anrejistre_metadata
from stokaj_fichye.nextcloud.kliyan import stoke_fichye_a
from travay_fichye import kreye_metadata_fichye, anrejistre_fichye_sou_disk

app = Flask('voxforge-kreyol')
api = Api(app)
cors = CORS(app, resources={r'/api/*': {'origins': 'https://voxforge-kreyol.nucklehead.vercel.app'}})

configure_mongo(app)

logger = logging.getLogger('werkzeug')

upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)


@api.route('/api/telechaje')
@api.expect(upload_parser)
class Telechaje(Resource):
    def post(self):
        if 'file' not in request.files:
            raise BadRequest('Kot fichye w ap voye a, tonton?')
        fichye = request.files['file']
        non_fichye = anrejistre_fichye_sou_disk(fichye)
        metadata = kreye_metadata_fichye(non_fichye)
        id_metadata = anrejistre_metadata(metadata)
        stoke_fichye_a(app, f'{id_metadata}.zip', non_fichye)
        response = make_response('submission uploaded successfully.')
        response.headers['content-type'] = 'text/plain'
        return response


@api.route('/api/anrejistreman')
class Anrejistreman(Resource):
    def get(self):
        return list(MONGO_DB.db.metadata_anrejistreman.find({}, {'_id': False}))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", default=8080))
    app.run(host='0.0.0.0', port=port)
