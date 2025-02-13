from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Modelo de Paciente


class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    historico_medico = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Paciente {self.nome}>'

# Rota para cadastrar paciente


@app.route('/pacientes', methods=['POST'])
def cadastrar_paciente():
    data = request.get_json()
    novo_paciente = Paciente(
        nome=data['nome'],
        data_nascimento=data['data_nascimento'],
        historico_medico=data.get('historico_medico', '')
    )
    db.session.add(novo_paciente)
    db.session.commit()
    return jsonify({"mensagem": "Paciente cadastrado com sucesso!"}), 201

# Rota para listar pacientes


@app.route('/pacientes', methods=['GET'])
def listar_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([{
        "id": p.id,
        "nome": p.nome,
        "data_nascimento": p.data_nascimento,
        "historico_medico": p.historico_medico
    } for p in pacientes]), 200


if __name__ == '__main__':
    db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)
