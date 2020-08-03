import io

from flask import Flask

from stokaj_fichye.nextcloud.kliyan import stoke_fichye_a

app = Flask(__name__)
stoke_fichye_a(app, f'test.zip', io.StringIO('asdasd'))