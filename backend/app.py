from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models.task import db
from routes.task_routes import task_bp
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Configurar la migración de base de datos
migrate = Migrate(app, db)

# Configurar la URI de la base de datos utilizando variables de entorno
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Habilitar CORS en la aplicación Flask
CORS(app)

# Inicializar la base de datos con la aplicación Flask
db.init_app(app)

# Registrar el blueprint de las rutas de tareas
app.register_blueprint(task_bp)

if __name__ == '__main__':
    # Crear todas las tablas si no existen y ejecutar la aplicación
    with app.app_context():
        db.create_all()
    app.run(debug=True)
