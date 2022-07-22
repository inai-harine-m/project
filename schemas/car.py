from pydantic import BaseModel


class car(BaseModel):
       id:int
       car_name:str
       model:str
       price_in_lakh:int