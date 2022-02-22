from flask import Blueprint, render_template, request, Response, make_response
from test_controller import Controller
import widefind as wf

views = Blueprint('views', __name__)
controller = Controller()

try: 
    widefind = wf.WideFind("130.240.74.55", 1883)
    widefind.run("ltu-system/#", False)
except:
    raise RuntimeError('Could not connect to WideFind')
else:
    print("WideFind connected")

widefind.attach(controller)


@views.route('/')
def home():
    return render_template('/index.html', widefindTrackers = widefind.trackers) #LAST PART NOT MVC
    
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



#WideFind stuff( NOT MVC)
@views.route("/getWidefind")
def getWidefind():
    response = widefind.trackers
    return Response(str(response))

@views.route("/getWidefindCoordinates")
@views.route("/getWidefindCoordinates/<wfID>")
def getWidefindCoordinates(wfID):
    response = widefind.trackers.get(wfID)
    print(response)
    return Response(str(response))


