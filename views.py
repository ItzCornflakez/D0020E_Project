from xml.dom.minidom import Document
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
    print ("this is controller src:" + str(controller.src))
    return render_template('/index.html', src = controller.src, widefindTrackers = controller.trackersDict)
    
@views.route('/rotate', methods=['POST'])
def rotate():
    controller.is_follow = False
    jsonData = request.get_json()
    i = int(jsonData['i'])
    j = int(jsonData['j'])    
    controller.rotate(i,j) 
    return ("nothing")

@views.route('/look/<tracker>')
def look(tracker):
    controller.is_follow = False
    controller.lookAtWideFind(tracker)
    return ('', 204)  # Return "204 No Content"

@views.route('/follow/<tracker>')
def follow(tracker):
    controller.is_follow = True
    controller.followWideFind(tracker)
    print ("follow")
    return ('', 204)

@views.route('/switchCam/<cam>')
def switchCam(cam):
    controller.switchCam(cam)
    if(cam == "Kitchen"):
        controller.src = "http://130.240.105.144/cgi-bin/mjpeg?resolution=1920x1080&amp;framerate=5&amp;quality=1"
    if(cam == "Bedroom"):
        controller.src = "http://130.240.105.145/cgi-bin/mjpeg?resolution=1920x1080&amp;framerate=5&amp;quality=1"
    return('', 204)

@views.route('/disconnect')
def disconnect():
    print ("disconnect")
    return ("nothing")

#Manual control stuff
@views.route('/up')
def up():
    controller.up()
    print ("up")
    return ('', 204)

@views.route('/down')
def down():
    controller.down()
    print ("down")
    return ('', 204)

@views.route('/left')
def left():
    controller.left()
    print ("left")
    return ('', 204)

@views.route('/right')
def right():
    controller.right()
    print ("right")
    return ('', 204)

@views.route('/zoomIn')
def zoomIn():
    controller.zoomIn()
    print ("Zoom in")
    return ('', 204)

@views.route('/zoomOut')
def zoomOut():
    controller.zoomOut()
    print ("Zoom out")
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


