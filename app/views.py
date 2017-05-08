from flask import Flask
import datetime
meu_web_app = Flask('meu_web_app')


@meu_web_app.route('/')
def pagina_inicial():
    return 'okur'


@meu_web_app.route('/date')
def date():
    return str(datetime.datetime.now())
