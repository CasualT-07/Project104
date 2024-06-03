import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (20, 220), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,255,255))

cv2.putText(img, "Mercury", (120, 220), cv2.FONT_HERSHEY_COMPLEX_SMALL, .5, (255,255,255))

cv2.putText(img, "Venus", (195, 220), cv2.FONT_HERSHEY_COMPLEX_SMALL, .5, (255,255,255))

cv2.putText(img, "Earth", (295, 260), cv2.FONT_HERSHEY_COMPLEX_SMALL, .5, (255,255,255))

cv2.putText(img, "Mars", (388, 220), cv2.FONT_HERSHEY_COMPLEX_SMALL, .5, (255,255,255))

cv2.putText(img, "Jupiter", (580, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, .5, (255,255,255))

cv2.putText(img, "Saturn", (770, 220), cv2.FONT_HERSHEY_COMPLEX_SMALL, .5, (255,255,255))

cv2.putText(img, "Uranus", (970, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL, .5, (255,255,255))

cv2.putText(img, "Uranus", (1100, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL, .5, (255,255,255))

cv2.imwrite("solar-system-named.jpg", img)

cv2.imshow("Solar System", img)

cv2.waitKey(0)