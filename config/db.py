from sqlalchemy import create_engine,MetaData

engine=create_engine('mysql+pymysql://root:harinemaha13@localhost:3306/sys')
meta=MetaData()
con=engine.connect()
