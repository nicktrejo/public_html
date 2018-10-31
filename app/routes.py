from app import app
from flask import Flask, render_template, request, url_for, redirect, session
from random import randint
from hashlib import md5
import json
import os
import sys

user=None

catalogue_data = open(os.path.join(app.root_path,'catalogue/catalogue.json'), "r").read()
catalogue = json.loads(catalogue_data)

#TODO: cambiar esto a lo correcto (es de prueba)
history_data = open('/home/nicolas/public_html/app/catalogue/historial_ejemplo.json', "r").read()
history = json.loads(history_data)

# Lista de los generos ordenados alfabeticamente y sin repetir
# Se usa la lista auxiliar que luego se elimina
generos_aux=[]
for item in catalogue["peliculas"]:
    generos_aux.append(item["genero"])
generos=list(set(generos_aux))
generos.sort()
del generos_aux

# Se hace una lista que corresponde a las peliculas de cada genero
generos_index=[]
for i, genero in enumerate(generos, 0):
    generos_index.append([])
    for j, pelicula in enumerate(catalogue["peliculas"], 0):
        if genero == pelicula["genero"]:
            generos_index[i].append(j)

#Dado la siga de la pelicula, quiero el indice correspondiente o -1 si no existe
def indice_pelicula(catalogue=[], sigla=""):
    for i, pelicula in enumerate(catalogue["peliculas"], 0):
        if sigla == pelicula["sigla"]:
            return i
    return -1

#Dado un string de busqueda, quiero un array con los indices correspondiente o array vacio si no existe
def indices_busqueda(catalogue=[], q=""):
    q_index = []
    for i, pelicula in enumerate(catalogue["peliculas"], 0):
        if q == pelicula["titulo"]:
            q_index.append(i)
    return q_index

#Encriptacion contrasena en md5 y
def check_password(path,contrasena):
    user_data = open(path, "r").read()
    user_data = json.loads(user_data)
    m = md5()
    m.update(contrasena)
    contrasena = m.hexdigest()
    if(user_data["contrasena"] == contrasena):
        session["user"] = user_data["user"]
        session["nombre"] = user_data["nombre"]
        session["apellido"] = user_data["apellido"]
        session["tarjeta"] = user_data["tarjeta"]
        session["correo"] = user_data["correo"]
        session["saldo"] = user_data["saldo"]
        # Prueba de carrito simulado, quitar las siguientes (5) lineas
        session["carrito"] = [2]
        session["carrito"] = [2]
        auxil = session["carrito"]
        auxil.append(3)
        session["carrito"] = auxil
        return True
    return False

def createuserlogin(user, contrasena, nombre, apellido, correo, tarjeta, path):
    m = md5()
    m.update(contrasena)
    contrasena = m.hexdigest()
    os.mkdir(path)
    dic={"contrasena": contrasena, "user": user, "correo": correo, "nombre": nombre, "apellido": apellido, "tarjeta": tarjeta, "saldo": randint(0,100)}
    open(path+"datos.dat", "w").write(json.dumps(dic))
    session["user"] = dic["user"]
    session["correo"] = dic["correo"]
    session["nombre"] = dic["nombre"]
    session["apellido"] = dic["apellido"]
    session["tarjeta"] = dic["tarjeta"]
    session["saldo"] = dic["saldo"]

@app.before_request
def before_request():
    global user
    if "user" in session:
        user = session["user"]
    else:
        user = None

@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    if "q" in request.args:
        q_index = indices_busqueda(catalogue, request.args["q"])
        return str(q_index)
    return render_template('index.html', user=user, catalogue=catalogue, generos=generos)


@app.route('/carrito')
def carrito():
    return render_template('carrito.html', title = "Carrito", user=user, generos=generos)


@app.route('/historial')
def historial():
    # busca cuales son los indices de peliculas para las compras realizadas
    # las peliculas que no encuentra, las ignora; y muestra las duplicadas
    index_historial=[]
    for compra in history["compras"]:
        index_historial.append(indice_pelicula(catalogue,compra["sigla"]))
    return render_template('historial.html', title = "Historial", user=user, generos=generos, catalogue=catalogue, index_historial=index_historial)


@app.route('/login/')
def login():
    if "user" in session:
        return index()
    else:
        user = None
    return render_template('login.html', title = "Log In", user=user, generos=generos)

@app.route('/login/activate/', methods=['POST'])
def login_activate():
    if "user" in session:
        return index()
    user= request.form['user']
    contrasena=request.form['contrasena']
    path = os.path.dirname(__file__)+"/usuarios/"+user+"/datos.dat"
    if(os.path.exists(path)):
        if(check_password(path,contrasena)):
            before_request()
            return index()
    return render_template("login.html", wrong=True)

@app.route('/logout/')
def logout():
    session.clear()
#    session.pop("user",None)
    before_request()
    return index()


@app.route('/signin/')
def signin():
    if "user" in session:
        return index()
    return render_template('signin.html', title = "Sign In", generos=generos)


@app.route('/signin/activate/', methods=['GET', 'POST'])
def signin_activate():
    if "user" in request.form:
        user=request.form['user']
        contrasena=request.form['contrasena']
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        correo=request.form['correo']
        tarjeta=request.form['tarjeta']
        path = os.path.dirname(__file__)+ "/usuarios/"+user+"/"
        if(os.path.exists(path)):
            return render_template("signin.html", error=True, generos=generos)
        createuserlogin(user, contrasena, nombre, apellido, correo, tarjeta, path)
        before_request()
        return index()

# TODO: que se pueda agregar la peli al carrito
@app.route('/peli/<movie>', methods=['GET', 'POST'])
def peli(movie):
    if "user" in session:
        user = session["user"]
    else:
        user = None
    pelicula = movie
    pelicula_num = -1
    for i, item in enumerate(catalogue["peliculas"], 0):
        if item["sigla"] == pelicula:
            pelicula_num = i
    if pelicula_num == -1:
        return "Pelicula no encontrada"
    else:
        return render_template('pelicula.html', pelicula=catalogue["peliculas"][pelicula_num], generos=generos, user=user,)

# TODO: sacar esto que es de prueba
@app.route('/session')
def session_test():
    if "carrito" in session:
        return str(session["carrito"])
    return "sin carrito"
# print(session["user"], session["nombre"], session["apellido"], session["tarjeta"], session["correo"], session["saldo"], session["carrito"])

@app.route('/categoria/<category>')
def categoria(category):
    # Se buscan los indices de las peliculas para la categoria o sino no existe la categoria
    indices=[]
    try:
        indices = generos_index[generos.index(category)]
    except:
        print >>sys.stderr, "Se ha pedido una categoria invalida"
        return "Categoria no existe"
#    return str(indices)
#    index_categoria=[]
#    categoria = category
#    for i, pelicula in enumerate(catalogue["peliculas"], 0):
#        if pelicula["genero"] == categoria:
#            index_categoria.append(i)
    return render_template('categorias.html', catalogue=catalogue, indices=indices, generos=generos, genero=category, user=user,)
    return str(index_categoria)
    # LO DE ABAJO SE PUEDE QUITAR TAL VEZ
    index_historial=[]
    for compra in history["compras"]:
        index_historial.append(indice_pelicula(catalogue,compra["sigla"]))
    pelicula = movie
    pelicula_num = -1
    for i, item in enumerate(catalogue["peliculas"], 0):
        if item["sigla"] == pelicula:
            pelicula_num = i
    if pelicula_num == -1:
        return "Pelicula no encontrada"
    else:
        return render_template('categoria.html', pelicula=catalogue["peliculas"][pelicula_num], generos=category, user=user,)
