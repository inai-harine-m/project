from fastapi import FastAPI
from schemas.car import car
from config.db import con
from models.cars import cars
app = FastAPI()
@app.get('/details')
async def message():
   data=con.execute(cars.select()).fetchall()
   return {
      # "success": True,
       "data": data
   }
#data insertion
@app.post('/details')
async def store(car:car):
    data=con.execute(cars.insert().values(
        id = car.id,
        car_name=car.car_name,
        model=car.model,
        price_in_lakh = car.price_in_lakh,
    ))

    if data.is_insert:
        return {
            "success": True,
            "msg":"car details successfull"
        }
    else:
        return{
            "success": False,
            "msg": "problem"
        }


#data updation

@app.put('/api/details/{id}')
async def update(id:int,car:car):
    data=con.execute(cars.update().values(
        id=car.id,
        car_name=car.car_name,
        model=car.model,
        price_in_lakh=car.price_in_lakh,
    ).where(cars.c.id==id))
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

@app.delete('/details/{id}')
async def delete(id:int):
    data=con.execute(cars.delete().where(cars.c.id==id))
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