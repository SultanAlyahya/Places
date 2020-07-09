Ful-Stack Capston Final Project

https://sultan-places.herokuapp.com/


Places API

Places API is an API that allows you to add, delete and modify togo places and places that you went, to allow the user to see where did you go and see your description about your trip or what you want to do if you go to this place and when you what to go

API dependencies

once you install the Project you need to install all the dependances first by running the command

pip install -r requirements.txt

To run the server on MacOS device, execute:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run

To run the server on Windows device from the powerShell, execute:

$:env:FLASK_APP="app.py"
$:env:FLASK_ENV=development
flask run

Endpoints

GET '/'
GET '/togo'
POST '/togo'
PATCH '/togo'
DELETE '/togo'
GET '/went'
POST '/went/

GET '/'
- Fetches a String
- Request Arguments: None
- Return: the word "works" to know that the server is working

GET '/togo'
- Fetches a dictionary of array togos
- Request Arguments: None
- Return: An array of object togo what contain id: integer key, location: String represent the name of the location, date: String represent the date, and descreption: String represent a decription of the place

{
    togos:[
        {
            id:1,
            location: "Riyadh",
            date: "2020/7/7",
            description: "i want to go there"
        }...
    ]
}

POST '/togo'
- Fetches A dictionary
- Request Arguments: location: String, date: String and description: String
- Return: A dictionary with one key "done" if "yes" so the togo have been added

{
    "done": "yes"
}

FETCH '/togo/<id:Integer>'
- Fetches A dictionary
- Request Arguments: location: String, date: String, description: String and URL 
  argument id: Integer
- Return: A dictionary with one key "done" if "yes" so the togo have been modified

{
    "done": "yes"
}

DELETE '/togo/<id:Integer>'
- Fetches A dictionary
- Request Arguments: URL argument id: Integer
- Return: A dictionary with one key "done" if "yes" so the togo have been deleted

{
    "done": "yes"
}


GET '/went'
- Fetches a dictionary of array wents
- Request Arguments: None
- Return: An array of object togo what contain id: integer key, location: String represent the name of the location, and descreption: String represent a decription of the place you went

{
    wents:[
        {
            id:1,
            location: "Riyadh",
            description: "i want to go there"
        }...
    ]
}

POST '/togo'
- Fetches A dictionary
- Request Arguments: location: String, description: String
- Return: A dictionary with one key "done" if "yes" so the togo have been added

{
    "done": "yes"
}

Testing 

to run the tests, you can by running the command
-python test.py