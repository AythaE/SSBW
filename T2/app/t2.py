# -*- coding: utf-8 -*-

from flask import (Flask, escape, redirect, render_template, request, session,
                   url_for)

app = Flask(__name__)


@app.route('/')
def index():
  if 'username' in session:
    usuario = session['username']
    return render_template('home.html', usuario=usuario)
  return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session['username'] = request.form['username']
    return redirect(url_for('index'))
  return render_template('signin.html')


@app.route('/logout')
def logout():
  if 'username' in session:
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))
  return redirect(url_for('login'))


@app.route('/un_texto_plano')
def texto_plano():
  if 'username' in session:
    texto = "Un texto plano cañon"
    return render_template('text_plain.html', texto=texto)
  return redirect(url_for('login'))


@app.route('/un_texto_html')
def texto_html():
  if 'username' in session:
    texto = 'Un texto <b>HTML</b> cañon'
    return render_template('text_html.html', texto=texto)

  return redirect(url_for('login'))


@app.route('/una_imagen')
def imagen():
  if 'username' in session:
    return render_template('imagen.html')
  return redirect(url_for('login'))


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
  #         en modo debug
