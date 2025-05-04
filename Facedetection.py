import cv2

alg = "d:\Artifical Intelligence\Day_5\Day_5\haarcascade_frontalface_default.xml"

haar_cascade=cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0)

while True:
    _,img=cam.read()
    grayimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayimg,1.3,6,"aaro")
    
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+y,w+h),(0,0,255),2)
    cv2.imshow("Face detection", img)
    
    key = cv2.waitKey(10)
    if key==27:
        break
    
cam.release()
cv2.destroyAllWindows()
    
        
    
    