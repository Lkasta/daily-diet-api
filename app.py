import os
from dotenv import load_dotenv

from database import db
from flask import Flask

from models.diet import Diet

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = "jonas_secreto"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db.init_app(app)

@app.route("/", methods=['GET'])
def hello_jonas():
 return "Jonas"

if __name__ == '__main__':
 app.run(debug=True)