from flask import Blueprint

#Create a Blueprint
hello_world_bp = Blueprint("hello_world", __name__)

#Define an endpoint
@hello_world_bp.get("/")
def say_hello_world():
    return "Hello world!"


# #Define a second endpoint 
# @hello_world_bp.get("/hello/JSON")
# def 

@hello_world_bp.get("c")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body

