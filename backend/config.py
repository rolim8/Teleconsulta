import os


class Config:
    # Configuração do banco de dados (PostgreSQL)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 'postgresql://usuario:senha@localhost:5432/teleconsulta')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
