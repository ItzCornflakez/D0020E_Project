from flask import Blueprint, render_template, request, Response, make_response
from test_controller import Controller
import widefind as wf

views = Blueprint('views', __name__)
controller = Controller()

try: 
    widefind = wf.WideFind("130.240.74.55", 1883)
    widefind.run("ltu-system/#", False)
    widefind.attach(controller)
except:
    raise RuntimeError('Could not connect to WideFind')
else:
    print("WideFind connected")




@views.route('/')
def home():
    return render_template('/index.html', widefindTrackers = controller.trackersDict)
    
@views.route('/rotate', methods=['POST'])
def rotate():
    jsonData = request.get_json()
    i = int(jsonData['i'])
    j = int(jsonData['j'])    
    controller.rotate(i,j) 
    return ("nothing")

@views.route('/video_feed')
def video_feed():
    return Response(controller.changeFrameLoop(), mimetype='multipart/x-mixed-replace; boundary=frame')

@views.route('/follow')
def follow():
    print ("follow")
    return ('', 204)

@views.route('/look/<tracker>')
def look(tracker):
    controller.lookAtWideFind(tracker)
    return ('', 204)

@views.route('/switch')
def switch():
    print ("switch")
    return ("nothing")

@views.route('/disconnect')
def disconnect():
    print ("disconnect")
    return ("nothing")



#WideFind stuff
@views.route("/getWidefind")
def getWidefind():
    response = controller.trackersDict
    return Response(str(response))

@views.route("/getWidefindCoordinates")
@views.route("/getWidefindCoordinates/<wfID>")
def getWidefindCoordinates(wfID):
    response = controller.trackersDict.get(wfID)
    print(response)
    return Response(str(response))


