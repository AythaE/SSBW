# -*- coding: utf-8 -*-

from flask import Flask, Response, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
  usuarios = []
  usuarios.append({'name': 'Pene', 'dni': 123456})
  usuarios.append({'name': 'Pedro', 'dni': 5984})
  return render_template('main.html', var='Perro', usuarios=usuarios)


@app.route('/un_texto_plano')
def texto_plano():
  response = Response()
  response.headers['Content-Type'] = 'text/plain; charset=utf-8'
  response.set_data("Un texto plano cañon")
  return response


@app.route('/este_texto_plano/<text>')
def este_texto_plano(text):
  response = Response()
  response.headers['Content-Type'] = 'text/plain; charset=utf-8'
  response.set_data(text)
  return response


@app.route('/un_texto_html')
def texto_html():
  return 'Un texto <b>HTML</b> cañon'


@app.route('/una_imagen')
def imagen():
  response = Response()
  response.headers['Content-Type'] = 'image/jpg'

  f = open('./static/img/juego-perro-1.jpg', 'rb')
  imagen = f.read()
  response.set_data(imagen)
  return response


@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  # 0.0.0.0 para permitir conexiones
  #         desde cualquier sitio.
  #         Ojo, peligroso en solo
  #         en modo debu
