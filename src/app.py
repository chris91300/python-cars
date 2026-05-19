from flask import Flask, jsonify, request, render_template, url_for
from dotenv import load_dotenv
from service.CarService import car_service
from db_mocked.cars import carsMocked


load_dotenv()

app = Flask(__name__)

#   AFFICHER LA PAGE D'ACCUEIL
@app.route('/')
def index():
    url_for('static', filename='style.css')
    brandList = car_service.findAllBrand()
    return render_template('home.html', brandList=brandList)


#   AFFICHER LA PAGE LISTANT TOUTES LES VOITURES
@app.route('/cars', methods=['GET'])
def get_car_list():
    
    cars = car_service.findAll()
    print(cars)
    return render_template('cars.html', cars=cars)


#   AFFICHER LA PAGE CONTENANT LES INFORMATIONS D'UNE VOITURE EN FONCTION DE SON ID
@app.route('/cars/<int:id>', methods=['GET'])
def get_car(id):
    car = car_service.findById(id)
    if car:
        return render_template('car.html', car=car)
    else:
        return render_template('404.html')
    

#   AFFICHER LA PAGE POUR VOIR LES VOITURES EN FONCTION DE LA MARQUE
@app.route('/cars/brand/<string:brand>', methods=['GET'])
def get_car_by_brand(brand):
    cars = car_service.findByBrand(brand)
    
    return render_template('brandList.html', brand=brand, cars=cars)
    


#   AFFICHER LA PAGE POUR AJOUTER UNE VOITURE
@app.route("/cars/add", methods=['GET'])
def add_car():
    return render_template('addCar.html')


#   AJOUTER UNE VOITURE DANS LA BASE DE DONNEES
@app.route('/cars', methods=['POST'])
def create_car():
   
    brand = request.form["brand"]
    model = request.form["model"]
    if brand == "" and model == "":
        return render_template('addCar.html', saved="false", error="true", errorMessage="données invalides.")
    
    else:
        carSaved = car_service.save(brand, model)
        print(carSaved)
        if carSaved:
            return render_template('addCar.html', saved="true")
        else:
            return render_template('addCar.html', saved="false", error="true", errorMessage="voiture non créée.")
    

#   AFFICHER LA PAGE POUR MODIFIER UNE VOITURE
@app.route('/cars/update/<int:id>', methods=['GET'])
def get_update_page(id):
    car = car_service.findById(id)
    if car:        
        return render_template('updateCar.html', car=car)
    
    else:
        return render_template('404.html')


#   MODIFIER UNE VOITURE
@app.route('/cars/update', methods=['PUT'])
def update_car():
    id = request.json["id"]
    brand = request.json["brand"]
    model = request.json["model"]
    
    carUpdated = car_service.update(id, brand, model)
    if carUpdated:
        return jsonify({"success": "true"})
    else:
        return jsonify({"succes": "false", "message": "voiture non modifiée"})
    


#   SUPPRIMER UNE VOITURE
@app.route('/cars/delete', methods=['DELETE'])
def delete_car():
    print("on delete")
    id = request.json["id"]
    car = car_service.findById(id)
    if car:                 
        car_service.deleteById(id)
        return jsonify({"success": "true"})
    else:
        return jsonify({"succes": "false", "message": "voiture non supprimée"})
    
   
    
    