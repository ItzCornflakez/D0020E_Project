from flask import Blueprint, render_template, request
from test_controller import Controller

views = Blueprint('views', __name__)
controller = Controller()

@views.route('/')
def home():
    return render_template('/test.html')
    
@views.route('/rotate', methods=['POST'])
def rotate():
    jsonData = request.get_json()
    i = int(jsonData['i'])
    j = int(jsonData['j'])    
    controller.rotate(i,j) 
    return ("nothing")

@views.route('/follow')
def follow():
    print ("follow")
    return ("nothing")

@views.route('/look')
def look():
    print ("look")
    return ("nothing")

@views.route('/switch')
def switch():
    print ("switch")
    return ("nothing")

@views.route('/disconnect')
def disconnect():
    print ("disconnect")
    return ("nothing")