import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import csv
import sys
import openpyxl,xlrd
from openpyxl import Workbook
import pathlib
import pandas as pd
import numpy as np

imagePath = "t1.jpg"

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print("[INFO] Found {0} Faces.".format(len(faces)))

for (x, y, w, h) in faces:
   # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = image[y:y + h, x:x + w]
    print("[INFO] Object found. Saving locally.")
    cv2.imwrite("abc/"+str(w) + str(h) + '_faces.jpg', roi_color)

status = cv2.imwrite('faces_detected.jpg', image)
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)

my_array = np.genfromtxt('../my_file.csv', delimiter=',')
new_array=enumerate(my_array)
print(len(my_array))
index=[]

Testimg=[]
TestClass=[]
Test_Path="abc"
Test_List=os.listdir(Test_Path)
for cl in Test_List:
    curImg = cv2.imread(f'{Test_Path}/{cl}')
    Testimg.append(curImg)
    TestClass.append(os.path.splitext(cl)[0])
def findEncodings_Test(Testimg):
    try:
        encodeList = []
        for img in Testimg:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            c=1
            f=0
            for test in my_array:
                if((face_recognition.face_distance([test],encode)[0])<0.5):
                    index.append(c)
                    f=1
                c=c+1
            if f==0:
                index.append(-1)
            encodeList.append(encode)
    except IndexError as e:
            print(e)
    return index
op=findEncodings_Test(Testimg)
print(op)
filename="../attendance.xlsx"
file=openpyxl.load_workbook("../attendance.xlsx")
sheet=file.active
df = pd.read_excel(filename)[["ER Number"]]
for x in op:
    i=0
    for y in df['ER Number']:
        if x==y:
            sheet.cell(column=3,row=i+1,value="p")
            i=0
        i+=1
file.save(r'attendance.xlsx')
            
            




