#!/usr/bin/env python3
from __future__ import print_function
from geek.srv import*
import rospy
import cv2
#from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import sys
import qrcode
import numpy as np
import glob

def recognizedata(my_list):
    rospy.init_node('request')
    rospy.wait_for_service('decode')
    print("sever service found")
    try:
        srv = rospy.ServiceProxy('decode',decodeqr)
        resp = decode(my_list)
        #resp = decode(img_name,filelist)
        return resp.decoded_info
    except rospy.ServiceException as e:
        print("service call failed" + str(e))


if __name__ == '__main__':


    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k == 27:
            # ESC pressed
            print("Escape hit, closing...")
            cam.release()
            cv2.destroyAllWindows()
            
            
        elif k == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cv2.waitKey(10)
   #im = cv2.imread("img_name{}.png".format(img_counter))
    
    filelist = glob.glob('/home/groot/catkin_ws/src/geek/resources/*.jpg')
    #print(filelist)
    #image_file = rospy.get_param(location)

    my_list = []
    n = len(my_list)

    path = '/home/groot/catkin_ws/src/geek/resources/*.jpg'
    
    #glob module use for read multiple images on folder 
    for file in glob.glob(path):
        print(file)
        a = cv2.imread(file)
        my_list.append(a)
       
                                                                       


    #plt.imshow(my_list[0])
    #display(my_list,req)
    #rospy.init_node('request')
    #display(my_list)
    recognizedata(my_list)
    #recognizedata(img_name,filelist)
    #display(my_list)
    '''rospy.init_node('request')
    rospy.wait_for_service('decode')
    
    try:
        srv = rospy.ServiceProxy('decode',decodeqr)
        resp = decode(my_list)
        return resp.decoded_info
    except rospy.ServiceException as e:
        print("service call failed" + str(e))'''

    

