from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])

def hello_jonas():
 return "Jonas"

if __name__ == '__main__':
 app.run(debug=True)