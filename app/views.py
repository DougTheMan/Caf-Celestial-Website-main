from app import app
from flask import render_template, url_for

#-----#-----#-----#-----#-----#-----#

@app.route('/home/')
def HomePage():


    return render_template('home.html')

@app.route('/fidelidade/')
def FidelidadePage():


    return render_template('fidelidade.html')

@app.route('/menu-produtos/')
def MenuPage():


    return render_template('menu.html')

@app.route('/reservas/')
def ReservasPage():


    return render_template('reservas.html')




#-- Logins e Cadastros

@app.route('/Login/')
def LoginPage():

    return render_template('login.html')


@app.route('/Login/Cadastro')
def CadastroPage():

    return render_template('cadastro.html')

#--

@app.route('/')
def IndexPage():
    #Login Required para adm talvez


    return render_template('index.html')
