import os
import cv2
import numpy as np
from PIL import Image
import pickle
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  #gets this files directory path
image_dir = os.path.join(BASE_DIR, "images")           # appends images to the base directory

face_cascade = cv2.CascadeClassifier("cascades\\data\\haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
current_id = 0
label_ids = {}
y_labels = []
x_train = []



for root, dirs, files in os.walk(image_dir):                #searches all directories beyond the image directory 
    for file in files:                                      #
        if file.endswith("png") or file.endswith("jpg"):    # for files ending with png or jpg
            path = os.path.join(root,file)                  # set the final path of image
            label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower() # label = name of the person in picture/ name of picture folder
            #print (label,path)        

            if not label in label_ids:            
                          # if label/ picture folder is not in label_ids list
                label_ids[label] = current_id               # add an ID to the person/ image folder to label dictonary
                current_id += 1                             # increments the current ID number, (ready for next person)
            
            id_ = label_ids[label]                          
           # print(label_ids)
            
            pil_image= Image.open(path).convert("L")        # turn image in to gray scale
            image_array = np.array(pil_image, "uint8")      # turn image in to an nubmer array(pixel data)
            #print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
           
           
            for (x,y,w,h) in faces:                     # gets the "region of interest"(face)
                roi = image_array[y:y+h, x:x+w]         # from the images (image array/pixel data)
                x_train.append(roi)                     # adds the registered "roi" to the x_train dictonary, this is the stored data to compare faces against
                y_labels.append(id_)                    # adds the corresponding id to the picture/face

with open ("labels.pickel", "wb") as f:
    pickle.dump(label_ids, f )

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")
