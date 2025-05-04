import cv2
import imutils

redLower = (58, 95, 80)
redUpper = (147, 255, 255)

cam = cv2.VideoCapture(0)

while True:
    _,img=cam.read()

    img=imutils.resize(img,width=1000)
    smooth=cv2.GaussianBlur(img,(11,11),0)
    hsv=cv2.cvtColor(smooth,cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, redLower , redUpper )
    mask = cv2.erode(mask, None , iterations=2)
    mask = cv2.dilate(mask, None , iterations=2)
    
    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    centre=None
    if len(cnts)>0:
        c=max(cnts,key=cv2.contourArea)
        ((x,y),radius) = cv2.minEnclosingCircle(c) 
        m = cv2.moments(c)
        centre=(int(m["m10"]/m["m00"]),int(m["m01"]/m["m00"]))
        if radius > 10 :
            cv2.circle(img,(int(x),int(y)),int(radius),(0,255,255),2)
            cv2.circle(img,centre,5,(0,0,255),1)
            print(centre,radius)
            if radius>250:
                print("Stop")
                
            else :
                if(centre[0]<150):
                    print("Right")
                elif(centre[0]>450):
                    print("Left")
                elif(radius<250):
                    print("Front")
                else:
                    print("Stop")

    cv2.imshow("frame", img)
    key=cv2.waitKey(10)& 0xFF
    if key==ord("q"):
        break
    
cam.release()
cv2.destroyAllWindows()



