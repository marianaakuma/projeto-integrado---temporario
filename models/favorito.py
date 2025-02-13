from utils import db

class favorito(db.Model): 
    __tablename__ = "favorito"
    
    data = db.Column(db.String(100))
    hora = db.Column(db.String(100))
    nome_livro = db.Column(db.String(100))
   
    def __init__(self, data, hora , nome_livro):
        self.data = data 
        self.hora = hora
        self.nome_livro = nome_livro
      
    def __repr__(self):
        return "<favorito{}>".format(self.data , self.hora , self.nome_livro )