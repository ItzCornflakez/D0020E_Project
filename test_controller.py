from optparse import Values
from re import X
from camera import HDIntegratedCamera
from observer_pattern.observer import Observer, Subject
import numpy

from widefind import WideFind
import widefind as wf
import pymysql


class Controller(Observer):
    def __init__(self):
        
        self.getAllLogs()

        self.src = "http://130.240.105.144/cgi-bin/mjpeg?resolution=1920x1080&amp;framerate=5&amp;quality=1"

        self.camera_bedroom_pos = numpy.array([619, 3935, 2600])
        self.camera_bedroom_zero = numpy.array([-765, 4112, 2878])
        self.camera_bedroom_floor = numpy.array([531, 3377, 331])

        self.camera_kitchen_pos = numpy.array([2873, -2602, 2186])
        self.camera_kitchen_zero = numpy.array([3413, -2722, 2284])
        self.camera_kitchen_floor = numpy.array([2694, -2722, 193])

        self.cam = HDIntegratedCamera("http://130.240.105.144/cgi-bin/aw_ptz?cmd=%23")
        self.cam_trans = wf.Transform(self.camera_kitchen_pos, self.camera_kitchen_zero, self.camera_kitchen_floor)

        self.rotate(210, 140)

        self.trackers = []
        self.trackersDict = {}

        self.rot_amount = 6
     
        self.followTarget = ""
        self.is_follow = False

    def createWideFindNameDict(self):
        oldNamesDict = {"Kitchen counter":"543D85B1B2D91E29",
                                "Kitchen corner 1":"9691FE799F371A4C",
                                "Kitchen corner 2":"D4984282E2E4D10B",
                                "Bed":"4B2A8EE2B9BAAAC0",
                                "Door":"03FF5C0A2BFA3A9B"
                                }
        self.WideFindNameDict = {}
        for key, value in self.trackersDict.items():
            for name, old_value in oldNamesDict.items():
                if key == old_value and key not in self.WideFindNameDict.values():
                    self.WideFindNameDict[name] = key             

    def rotate(self, i, j):
        self.cam.rotate(i, j)

    def lookAtWideFind(self, val):
        if val in self.trackers:
            tracker_pos = self.trackersDict[val]
            new_yaw = self.cam_trans.get_yaw_from_zero(tracker_pos)
            new_pitch = self.cam_trans.get_pitch_from_zero(tracker_pos)

            self.cam.rotate(new_yaw, new_pitch + 80)

    def followWideFind(self, val):
        self.followTarget = val

    def switchCam(self, cam):
        if(cam == "Kitchen"):
            self.cam = HDIntegratedCamera("http://130.240.105.144/cgi-bin/aw_ptz?cmd=%23")
            self.cam_trans = wf.Transform(self.camera_kitchen_pos, self.camera_kitchen_zero, self.camera_kitchen_floor)
        if(cam == "Bedroom"):
            self.cam = HDIntegratedCamera("http://130.240.105.145/cgi-bin/aw_ptz?cmd=%23")
            self.cam_trans = wf.Transform(self.camera_bedroom_pos, self.camera_bedroom_zero, self.camera_bedroom_floor)

    def up(self):
        self.is_follow = False
        self.cam.rotate(self.cam.get_current_yaw(), self.cam.get_current_pitch() + self.rot_amount)

    def down(self):
        self.is_follow = False
        self.cam.rotate(self.cam.get_current_yaw(), self.cam.get_current_pitch() - self.rot_amount)

    def left(self):
        self.is_follow = False
        self.cam.rotate(self.cam.get_current_yaw() - self.rot_amount, self.cam.get_current_pitch())

    def right(self):
        self.is_follow = False
        self.cam.rotate(self.cam.get_current_yaw() + self.rot_amount, self.cam.get_current_pitch())

    def zoomIn(self):
        self.cam.zoom(50)

    def zoomOut(self):
        self.cam.zoom(0)

    def databaseConn(self):
        #localhost xampp phpmyadmin database
        self.connection = pymysql.connect(host="localhost", user="root", passwd="", database="log")
        self.cursor = self.connection.cursor()

        #logtable( log_id(int), entry(text), created_at(timestamp))

    def getAllLogs(self):
        self.databaseConn()

        sql = "SELECT * FROM log_table"
        self.cursor.execute(sql)
        self.log_rows = self.cursor.fetchall()
        for row in self.log_rows:
            print(row)
        self.connection.close()
    
    def databaseActions(self, action):
        self.databaseConn()
        sql = "INSERT INTO log_table(entry) VALUES('" + str(action) + "');"
        print(sql)
        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()
        self.getAllLogs()
        return self.log_rows

        


    def update(self, subject: WideFind):
        self.trackersDict = subject.trackers
        self.createWideFindNameDict()
        self.trackers = subject.trackers.keys()
        if(self.is_follow == True):
            if(self.followTarget in self.trackers):
                self.lookAtWideFind(self.followTarget)
        
