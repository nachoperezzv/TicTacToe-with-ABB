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


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html'), 200

@app.route('/tutorial', methods=['GET'])
def one_player():
    return render_template('tutorial.html'), 200

@app.route('/configuration', methods=['GET'])
def configuration():
    return render_template('config.html'), 200

@app.route('/play')
def play():
    return render_template('play.html'), 200

@app.route('/gameMode', methods=(['POST']))
def setGameMode():
    try:
        print(request.form.to_dict().get('numOfPlayers'))
    except ValidationError as e:
        logging.error(str(e), traceback.format_exc())


if __name__ == '__main__':
    app.debug = True
    app.run(
        host="0.0.0.0",
        port=5000,        
    )



