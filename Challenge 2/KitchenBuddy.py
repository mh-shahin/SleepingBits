from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from pyngrok import ngrok

app = Flask(name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ingredients.db'
db = SQLAlchemy(app)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    quantity = db.Column(db.Float)
    unit = db.Column(db.String(20))

@app.route('/')
def home():
    return "Welcome to Mofa's Kitchen Buddy!"

@app.route('/ingredients', methods=['POST'])
def add_ingredient():
    data = request.get_json()
    new_ingredient = Ingredient(name=data['name'], quantity=data['quantity'], unit=data['unit'])
    db.session.add(new_ingredient)
    db.session.commit()
    return jsonify({"message": "Ingredient added successfully"})

@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    ingredients = Ingredient.query.all()
    return jsonify([{"id": ing.id, "name": ing.name, "quantity": ing.quantity, "unit": ing.unit} for ing in ingredients])

@app.route('/ingredients/<int:id>', methods=['PUT'])
def update_ingredient(id):
    data = request.get_json()
    ingredient = Ingredient.query.get(id)
    if ingredient:
        ingredient.quantity = data['quantity']
        ingredient.unit = data['unit']
        db.session.commit()
        return jsonify({"message": "Ingredient updated successfully"})
    return jsonify({"message": "Ingredient not found"}), 404

# Creating the database within the application context
with app.app_context():
    db.create_all()

# Set up ngrok to expose the Flask app
ngrok.kill()
public_url = ngrok.connect(5000)
print(f"Public URL: {public_url}")

# Run the Flask app
app.run()