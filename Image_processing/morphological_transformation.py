import cv2
import numpy as np

img = cv2.imread(r"C:\Users\saikeerthana\OneDrive\Desktop\revise\AI engagement tracker\Image_processing\image2.jpg", 0)
kernel = np.ones((5,5), np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Opening (Noise Removal)', opening)
cv2.imshow('Closing (Fill Gaps)', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
