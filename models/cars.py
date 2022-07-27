from config.db import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String


cars = Table(
    'cars', meta,
    Column('registration_no', String(17)),
    Column('car_name', String(255)),
    Column('model', String(255)),
    Column('price_in_lakh', Integer),
)



