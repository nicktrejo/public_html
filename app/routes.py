from app import app
from flask import render_template, flash, request, url_for, redirect, session, g
import json
import os
import sys
import csv


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
#     print >>sys.stderr, url_for('static', filename='estilo.css')
# Abre el catalogue.json como solo lectura (r) y lo pasa
    catalogue_data = open(os.path.join(app.root_path,'catalogue/catalogue.json'), "r").read()
    catalogue = json.loads(catalogue_data)

    return render_template('index.html', title = "Home", catalogue=catalogue)


@app.route('/carrito')
def carrito():
   return render_template('carrito.html', title = "Carritoo")


@app.route('/historial')
def historial():
   return render_template('historial.html', title = "Historial")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'usuario' in request.form:
        session.pop('usuario', None)
        # aqui se deberia validar con fichero .dat del usuario
        if request.form['usuario'] == 'user'and request.form['contrasena']=='password':
            session['usuario'] = request.form['usuario']
            session['login'] = True
            # se puede usar request.referrer para volver a la pagina desde la que se hizo login
            return redirect(url_for('index'))
        else:
            return render_template('login.html', title = "Log In")
    else:
        # se puede guardar la pagina desde la que se invoca
#       session['url_origen']=request.referrer
        # print a error.log de Apache si se ejecuta bajo mod_wsgi
        print >>sys.stderr, request.referrer
        return render_template('login.html', title = "Log In")

@app.route('/logout')
def logout():
    session['login']= False
    return redirect(url_for('index'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
        if 'username' in request.form:
            nombre=request.form['username']
            savetxt('data.dat',nombre)
            return render_template('login.html', title = "Log In")
        else:
            print >>sys.stderr, request.referrer
            return render_template('signin.html', title = "Sign In")

@app.route('/peli/<movie>')
def peli(movie):
    catalogue_data = open(os.path.join(app.root_path,'catalogue/catalogue.json'), "r").read()
    catalogue = json.loads(catalogue_data)
    pelicula=movie
    pelicula_num=0
    for i, item in enumerate(catalogue["peliculas"], 1):
        if item["sigla"]==pelicula:
            pelicula_num=i
    if not pelicula_num:
        return "Pelicula no encontrada"
    else:
        return render_template('pelicula.html', pelicula=catalogue["peliculas"][pelicula_num-1])
