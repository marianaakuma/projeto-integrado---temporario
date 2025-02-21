from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils import db,lm
from models.livros_create import livros_create
from flask import Blueprint
from flask_login import login_required

bp_livros_create = Blueprint("livros_create", __name__, template_folder='templates')


@login_required
@bp_livros_create.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('livros_create.html')  # Ajuste no nome do template

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        print(titulo)
        ano = request.form.get('ano')
        curso = request.form.get('curso')
        link = request.form.get('link')
        materia = request.form.get('materia')


        novo_livro =livros_create(titulo, ano, curso, link, materia)
        db.session.add(novo_livro)
        db.session.commit()

        return redirect(url_for('livros_create.recovery')) 

@bp_livros_create.route('/recovery')
def recovery():
    if request.method == 'GET':
        livros= livros_create.query.all()
        print(livros)
        return render_template("biblioteca.html",livros = livros)