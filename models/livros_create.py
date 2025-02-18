from utils import db

class livros_create(db.Model):
    __tablename__= "livros_create"
    id = db.Column(db.Integer, primary_key = True)
    Título = db.Column(db.String(100))
    Ano = db.Column(db.String(100))
    curso = db.Column(db.String(100))
    Link = db.Column(db.Boolean)


    def __init__(self, Título, Ano, curso, Link):
        self.Título = Título
        self.Ano = Ano
        self.curso = curso
        self.Link = Link
    
    def __repr__(self):
        return "<livros_create {}>".format(self.id)