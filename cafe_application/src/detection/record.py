import numpy as np
import cv2
from time import sleep
from tkinter import messagebox
from threading import Thread
class Record:
    def __init__(self, customerID) -> None:
        self.customerID = customerID

    def writeimg(self):
        cv2.imwrite(f"face." + self.customerID + "." + str(self.i)+".jpg", self.roi_color)
        self.i+=1
        sleep(1)

    def recording(self):
        face_cascade = cv2.CascadeClassifier('D:\\vscode\\veterinary-clinic\\cafe_application\\src\\detection\\haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        self.i = 0
        while (True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                self.roi_color = frame[y:y+h, x:x+w]

                if self.i<30:
                    if self.i == 0:
                        messagebox.showinfo("Message", "Vui lòng nhìn thẳng!")
                    if self.i == 10:
                        messagebox.showinfo("Message", "Vui lòng quay sang trái!")
                    if self.i == 20:
                        messagebox.showinfo("Message", "Vui lòng quay sang phải!")
                    thread = Thread(target=self.writeimg)
                    thread.start()

            if self.i == 30:
                messagebox.showinfo("Message", "Đăng ký thành công!")
                break
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


