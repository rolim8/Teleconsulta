from app import db

# Modelo de Paciente (pode ser movido para um arquivo separado)


class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    historico_medico = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Paciente {self.nome}>'
