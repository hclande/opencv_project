# opencv_project

modules used for this project:
opencv (cv2),
numpy,
pickle,
pillow,
os,

#
this project has been made by following the opencv tutorial from
#joincfe.com



##These files uses any webcamera that are properly set up to the computer.
##there is no need for any setup for the camera to run any of these files.





#cap-img.py
\n
to capture images for data base, run cap-img.py
type in the name of the subject, this will be the name of the image folder.
this will capture images every 500ms, in total 50 images per use.
this file can be used several times pr.subject, image numbering will continue from last image number. 

#faces-train.py
this file sets up the recognition data, to be used by face.py
after new photos has been added to the images folder this trainner has to be executed.


#faces.py
this is the face recognition script.

#camera-test.py
just for testing of camera


#trainner.yml
this is the recognition database file

#labels.pickel###
this is the image labels and subject name data file.

#cascade folder##
this folder contains the different types of image identification