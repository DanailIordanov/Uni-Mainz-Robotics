import cv2
import numpy as np

#Get source
# ~ cap = cv2.VideoCapture(0)
# ~ cap.set(3, 640)
# ~ cap.set(4, 480)
src = cv2.imread('./../../../res/testPic.jpg', cv2.IMREAD_UNCHANGED)

scale_percent = 30

width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

img = cv2.resize(src, (width, height))

while True:
	# ~ successful, img = cap.read()
	# ~ #imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# ~ #imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
	imgCanny = cv2.Canny(img, 100, 150)
	cv2.imshow("PiCam Stream", imgCanny)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# ~ img = np.zeros((512,512,3), np.uint8)
# ~ # img[:] = 255,0,0
# ~ # line(imgName, startPoint, endPoint = (width shape[1], height shape[0]), color = bgr, thickness) 
# ~ cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (255,0,0), 5)
# ~ cv2.rectangle(img, (128, 192), (img.shape[1] - 128, img.shape[0] - 64), (0,0,255), 3) #3/cv2.FILLED
# ~ cv2.circle(img, (194, 128), 32, (255, 0, 255), 2)
# ~ cv2.putText(img, " openCV ", (194, 256), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 



# ~ cv2.imshow("Image", img)
cv2.waitKey(0)
