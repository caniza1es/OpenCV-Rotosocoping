import cv2
import sys

cap = cv2.VideoCapture(sys.argv[1])

if (cap.isOpened()== False): 
  print("Error opening video stream or file")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    edges = cv2.Canny(blur,50,150)
    dilated = cv2.dilate(edges, None)
    result = cv2.bitwise_and(frame, frame, mask=dilated)
    out.write(result)
    cv2.imshow('Frame',result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else: 
    break

cap.release()
out.release()
cv2.destroyAllWindows()
