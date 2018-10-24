from app import app
from flask import render_template, url_for, session
import json
import os
import sys


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


@app.route('/signin')
def signin():
   return render_template('signin.html', title = "SignIn")


@app.route('/login')
def login():
   return render_template('login.html', title = "LogIn")
   

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
