import distutils.log import debug
from flask import Flask
from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route("/aproxsen/<string:x>")
def get_datos_aprox(x):
    x = float(x)
    multiplier = 1
    result = 0
    
    for i in range(1,20,2):
        result += multiplier*pow(x,i)/math.factorial(i)
        multiplier *= -1
    
    return jsonify({"seno": result})

@app.route("/sumaseries/<string:x>/<string:n>")
def get_suma_series(x, n):
    x = int(x)
    n = int(n)
    result = 0
    sine = 0

    for i in range(n):
        sign = (-1)**i
        pi = 22/7
        y = x*(pi/180)
        sine += ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    
    result = round(sine,2)

    return jsonify({"sumas": result})

@app.route("/heron/<string:a>/<string:b>/<string:c>")
def get_formula_heron(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)

    s = (a+b+c)/2

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    return jsonify({"area": area})

if __name__ == '__main__':
    app.run(debug = True, port=4000)
