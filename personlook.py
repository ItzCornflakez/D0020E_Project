from transform import Vector3
from array import array


class Personlook:
    
    def positioner(self):    
        pos = [1]
        while len(pos) != 0:
            pos = list(map(int,input("\nEnter cordinates : ").strip().split(",")))[:3]

            return  Vector3(pos[0],pos[1],pos[2])
            
        print('x cord: ', x)
        print('y cord: ', y)
        print('z cord: ', z)
    
    
   # def personLook(self):
      #  while true:
            