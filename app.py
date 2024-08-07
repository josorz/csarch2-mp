from flask import Flask, render_template, request
from lib import Calculator

app = Flask(__name__)
calculator = Calculator()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        ## Get form data
        op1 = request.form['input-1-operand']
        b1 = request.form['input-1-base']
        op2 = request.form['input-2-operand']
        b2 = request.form['input-2-base']
        rounding = request.form['round']
        digits = request.form['supported-digits']

        op1 = str(op1)
        b1 = int(b1)
        op2 = str(op2)
        b2 = int(b2)
        digits = int(digits)

        ## Process
        solution = calculator.solve(op1, b1, op2, b2, rounding, digits)
        inputs = {'op1': op1, 
        'b1': b1, 
        'op2': op2, 
        'b2': b2, 
        'rounding': rounding, 
        'digits': digits}
        

        ## Output to user
        ## Once
        return render_template('solution.html', solution=solution, inputs=inputs)