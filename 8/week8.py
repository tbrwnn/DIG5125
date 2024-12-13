import cv2 

#create a video caputure object
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc (* 'XVID')
out = cv2.VideoWriter ('output.avi', fourcc , 20.0 , (640 ,480) )

#check is camera opened successfully
if not cap.isOpened() :
    print('Error: could not open video.')
    exit()

while cap.isOpened() :
    #capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        #display the resulting frame
        cv2.imshow('Frame', frame)
        out.write ( frame )

        #press q on keyboard to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows ()
     
#when ever