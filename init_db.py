from flask import Flask
from modelos import db, Alumna

# Instancia de la clase flask
app = Flask('app')

# Configuramos la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# # Crear la base de datos
# with app.app_context():
#     db.create_all()

# Agregamos datos manualmente
with app.app_context():

    # Cargamos los datos de la alumnas
    alumna_1 = Alumna(nombre='Abril', apellido='Torres', edad=22, colegio='Nacional de Luque')
    alumna_2 = Alumna(nombre='Diana', apellido='Delgadillo', edad=26, colegio='CEP')
    

    db.session.add(alumna_1)
    db.session.add(alumna_2)
    db.session.commit()



