import os
from flask import Flask
app = Flask(__name__)

nombre = os.environ['nombre']

@app.route('/')
def index():
    return f"hola mundo, soy {nombre}...."

if __name__ == '__main__':
  app.run(port=80, debug=False)
 