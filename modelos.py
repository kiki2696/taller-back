from flask_sqlalchemy import SQLAlchemy

# Instanciar SQLAlchemy
db = SQLAlchemy()

# Creamos nuestro modelo de db
class Alumna(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    edad = db.Column(db.Integer)
    colegio = db.Column(db.String(20))
    
