from flask import Flask, session

app = Flask(__name__)

DATABASE = 'login_reg_db'

app.secret_key= "yurpppp"

from flask_app.controllers import users