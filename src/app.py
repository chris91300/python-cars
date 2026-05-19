from flask import Flask, jsonify, request, render_template, url_for
from dotenv import load_dotenv
from service.CarService import car_service


load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    url_for('static', filename='style.css')
    cars = car_service.findAll()
    return render_template('home.html')

@app.route('/cars', methods=['GET'])
def get_car_list():
    
    cars = car_service.findAll()

    return render_template('cars.html', cars=cars)


@app.route('/cars/<int:id>', methods=['GET'])
def get_car(id):
    car = car_service.findById(id)
    if car:
        return render_template('car.html', car=car)
    else:
        return render_template('404.html')
    

@app.route('/cars/brand/<string:brand>', methods=['GET'])
def get_car_by_brand(brand):
    car = car_service.findByBrand(brand)
    if car:
        return jsonify(car)
    else:
        return 'Voiture non trouvé', 404
    

@app.route("/cars/add", methods=['GET'])
def add_car():
    return render_template('addCar.html')

@app.route('/cars', methods=['POST'])
def create_car():
   
    brand = request.form["brand"]
    model = request.form["model"]
    carSaved = car_service.save(brand, model)
    print(carSaved)
    if carSaved:
        return render_template('addCar.html', saved="true")
    else:
        return render_template('addCar.html', saved="false", error="true", errorMessage="voiture non créée.")
    

@app.route('/cars', methods=['PUT'])
def update_car():
    data = request.get_json()
    brand = data["brand"]
    model = data["model"]
    carSaved = car_service.update(brand, model)
    if carSaved:
        return jsonify(carSaved)
    else:
        return 'Voiture non créé', 400
    

@app.route('/cars', methods=['DELETE'])
def delete_car(id):
    data = request.get_json()
    id = data["id"]
    car_service.deleteById(id)
    
    return 'Voiture supprimée'