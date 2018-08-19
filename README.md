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

this project was made with python version 3.7.0 and opencv version 3.4.2


## install and run this project

download and install python from pyton.org, make shure to tick of "add python to path" while installing.

use PIP to install modules:
        pip install opencv-python --upgrade
        pip install numpy --upgrade
        pip install pickle --upgrade
        pip install pillow --upgrade

download this repository and unpack to desired folder.
add reference pictures of faces in named folders in \images\"name_of_subject"

now you can run the files from windows power shell or cmd. 
cd into the copied folder containing the .py files

run files by typing: python "filename.py"
example: c:\opencv-project\python faces.py

UPDATE REFERENCE DATABASE by running "faces-train.py" 
now run the "faces.py" file to start facial recognizion



## cap-img.py

to capture grayscale images for data base, run cap-img.py
script will promt for name and number of pictures that are to be taken.

name of the subject, this will be the name of the image folder.
this will capture images every 500ms.
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