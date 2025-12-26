from flask import Flask, request
from flask import Flask, jsonify, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculator', methods = ['POST'])
def calculator():
    data = request.form
    x = eval(data['x'])
    y = eval(data['y'])
    operation = data['operation']
    if operation == 'addition':
        result = x + y
    
    elif operation == 'multiplication':
        result = x * y

    elif operation == 'substraction':
        result = x - y

    elif operation == 'division':
        result = x / y
    
    return jsonify({"status": "success", "result":result})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)