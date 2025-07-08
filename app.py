import os
from dotenv import load_dotenv

from database import db
from flask import Flask,jsonify, request
from datetime import datetime

from models.diet import Diet

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = "jonas_secreto"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db.init_app(app)

@app.route("/", methods=['GET'])
def hello_jonas():
 return "Jonas"

@app.route('/register-diet', methods=['POST'])
def register_diet():
  data = request.json
  name = data.get("name")
  description = data.get("description")
  within_diet = data.get("within_diet") or False
  date_time = data.get("date_time") or datetime.now()

  if name and description:
    diet = Diet(
      name=name,
      description=description, 
      date_time=date_time,
      within_diet=within_diet
    )
    db.session.add(diet)
    db.session.commit()

    return jsonify({"message": f"{name} added susccessfully"})
  
  return jsonify({"message": "Invalid credentials"}), 400

if __name__ == '__main__':
 app.run(debug=True)