import numpy as np
import cv2
import threading
import os
import time

cap = cv2.VideoCapture(0)
name = input("name:")
num = 0


def capture(name,num,start):
    #print ("capture")
    img = " "
    img_dir = str("images\\" + name + "\\" )                                     #directory path
    img_item = str("images\\" + name + "\\" + name + "_" + str(num) +" .png")
    print (img_dir)
    num = len(os.listdir(img_dir)) + 1 # counts number of files in image path and adds one to num

        
    og_num = num

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
        
        
        if not os.path.exists(img_dir):         # if directory is not there, make the directory
            os.makedirs(img_dir)
        if start + 0.5 < time.time():
            if img != " ":
                cv2.destroyWindow("capture")
            cv2.imwrite(img_item, gray)
            print (img_item)
            img = cv2.imread(img_item,-1)
            cv2.imshow("capture",img)
            num += 1
            start = time.time()
        
        if num == (og_num + 50) or cv2.waitKey(20) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()



start = time.time()    
capture(name,num,start)
   


cap.release()
cv2.destroyAllWindows()
#t1 = threading.Thread( target= show() )
#t2 = threading.Thread( target= capture(name,num) )

#t1.start()
#t2.start()
# When everything done, release the capture
