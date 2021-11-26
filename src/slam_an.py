#! /usr/bin/env python3
from typing import Sized
from owlready2 import *
import random
import os
import rospy
import json
import std_msgs.msg as std
from visualization_msgs.msg import Marker
import numpy as np

#import words_for_pico
os.chdir(sys.path[0])
#words_for_pico.run()
file = open("vertices_list(1)","w+")
arr=[]
def callback(vertices):
    print(len(vertices.points))

    for each in vertices.points:
        arr.append([each.x,each.y,each.z])

  
        
        
    




def listener():
    rospy.init_node('listener_for_word', anonymous=True)

    sub_once=None

    sub_once=rospy.Subscriber("Mapper/vertices", Marker, callback,sub_once)

    rospy.spin()


if __name__=="__main__":
    # listener()

    rospy.init_node('listener_new', anonymous=True)
    vertices=rospy.wait_for_message('Mapper/vertices', Marker)
    print(vertices)
    for each in vertices.points:
        arr.append([each.x,each.y,each.z])
    np.save("array2",arr)


    print("done")
    