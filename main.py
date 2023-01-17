from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

PI = 3.14

# home route
@app.route('/')
def index():
    return '<h1 style="text-align: center; color: royalblue"> Area And Perimeter API<h1/>'

# area of circle route
@app.route('/api/calc/area/circle/')
def calc_Area_Of_Circle():
    radius = int(request.args.get('radius'))
    area = (PI * (radius * radius))
    response =  {"radius": radius, "area": area }
    return jsonify(response)

# area of rectangle route
@app.route('/api/calc/area/rectangle/')
def calc_Area_Of_Rectangle():
    width = int(request.args.get('width'))
    height = int(request.args.get('height'))
    area = width * height
    response = {"width": width, "height": height, "area": area}
    return jsonify(response)

# area of triangle route
@app.route('/api/calc/area/triangle/')
def calc_Area_Of_Triangle():
    base = int(request.args.get('base'))
    height = int(request.args.get('height'))
    area = 1/2 *base * height
    response = {"base": base, "height": height, "area": area}
    return jsonify(response)

#perimeter of rectangle route
@app.route('/api/calc/perimeter/rectangle/')
def calc_Perimeter_Of_Rectangle():
    width = int(request.args.get('width'))
    height = int(request.args.get('height'))
    perimeter = (2*height) + (2*width)
    response = {"width": width, "height": height, "perimeter": perimeter}
    return jsonify(response)

#perimeter of triangle route

@app.route('/api/calc/perimeter/triangle/')
def  calc_Perimeter_Of_Triangle():
    side1 = int(request.args.get('side1'))
    side2 = int(request.args.get('side2'))
    side3 = int(request.args.get('side3'))
    perimeter = side1 + side2 + side3
    response = {"side1": side1, "side2": side2, "side3": side3, "perimeter": perimeter}
    return jsonify(response)


#circumference of circle route 

@app.route('/api/calc/circumference/circle/')
def  calc_Circumference_Of_Circle():
    #Given only radius
    if request.args.get('radius'):
        radius = int(request.args.get('radius'))
        circumference =  2 * PI * radius
        response = {"radius": radius, "circumference": circumference}

    #Given only diameter
    elif request.args.get('diameter'):
        diameter = int(request.args.get('diameter'))
        circumference =  PI * diameter
        response = {"diameter": diameter, "circumference": circumference}

    return jsonify(response)


app.run(host='0.0.0.0', port=81)