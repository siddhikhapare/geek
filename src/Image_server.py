#!/usr/bin/env python3
from __future__ import print_function
from geek.srv import decodeqr,decodeqrResponse
import rospy
import cv2
#from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import sys
import qrcode
import numpy as np
import glob

#bridge = CvBridge()

        
def display(my_list,req):
    bridge = CvBridge()
    #global bridge
    #converting ros to opencv image
    try:
        image = bridge.imgmsg_to_cv2(my_list,"bgr8")
        success = True
    except CvBridgeError as e:
        print(e)
    return decodeqrResponse(success)

    success = False
    for x in my_list:
        x = np.arange(0,n)
    d = cv2.QRCodeDetector()
    retval,decoded_info,points,straight_qrcode = d.detectAndDecodeMulti(np.hstack(my_list))
    print(req.decoded_info)
    

def decode():
     rospy.init_node("response")
     s = rospy.Service('decode',decodeqr,display)
     rospy.spin()

    
       

if __name__ =="__main__":
    decode()
    '''rospy.init_node("response")
    s = rospy.Service('decode',decodeqr,display)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")'''
    