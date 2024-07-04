from app import app, db
from flask import render_template, url_for, redirect
from app.forms import CadastroForm, ItensForm, User2Form
from app.models import User2

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


@app.route('/Cadastro/', methods = ['GET', 'POST'])
def CadastroPage():
    form = CadastroForm()
    if form.validate_on_submit():
        form.save()  #talvez coloca USER
        print("Acho que deu")
        return redirect(url_for('IndexPage'))
    
    return render_template('cadastro.html', form = form)

#-- Para Testes 

@app.route('/')
def IndexPage():
    #Login Required para adm talvez


    return render_template('index.html')

@app.route('/adm/', methods = ['GET', 'POST'])
def CadProdPage():
    #if login epsecial == True permitir entrada
    form = ItensForm()
    if form.validate_on_submit():
        form.SalvaItens()
        return redirect(url_for('IndexPage'))

    return render_template('cadproduto.html', form=form)
