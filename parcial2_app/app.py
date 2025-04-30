from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/factorial/<int:num>')
def factorial(num):
    try:
        resultado = math.factorial(num)
        return render_template("factorial.html", numero=num, resultado=resultado)
    except ValueError:
        return "Por favor ingrese un número entero no negativo", 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
