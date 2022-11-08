import cv2

path = r"images\download.jpg"

# Reading an image in default mode
src = cv2.imread(path)

# Convert to Grayscale
img_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

# To display Image
window_name='Grayscale Conversion OpenCV'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name,img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()