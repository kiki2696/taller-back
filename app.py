from flask import Flask, render_template, request, redirect, url_for
from modelos import db, Alumna

# Instancia de la clase flask
app = Flask(__name__)

# Configuramos la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos nuestra base de datos
db.init_app(app)


### RUTAS ###
# Ruta Read - leer
@app.route('/')
def index():

    # Obtener todas las alumnas de la db
    alumnas = Alumna.query.all()

    return render_template('index.html', alumnas=alumnas )


# Ruta Create - Crear
@app.route('/crear', methods=['POST'])
def crear():
    if request.method =='POST':

        # Obtener los datos de mi formulario
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        edad = request.form.get('edad')
        colegio = request.form.get('colegio')

        # Creamos el objeto de tipo alumno
        alumna = Alumna(nombre=nombre, apellido=apellido, edad=edad, colegio=colegio)

        # Agregamos el objeto a la db
        db.session.add(alumna)

        # Guardamos los cambios
        db.session.commit()

        return redirect(url_for('index'))
    
# Ruta Delete - Eliminar
@app.route('/eliminar/<id>')
def eliminar(id):

    # Obtenemos la alumna a eliminar
    alumnna = Alumna.query.get(id)

    # Eliminamos la alumna seleccionada
    db.session.delete(alumnna)

    # Guardamos los cambios 
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):

    # Obtenemos la alumna a modificar
    alumna = Alumna.query.get(id)

    if request.method == 'POST':

        # Obtenemos los datos del formulario 
        alumna.nombre = request.form.get('nombre') 
        alumna.apellido = request.form.get('apellido')
        alumna.edad = request.form.get('edad') 
        alumna.colegio = request.form.get('colegio') 

        # Guardar los cambios
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('editar.html', alumna=alumna)
    
















### BREAKPOINT ###
if __name__ == '__main__':
    app.run(debug=True)

