import numpy as np
import cv2
import time
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
customer_list = []
for i in range(0,20):
    customer_list.append("face"+str(i)+".jpg")
i = 0
while (True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # if i<30:
        #     cv2.imwrite(f"face"+str(i)+".jpg", roi_color)
        #     i+=1
        #     time.sleep(1)

        for customer in customer_list:
            customer_img = cv2.imread(customer, cv2.IMREAD_GRAYSCALE)
            customer_img = cv2.resize(customer_img, (w, h))
            diff = cv2.absdiff(roi_gray, customer_img)
            diff_mean = np.mean(diff)
            print(diff_mean)
            if diff_mean < 50:
                 print("Khách hàng đã mua hàng")
                 break

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
