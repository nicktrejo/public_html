from app import app
from flask import Flask, render_template, request, url_for, redirect, session
import json
import os

catalogue_data = open(os.path.join(app.root_path,'catalogue/catalogue.json'), "r").read()
catalogue = json.loads(catalogue_data)

# Lista de los generos ordenados alfabeticamente y sin repetir
# Se usa la lista auxiliar que luego se elimina
generos_aux=[]
for item in catalogue["peliculas"]:
    generos_aux.append(item["genero"])
generos=list(set(generos_aux))
generos.sort()
del generos_aux

def check_password(path,contrasena):
    user_data = open(path, "r").read()
    user_data = json.loads(user_data)
    m = md5()
    m.update(contrasena)
    contrasena = m.hexdigest()
    if(user_data["contrasena"] == contrasena):
        session["user"] = user_data["user"]
        session["correo"] = user_data["correo"]
        session["saldo"] = user_data["saldo"]
        return True
    return False

def createuserlogin(user, contrasena, correo, tarjeta, path):
    m = md5()
    m.update(contrasena)
    contrasena = m.hexdigest()
    os.mkdir(path)
    dic={"contrasena": contrasena,\
        "user": user,\
        "correo": correo,\
        "nombre": nombre,\
        "apellido": apellido,\
        "tarjeta": tarjeta,\
        "saldo": randint(0,100)}
    open(path+"datos.dat", "w").write(json.dumps(dic))
    session["user"] = dic["user"]
    session["correo"] = dic["correo"]
    session["saldo"] = dic["saldo"]

@app.route('/')
@app.route('/index/', methods=['GET', 'POST'])
def index():
    if "user" in session:
        user=session["user"]
    else:
        user = None
    return render_template('index.html', user=user, catalogue=catalogue, generos=generos)


@app.route('/carrito/')
def carrito():
    if "user" in session:
        user=session["user"]
    else:
        user = None
    return render_template('carrito.html', title = "Carrito", user=user, generos=generos)


@app.route('/historial')
def historial():
   return render_template('historial.html', title = "Historial", user=user, generos=generos)


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
    path = os.path.dirname(__file__)+"/usuarios/"+user+"/datos.dat/"
    if(os.path.exist(path)):
        if(check_password(path,contrasena)):
            return index()
    return render_template("login.html", wrong=True)

@app.route('/logout/')
def logout():
    session.pop("user",None)
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
        correo=request.form['correo']
        tarjeta=request.form['tarjeta']
        path = os.path.dirname(__file__)+ "/usuarios/"+user+"/"
    if(os.path.exists(path)):
        return render_template("signin.html", error=True)
    createuserlogin(user, contrasena, correo, tarjeta, path)
    return index()\

#@app.route("/users/<userc>/")
#def user_info(userc):
#    if "user" in session:
#       user = session["user"]
#        correo = session["correo"]
#        saldo = session["saldo"]
#        if userc != user:
#            return index()
#    else:
#        return index()
#    return render_template("user-info.html",r
#     user=user, correo=correo, saldo=saldo)


@app.route('/peli/<movie>')
def peli(movie):
    pelicula=movie
    pelicula_num=0
    for i, item in enumerate(catalogue["peliculas"], 1):
        if item["sigla"]==pelicula:
            pelicula_num=i
    if not pelicula_num:
        return "Pelicula no encontrada"
    else:
        return render_template('pelicula.html', pelicula=catalogue["peliculas"][pelicula_num-1])
