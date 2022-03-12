from flask import Blueprint, jsonify, render_template, request, Response, make_response
from controller import Controller
import widefind as wf
import json

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
    return render_template('/index.html', src = controller.src, log_rows = controller.log_rows, widefindTrackers = controller.WideFindNameDict)
    
@views.route('/rotate', methods=['POST'])
def rotate():
    controller.is_follow = False
    jsonData = request.get_json()
    i = int(jsonData['i'])
    j = int(jsonData['j'])    
    controller.rotate(i,j)
    action = "Has rotated to (" + str(i) + "," + str(j) + ")"
    response = controller.databaseActions(action) 
    return Response(str(response))

@views.route('/look/<tracker>')
def look(tracker):
    name = ""
    for key, value in controller.WideFindNameDict.items():
        if key == tracker:
            name = tracker
            tracker = value
    controller.is_follow = False
    controller.lookAtWideFind(tracker)
    action = "Now looking at " + name + ""
    controller.databaseActions(action) 
    return ('', 204)

@views.route('/follow/<tracker>')
def follow(tracker):
    name = ""
    for key, value in controller.WideFindNameDict.items():
        if key == tracker:
            name = tracker
            tracker = value
    controller.is_follow = True
    controller.followWideFind(tracker)
    action = "Now following " + name + ""
    controller.databaseActions(action) 
    return ('', 204)

@views.route('/switchCam/<cam>')
def switchCam(cam):
    controller.switchCam(cam)
    if(cam == "Kitchen"):
        controller.src = "http://130.240.105.144/cgi-bin/mjpeg?resolution=1920x1080&amp;framerate=5&amp;quality=1"
    if(cam == "Bedroom"):
        controller.src = "http://130.240.105.145/cgi-bin/mjpeg?resolution=1920x1080&amp;framerate=5&amp;quality=1"
    action = "Has switched to " + cam + ""
    response = controller.databaseActions(action) 
    return Response(str(response))

#Manual control stuff
@views.route('/up')
def up():
    controller.up()
    return ('', 204)

@views.route('/down')
def down():
    controller.down()
    return ('', 204)

@views.route('/left')
def left():
    controller.left()
    return ('', 204)

@views.route('/right')
def right():
    controller.right()
    return ('', 204)

@views.route('/zoomIn')
def zoomIn():
    controller.zoomIn()
    return ('', 204)

@views.route('/zoomOut')
def zoomOut():
    controller.zoomOut()
    return ('', 204)


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

@views.route("/updateLog")
def updateLog():
    arr = []
    for row in controller.log_rows:
        arr.append(row[1])
    response = arr
    return Response(json.dumps(response))
