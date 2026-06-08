import cv2
fac=r"C:\Users\gajap\Downloads\haarcascade_frontalface_default.xml"
facial=cv2.CascadeClassifier(fac)
cam=cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fase_cascade=facial.detectMultiScale(grayimg,1.5,9)
    for (x,y,w,h) in fase_cascade:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Show",img)
    key=cv2.waitKey(10)
    print(key)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()
    
        
