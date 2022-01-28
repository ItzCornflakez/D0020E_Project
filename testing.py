from pynput import keyboard
from pynput._util.win32_vks import DOWN, UP, LEFT, RIGHT
from camera import HDIntegratedCamera
camera = HDIntegratedCamera
from enum import Enum
from transform import Transform, Vector3
import numpy
import requests
from widefind import WideFind
import time

debug = False
camera = HDIntegratedCamera
camera_kitchen_pos = numpy.array([1500, -2602,  2186])
camera_kitchen_zero = numpy.array([1500, -2722,  2284])
camera_kitchen_floor = numpy.array([1500, -2722, 193])
camera_kitchen = HDIntegratedCamera("http://130.240.105.144/cgi-bin/aw_ptz?cmd=%23", camera_kitchen_pos, camera_kitchen_zero, camera_kitchen_floor)

widefind = WideFind("130.240.74.55", 1883)
widefind.run(debug)

while True:
    time.sleep(.2)

    if "F1587D88122BE247" in widefind.trackers:
       # print(widefind.trackers["F1587D88122BE247"])
        camera_kitchen.look_at_coordinate(widefind.trackers["F1587D88122BE247"])
        #camera_bedroom.look_at_coordinate(widefind.trackers["F1587D88122BE247"])
            
            
    def on_press(key):
    
    
        if key == keyboard.Key.down: # here you can choose the letter you want to get detected
            print("You pressed s")
            camera.rotate(100,20)
        if key == keyboard.Key.up: # here you can choose the letter you want to get detected
            print("You pressed w")
            camera.rotate(200,20)
        if key == keyboard.Key.left: # here you can choose the letter you want to get detected
            print("You pressed A")
            camera.rotate(50,100)
        if key == keyboard.Key.right: # here you can choose the letter you want to get detected
            print("You pressed d")    
            camera.rotate(300,80)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()