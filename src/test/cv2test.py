import cv2
import numpy as np

img = cv2.imread("D:\Test.jpg")
emptyImage = np.zeros(img.shape, np.uint8)
emptyImage2 = img.copy()

cv2.imshow("Python+OpenCV", emptyImage2)
cv2.waitKey (0)
cv2.destroyAllWindows()