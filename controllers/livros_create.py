from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils import db,lm
from models.livros_create import livros_create
from flask import Blueprint

bp_livros_create = Blueprint("livros_create", __name__, template_folder='templates')

@bp_livros_create.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('livros_create.html')

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        ano = request.form.get('ano')
        curso = request.form.get('curso')
        Link = request.form.get('Link')

        # Criar um novo livro
        novo_livro = Livro(titulo=titulo, ano=ano, curso=curso, Link=Link)
        db.session.add(livros_create)
        db.session.commit()

        flash("Livro cadastrado com sucesso!")
        return redirect(url_for('biblioteca.html'))


@bp_livros_create.route('/autenticar', methods=['GET','POST'])
def autenticar():
    if request.method == 'GET':
            return render_template('livros_create.html')
    
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        ano = request.form.get('ano')
        curso = request.form.get('curso')
        Link = request.form.get('link')
        livros_create = livros_creat.query.filter_by(titulo = titulo).first()

        if (senha is not None and check_password_hash(usuario.senha, senha)):
            login_user(usuario)
            return render_template('biblioteca.html')
        else:
            flash('Dados incorretos')
            return redirect('/')