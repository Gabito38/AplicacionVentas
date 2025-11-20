from flask import Flask, request
from Controllers import Usuario_controller
from Controllers import Cliente_controller
from Controllers import Producto_controller
from Controllers import Venta_controller
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ventas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(Usuario_controller.usuario_bp)
app.register_blueprint(Cliente_controller.cliente_bp)
app.register_blueprint(Producto_controller.producto_bp)
app.register_blueprint(Venta_controller.venta_bp)

@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return (dict(is_active = is_active))

@app.route("/")
def home():
    return "<h1>Aplicacion ventas</h1>"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)