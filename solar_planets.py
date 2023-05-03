import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "sun",
            (100,100),
            cv2.FONT_HERSHEY_COMPLEX,
            1.2,
            (0,0,255)
            )

cv2.putText(img,
            "mercury",
            (100,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,255)
            )

cv2.putText(img,
            "venus",
            (200,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,255)
            )

cv2.putText(img,
            "earth",
            (300,279),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,0)
            )

cv2.putText(img,
            "mars",
            (400,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "jupiter",
            (500,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,100,0)
            )

cv2.putText(img,
            "saturn",
            (800,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "uranus",
            (990,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (100,100,100)
            )

cv2.putText(img,
            "neptune",
            (1100,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.imshow("output",img)           
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)