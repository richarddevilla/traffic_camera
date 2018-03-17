
import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\cas3.xml')

cars = []
for i in range(0,183):
    file_name ='trainer\\img'+str(i)+'.png'
    img = cv2.imread(file_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    try:
        cars.append(car_cascade.detectMultiScale(gray, 1.3, 5))
        i=111
        print('Car found!')
    except Exception:
        print('No car found!')
for car in cars:
    cnt=0
    for (x,y,w,h) in car:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cnt+=1
    print('Found '+str(cnt)+' cars!')


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()