import cv2
import numpy as np
from src import configuration as config


def main():
    path = './../res/testPic.jpg'

    src = cv2.imread(path)
    img = cv2.resize(src, (int(src.shape[1] / 3), int(src.shape[0] / 3)))

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([config.HUE_MIN, config.SAT_MIN, config.VAL_MIN])
    upper = np.array([config.HUE_MAX, config.SAT_MAX, config.VAL_MAX])

    mask = cv2.inRange(imgHSV, lower, upper)

    imgResult = cv2.bitwise_and(img, img, mask=mask)
    print(imgResult)
    #
    # config.get_trackbars(img)


if __name__=='__main__':
    main()
