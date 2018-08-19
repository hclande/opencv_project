"""
this script will take grayscale images of a subject. 
it will ask for the subjet name, this will be the folder name wich the images are stored in:
\images\"subject name"\
and number of pictures that are to be taken.

script can be cancled by pressing q while running.

Based on opencv tutorial by joincfe.com
"""

import numpy as np
import cv2
import os
import time

cap = cv2.VideoCapture(0)
name = input("name:")
num_photo= input("how many photos?:")                       # get the name of the subject
num = 0


def capture(name,num,start):
    #print ("capture")
    img = " "
    img_dir = str("images\\" + name + "\\" )                                     #directory path
    img_item = str("images\\" + name + "\\" + name + "_" + str(num) +" .png")
    print (img_dir)
    if not os.path.exists(img_dir):         # if directory is not there, make the directory
        os.makedirs(img_dir)
    num = len(os.listdir(img_dir)) + 1 # counts number of files in image path and adds one to num

        
    og_num = num                                # get the current number of files in directory

    while(True):
        print(num)
        #print ("capture while loop start")
        # Capture frame-by-frame
        ret, frame = cap.read()
        #num += 10
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        
        cv2.imshow('gray',gray)
        img_dir = str("images\\" + name + "\\" )                                     #directory path
        img_item = str("images\\" + name + "\\" + name + "_" + str(num) +".png")    #directory path and file name
        
        
        
        
        if start + 0.5 < time.time():           # captures images every 0,5sec
            if img != " ":
                cv2.destroyWindow("capture")


            cv2.imwrite(img_item, gray)         #saves image 
            print (img_item)                    
            img = cv2.imread(img_item,-1)       #reads saved image
            cv2.imshow("capture",img)           #displays saved image in second frame
            num += 1                            # adds number of  image
            start = time.time()                 #resets time for next image
        
        if num == (og_num + int(num_photo)) or cv2.waitKey(20) & 0xFF == ord('q'): # quits program after number of images or if q is pressed
            break


    cap.release()
    cv2.destroyAllWindows()



start = time.time()    
capture(name,num,start)
   


cap.release()
cv2.destroyAllWindows()
# When everything done, release the capture
