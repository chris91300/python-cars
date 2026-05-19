from service.DatabaseService import databaseService

class CarService:

    def  __init__(self, DatabaseService):
      self.databaseService = DatabaseService
  

    def findAll(self):
        connection = self.databaseService.get_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM car ORDER BY car_id')
        cars = cursor.fetchall()

        cursor.close()
        connection.close()
        return cars
    
    def findAllBrand(self):
        connection = self.databaseService.get_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT brand FROM car GROUP BY brand ORDER BY brand')
        cars = cursor.fetchall()

        cursor.close()
        connection.close()
        return cars
    

    def findById(self, id):
        connection = self.databaseService.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM car WHERE car_id=%s', (id,))
        car = cursor.fetchall()
        car = [dict(row) for row in car]
        cursor.close()
        connection.close()
        return car[0]
    
    def findByBrand(self, brand):
        connection = self.databaseService.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM car WHERE brand=%s', (brand,))
        cars = cursor.fetchall()
        cursor.close()
        connection.close()
        return cars
    

    def save(self, brand, model):
        connection = self.databaseService.get_connection()
        cursor = connection.cursor()

        cursor.execute('INSERT INTO car (brand, model) VALUES(%s, %s) RETURNING *', (brand, model) )
        car = cursor.fetchall()

        connection.commit()
        cursor.close()
        connection.close()
        return car
    

    def update(self, id, brand, model):
        connection = self.databaseService.get_connection()
        cursor = connection.cursor()
        
        cursor.execute('UPDATE car SET brand=%s, model=%s WHERE car_id=%s RETURNING *', (brand, model, id) )
        car = cursor.fetchone()

        connection.commit()
        cursor.close()
        connection.close()
        return car
    

    def deleteById(self, id):
        connection = self.databaseService.get_connection()
        cursor = connection.cursor()

        cursor.execute('DELETE FROM car WHERE car_id = %s RETURNING *', (id,))
        carDeleted = cursor.fetchone()

        connection.commit()
        cursor.close()
        connection.close()
        return carDeleted
    



car_service = CarService(databaseService)