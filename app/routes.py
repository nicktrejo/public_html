from app import app
from flask import render_template, url_for, session
import json
import os
import sys


@app.route('/')
@app.route('/index')
def index():
#     print >>sys.stderr, url_for('static', filename='estilo.css')

# Abre el catalogue.json como solo lectura (r) y lo pasa 
    catalogue_data = open(os.path.join(app.root_path,'catalogue/catalogue.json'), "r").read()
    catalogue = json.loads(catalogue_data)
    return render_template('index.html', title = "Home", catalogue=catalogue)
#-------------------------------------------------------------------------------------, movies=catalogue['peliculas']


#-------------------------------------------------------------------------------------

@app.route('/aladdin')
def aladdin():
   return render_template('aladdin.html', title = "Aladdinn")

@app.route('/carrito')
def carrito():
   return render_template('carrito.html', title = "Carritoo")

@app.route('/dumbo')
def dumbo():
   return render_template('dumbo.html', title = "Dumboo")

@app.route('/harry')
def harry():
   return render_template('harry.html', title = "Harryy")

@app.route('/historial')
def historial():
   return render_template('historial.html', title = "Historial")

@app.route('/peter')
def peter():
   return render_template('peter.html', title = "Peter")

@app.route('/piratas')
def piratas():
   return render_template('piratas.html', title = "Piratas")

@app.route('/signin')
def signin():
   return render_template('signin.html', title = "SignIn")

@app.route('/login')
def login():
   return render_template('login.html', title = "LogIn")
   

# PARA IMPLEMENTAR peli , ver como estan hechos los usuarios aca
# https://github.com/miguelgrinberg/microblog/blob/v0.22/app/main/routes.py
@app.route('/peli/<pelicula>')
def peli(pelicula):
   return render_template('piratas.html', title = "Piratas")

# QUITAR LAS PELIS INDIVIDUALES UNA VEZ QUE FUNCIONE /PELI

@app.route('/harry3')
def harry3():
   return render_template('piratas.html', title = "Piratas")

@app.route('/animales')
def animales():
   return render_template('piratas.html', title = "Piratas")

@app.route('/malefica')
def malefica():
   return render_template('piratas.html', title = "Piratas")

@app.route('/cahrlie')
def charlie():
   return render_template('piratas.html', title = "Piratas")

@app.route('/jumanji')
def jumanji():
   return render_template('piratas.html', title = "Piratas")

@app.route('/antes')
def antes():
   return render_template('piratas.html', title = "Piratas")

@app.route('/cartas')
def cartas():
   return render_template('piratas.html', title = "Piratas")

@app.route('/cabana')
def cabana():
   return render_template('piratas.html', title = "Piratas")

@app.route('/ar')
def aro():
   return render_template('piratas.html', title = "Piratas")
