import cv2

def main():
    print("Hello World!")
    src = cv2.imread('./../res/testPic.jpg', cv2.IMREAD_UNCHANGED)

    img = cv2.resize(src, (src.shape[1] / 3, src.shape[0] / 3))
    
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    
    cv2.imshow("Image", img)
    cv2.waitKey(0)


if __name__=='__main__':
    main()
