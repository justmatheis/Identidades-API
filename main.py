#import distutils.log import debug
from flask import Flask
from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route("/sumasen/<string:a>/<string:b>")
def get_suma_sen(a, b):
    a = float(a)
    b = float(b)
    
    result = (2 * math.sin((a + b)/2)) * (math.cos((a - b)/2))
    
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

@app.route("/razoncos/<string:a>")
def get_razones(a):
    a = float(a)

    senC = 1 - math.pow(a, 2)
    sen = - math.sqrt(senC)
    tan = sen / a
    cot = 1 / tan
    sec = 1 / a
    csc = 1 / sen

    return jsonify({"sen": sen, "tan": tan, "cot": cot, "sec": sec, "csc": csc})

@app.route("/triangulorect/<string:a>/<string:b>")
def get_triangulo_rect(a, b, c):
    a = float(a)
    b = float(b)
    ang_a = 90.0
    c = math.sqrt(math.pow(a,2) + math.pow(b,2)) 
    
    ang_t = math.degrees(math.atan(b/a))
    ang_b = math.degrees(math.atan(a/b))
    
    return jsonify({"c": c, "alpha": ang_a, "beta": ang_b, "theta": ang_t})

@app.route("/triangulobl/<string:a>/<string:b>/<string:c>")
def get_triangulo_obl(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    
    ang_a = math.degrees(math.acos((math.pow(a,2) - math.pow(b,2) - math.pow(c,2))/(-2 * b * c)))
    ang_b = math.degrees(math.acos((math.pow(b,2) - math.pow(a,2) - math.pow(c,2))/(-2 * a * c)))
    ang_t = math.degrees(math.acos((math.pow(c,2) - math.pow(a,2) - math.pow(b,2))/(-2 * a * b)))
    
    return jsonify({"alpha": ang_a, "beta": ang_b, "theta": ang_t})

if __name__ == '__main__':
    app.run(debug = True, port=4000)
