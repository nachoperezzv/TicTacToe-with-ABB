from utils import Tablero
from utils import Player

from utils import (
    get_from_request,
    set_response
)

from custom import ValidationError
from logger import getFullPatch

from flask import Flask
from flask import render_template

import sys, os, traceback, logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
logging.basicConfig(
    filename=f'{getFullPatch()}/log/logger.log',
    filemode='a',
    level=logging.INFO,
    encoding='utf-8', 
    format='%(asctime)s - %(levelname)s:%(filename)s:%(message)s',
    datefmt='%d/%m/%Y;%H:%M:%S'
)

app = Flask("TicTacToe")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

tablero = Tablero()

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav'}


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html'), 200

@app.route('/tutorial', methods=['GET'])
def one_player():
    return render_template('tutorial.html'), 200

@app.route('/configuration', methods=['GET'])
def configuration():
    return render_template('config.html'), 200

@app.route('/configuration/setABBconfig', methods=['POST'])
def setABBconfig():
    '''
    Se recoge la IP y el PUERTO. En la clase de comunicación se debe asignar la nueva IP y el nuevo puerto
    '''
    try:
        print(get_from_request('ip'), get_from_request('port'))
        return set_response('ok')
    except ValidationError as e:
        logging.error(str(e), traceback.format_exc())
        return set_response(str(e))

@app.route('/play', methods=['GET'])
def play():
    try:
        return render_template('play.html'), 200
    except ValidationError as e:
        logging.error(str(e), traceback.format_exc())

@app.route('/play/GameMode', methods=['POST'])
def setGameMode():
    try:
        tablero.setGameMode(get_from_request('GameMode'))
        return set_response('ok', 200)
    except ValidationError as e:
        logging.error(str(e), traceback.format_exc())

if __name__ == '__main__':
    app.debug = True
    app.run(
        host="0.0.0.0",
        port=5000,        
    )



