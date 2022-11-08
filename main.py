import cv2  # importing cv
import imutils

if __name__ == '__main__':
    # read an image as input using OpenCV
    image = cv2.imread(r"images\download.jpg")
    Rotated_image = imutils.rotate(image, angle=90)
    cv2.imshow("Rotated", Rotated_image)
    cv2.waitKey(0)
