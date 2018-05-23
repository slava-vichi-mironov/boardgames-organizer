from flask import Flask, jsonify, request
from flask_api import FlaskAPI, status

from resources import board_game, board_game_repository

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
