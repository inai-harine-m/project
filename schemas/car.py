from pydantic import BaseModel,Field
#from typing import Optional

class car(BaseModel):
       registration_no:str=Field(None,title="registration number",max_length=10)
       car_name:str
       model:str
       price_in_lakh:int=Field(...,gt=0,le=100,description="The price should be greater than zero and less than 100")
