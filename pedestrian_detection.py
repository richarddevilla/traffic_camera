import numpy as np
import cv2

full_body_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_full_body.xml')
upper_body_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_upperbody.xml')
lower_body_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_lowerbody.xml')

pedestrian = []
file_name ='pedestrian\\img2.png'
img = cv2.imread(file_name)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
try:
    pedestrian.append(lower_body_cascade.detectMultiScale(gray, 1.3, 5))
except Exception:
    print('No pedestrian lower body found!')
try:
    pedestrian.append(full_body_cascade.detectMultiScale(gray, 1.3, 5))
except Exception:
    print('No pedestrian full body found!')
print(pedestrian)
try:
    pedestrian.append(upper_body_cascade.detectMultiScale(gray, 1.3, 5))
except Exception:
    print('No pedestrian upper body found!')
print(pedestrian)

print(pedestrian)

for each in pedestrian:
    try:
        for (x,y,w,h) in each:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
    except:
        print('No one detected')

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
