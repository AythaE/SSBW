# -*- coding: utf-8 -*-

from flask import (Flask, escape, redirect, render_template, request, session,
                   url_for)

app = Flask(__name__)


@app.route('/')
def index():
  if 'username' in session:
    return render_template('home.html')
  return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session['username'] = request.form['username']
    return redirect(url_for('index'))
  return render_template('signin.html')


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


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  # 0.0.0.0 para permitir conexiones
  #         desde cualquier sitio.
  #         Ojo, peligroso en solo
  #         en modo debu
