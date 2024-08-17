from flask_sqlalchemy import SQLAlchemy

# Inicializar la instancia de SQLAlchemy
db = SQLAlchemy()

class Task(db.Model):
    """
    Modelo de base de datos para representar una tarea.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """
        Representación en cadena del objeto Task.
        """
        return f"<Task {self.title}>"
