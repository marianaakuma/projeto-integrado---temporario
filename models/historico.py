from utils import db

class historico(db.Model): 
    __tablename__ = "historico"
    
    id = db.Column(db.Integer, primary_key=True)  # Adicionando um ID único para cada registro
    titulo = db.Column(db.String(100))
    Data = db.Column(db.String(100))
    Hora = db.Column(db.String(100))
  
    def __init__(self, titulo, Data, Hora):
        self.titulo = titulo  # Corrigido para usar o nome correto da variável
        self.Data = Data 
        self.Hora = Hora
        
    def __repr__(self):
        return "<Historico(titulo='{}', Data='{}', Hora='{}')>".format(self.titulo, self.Data, self.Hora)