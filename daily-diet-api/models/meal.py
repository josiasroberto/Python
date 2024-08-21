from database import db

class Meal(db.Model):
    # id (int), name (text), description (text), datetime (date), status (boolean)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True, default='')
    datetime = db.Column(db.DateTime, nullable=False)
    is_on_the_diet = db.Column(db.Boolean, nullable=False)
    
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "datetime": self.datetime,
            "is_on_the_diet": self.is_on_the_diet  # True se está na dieta, False caso contrário
        }
