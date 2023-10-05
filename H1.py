import cv2
img = cv2.imread("GOJO.png",0)
cv2.imshow("show Result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("result.png",img)