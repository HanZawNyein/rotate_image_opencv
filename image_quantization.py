import cv2
import numpy as np
import matplotlib.pyplot as plt

def quantimage(image,k):
    i = np.float32(image).reshape(-1,3)
    condition = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,20,1.0)
    ret,label,center = cv2.kmeans(i, k , None, condition,10,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    final_img = center[label.flatten()]
    final_img = final_img.reshape(image.shape)
    return final_img

if __name__ == '__main__':
    image = cv2.imread('a.png')
    plt.imshow(quantimage(image, 5))
    plt.show()
    # plt.imshow(quantimage(image, 8))
    # plt.show()
    # plt.imshow(quantimage(image, 25))
    # plt.show()
    # plt.imshow(quantimage(image, 35))
    # plt.show()
    # plt.imshow(quantimage(image, 45))
    # plt.show()