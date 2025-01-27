from flask import Flask

app: Flask = Flask(__name__)

@app.route('/')
def home_page():
    return 'Hello world!'

@app.route('/papers')
def papers_page():
    return 'Here are my papers!'

@app.route('/patents')
def patents_page():
    return 'Here are my patents!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)    
