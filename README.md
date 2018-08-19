# opencv_project

This project has been made by following the opencv tutorial from joincfe.com
These files uses any webcamera that are properly set up to the computer.
there is no need for any additional setup for the camera to run any of these files.



modules used for this project:
opencv (cv2),
numpy,
pickle,
pillow,
os,



## cap-img.py

to capture images for data base, run cap-img.py
type in the name of the subject, this will be the name of the image folder.
this will capture images every 500ms, in total 50 images per use.
this file can be used several times pr.subject, image numbering will continue from last image number. 


## Capture-unknown-faces.py

this script are basically the same as faces.py. Except that this captures photos of all unknown faces and stores them under \images folder\unknown-subject_"timestamp".png 



## faces-train.py

this file sets up the recognition data, to be used by face.py
after new photos has been added to the images folder this trainner has to be executed.


## faces.py

this is the face recognition script.

## camera-test.py

just for testing of camera


## trainner.yml

this is the recognition database file

## labels.pickel

this is the image labels and subject name data file.

## cascade folder

this folder contains the different types of image identification