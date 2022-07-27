# FastApi CRUD with mysql
Here we are going to create REST API to perform CRUD operations using FastAPI with MySQL.

# Introduction 

For building APIs with Python , FastAPI is a modern, high-performance web framework 
Run the live server using Uvicorn and by using the API built , Uvicorn serve requests.
Swagger allows both computers and humans to understand the capabilities of a REST API without direct access to the source code.
Use path parameters to get a unique URL path per item
In the application,JSON message is the same dictionary that is returned from the function . 
Serializing the Python dict into a JSON object is handled by  FastAPI. 
The automatic documentation and serialization is done.
 
# Steps:

1.Create a project folder and navigate to it.

2.create a virtual environment 

      python3 -m venv env

3.Actiavte virtual environment 

In Windows


    env/Scripts/activate


4.For installation 

    pip install pymysql fastapisqlalchemy

5.Create a FastAPI file :

main.py

     from fastapi import FastAPI

     app = FastAPI()

     @app.get("/")

     async def root():

        return {"message": "cars details"}
    
    
It has  a fully functional API application but it won’t run on itself if you call it with python directly.
To run it, you need a server program , Uvicorn. That will be the server.

6.To install uvicorn 


    pip install uvicorn 


7.Run the live server using Uvicorn:

     $ uvicorn main:app --reload

output:

    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

    INFO:     Started reloader process [28720]

    INFO:     Started server process [28722]

    INFO:     Waiting for application startup.

    INFO:     Application startup complete.


The URL shows where your app is being served in your local machine. Since we used --reload for development, when we update your application code,
the server will reload automatically.

 It will then send a JSON response with the following:

     {"message": "cars details"}

# CRUD OPERATION 

1)GET request

Request URL for example:

       http://127.0.0.1:8000/details

Response body


             {
                   "data": [
                      {
                               "registration_no": "AP21BP7331",
                               "car_name": "Maruti",
                               "model": "Maruti Suzuki Baleno",
                               "price_in_lakh": 26
                      },
                     {
                               "registration_no": "AR01O4554",
                               "car_name": "Mahendra",
                               "model": "Mahendra Scorpio",
                               "price_in_lakh": 16
                      },
                     {
                                "registration_no": "TN75AA7106",
                                "car_name": "Toyota",
                                "model": "Toyota Camry",
                                "price_in_lakh": 18
                     }
                           ]
             }

2)Post request 

to insert data

Request URL :

      http://127.0.0.1:8000/api/cars

Response body

     {
      "success": true,
      "msg": "car details successfull"
     }

validation
 
 if already exists registration number is inserted then
 
 Response body
 
         "registration_no already exists"

 
3)PUT request 

to update the data

Request URL

         http://127.0.0.1:8000/api/cars/Maruti
	
Response body

              {
                   "success": true,
                  "msg": "car details updated  successfull"
              }

4)DELETE request 

to delete the data 

Request URL

         http://127.0.0.1:8000/api/cars/Maruti

Response body

         {
           "success": true,
           "msg": "car details deleted successfull"
         }


