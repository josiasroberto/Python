import os
from flask import Flask, jsonify, request
from models.user import User
from database import db
from flask_login import LoginManager, login_required, login_user, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance/database.db')

# print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
#view login
login_manager.login_view = 'login'
#Session <- conexão ativa

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        # Login
        user = User.query.filter_by(username=username).first()
                
        if user and user.password == password:
            login_user(user)  # Inicia a sessão
            print(current_user.is_authenticated)
            return jsonify({"message": "Login realizado com sucesso!"})
    
    return jsonify({"message": "Credenciais inválidas"}), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso!"})

@app.route('/user', methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user_already_exists = User.query.filter_by(username=username).first()
        if user_already_exists:
            return jsonify({"message": "Username já existe"}), 400
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuario cadastrado com sucesso"})

    return jsonify({"message": "Dados invalidos"}), 400


@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)