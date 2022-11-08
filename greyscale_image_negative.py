import cv2

path = r"images\download.jpg"

# Reading an image in default mode
src = cv2.imread(path)

# Convert to Grayscale
img_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

# invert
invert_img = cv2.bitwise_not(img_gray)
# To display Image
window_name='Grayscale Conversion OpenCV'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name,invert_img)
cv2.waitKey(0)
cv2.destroyAllWindows()