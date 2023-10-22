from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    name1 = request.form.get('name1')
    name2 = request.form.get('name2')
    love_percentage = random.randint(1, 100)
    return render_template('result.html', name1=name1, name2=name2, love_percentage=love_percentage)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
