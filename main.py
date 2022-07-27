from fastapi import FastAPI
from schemas.car import car
from config.db import con
from models.cars import cars
app = FastAPI()
@app.get('/api/cars')
async def message():
   data=con.execute(cars.select()).fetchall()
   return {
      # "success": True,
       "data": data
   }
#data insertion
@app.post('/api/cars')
async def store(car:car):
    data1 = con.execute(cars.select().where(cars.c.registration_no==car.registration_no)).fetchall()
    if(len(data1)==0):                                   #if already exist registration_no is not inserted
        data = con.execute(cars.insert().values(
            registration_no=car.registration_no,
            car_name=car.car_name,
            model=car.model,
            price_in_lakh=car.price_in_lakh,
        ))
        if data.is_insert:
            return {
                         "success": True,
                         "msg": "car details successfull"
                   }
        else:
            return {
                      "success": False,
                      "msg": "problem"
                   }
    else:
        return "registration_no already exists"






#data updation

@app.put('/api/cars/{car_name}')
async def update(registration_no:str, car:car):
    data=con.execute(cars.update().values(
        registration_no=car.registration_no,
        car_name=car.car_name,
        model=car.model,
        price_in_lakh=car.price_in_lakh,
    ).where(cars.c.registration_no==registration_no))
    if data:
        return {
            "success": True,
            "msg":"car details updated  successfull"
        }
    else:
        return{
            "success": False,
            "msg": "problem"
        }

#delete

@app.delete('/api/cars/{car_name}')
async def delete(registration_no:str):
    data=con.execute(cars.delete().where(cars.c.registration_no==registration_no))
    if data:
        return {
            "success": True,
            "msg":"car details deleted successfull"
        }
    else:
        return{
            "success": False,
            "msg": "problem"
        }