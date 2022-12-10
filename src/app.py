from utils import Tablero
from utils import Player
from custom import ValidationError
from logger import getFullPatch

from flask import Flask
from flask import jsonify, render_template
from flask import request

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

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav'}

def get_from_request(name):
    return request.form.to_dict().get(name, None)

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
    except ValidationError as e:
        logging.error(str(e), traceback.format_exc())

@app.route('/play')
def play():
    return render_template('play.html'), 200

@app.route('/gameMode', methods=['POST'])
def gameMode():
    try:
        print(get_from_request('numOfPlayers'))
        return 'ok'
    except ValidationError as e:
        logging.error(str(e), traceback.format_exc())



if __name__ == '__main__':
    app.debug = True
    app.run(
        host="0.0.0.0",
        port=5000,        
    )



