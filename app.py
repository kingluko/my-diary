from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def hello_world():
   if request.method == 'GET':
       return 'My Diaries'

if __name__ == '__main__':
   app.run(debug=True)