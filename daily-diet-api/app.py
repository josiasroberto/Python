import os
from flask import Flask, jsonify, request
from models.meal import Meal
from database import db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'lorem_ipsum'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/daily-diet'

db.init_app(app)

@app.route('/meal', methods=['POST'])
def create_meal():
    data = request.get_json()

    name = data.get("name")
    description = data.get("description")
    datetime = data.get("datetime")
    is_on_the_diet = data.get("is_on_the_diet")

    if name and datetime:
        meal = Meal(name=name, description=description, datetime=datetime, 
                    is_on_the_diet=is_on_the_diet)
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Refeição cadastrada com sucesso!"}), 201
    
    return jsonify({"message": "Dados inválidos!"}), 400


@app.route('/meals', methods=['GET'])
def get_meals():
    meal_list = [meal.to_dict() for meal in Meal.query.all()]

    output = {
        "meals": meal_list,
        "total_meals": len(meal_list)
    }
    return jsonify(output)    

if __name__ == '__main__':
    app.run(debug=True)