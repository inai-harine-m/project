from config.db import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String


cars = Table(
    'cars', meta,
    Column('id', Integer,primary_key=True),
    Column('car_name', String(255)),
    Column('model', String(255)),
    Column('price_in_lakh', Integer),
)



