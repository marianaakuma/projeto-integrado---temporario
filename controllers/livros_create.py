from flask import Blueprint, render_template, request, redirect, url_for, flash,re
from utils import db,lm
from models.livros_create import livros_create
from flask import Blueprint

bp_livros_create = Blueprint("livros_create", __name__, template_folder='templates')

@bp_ livros_create.route('/create', methods=['GET', 'POST'])
@livros_create_required
def create():
    if request.method == 'GET':
        return render_template('livros_create.html')  # Ajuste no nome do template

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        ano = request.form.get('ano')
        curso = request.form.get('curso')
        link = request.form.get('link')

        novo_livro = Livro(titulo, ano, curso, link)
        db.session.add(novo_livro)
        db.session.commit()

        return redirect(url_for('livros.biblioteca')) 

@bp_livros_create.route('/biblioteca')
@login_required
def biblioteca():
    livros = Livro.query.all()
    return render_template('biblioteca.html', livros=livros)


@bp_livros_create.route('/autenticar', methods=['POST'])
def autenticar():
    admin = request.form.get("admin")
    senha = request.form.get("senha")
    
    if usuario != 'admin' or senha != 'senha123':
        if (usuario == 'admin'):
            flash('O login está correto. ', "warning")
        else:
            flash('O login está incorreto. ', "danger")
        
        if (senha == 'senha123'):
            flash('A senha está correta. ', "warning")
        else:
            flash('A senha está incorreta. ', "danger")
       
        return redirect("/livros_create")
    else:
        return "Os dados recebidos foram: usuario = {} e senha = {}".format(usuario, senha)