from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('/test.html')

@views.route('/rotate')
def rotate():
    print ("rotate")
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