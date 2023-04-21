import os
from threading import Thread
from time import sleep
from tkinter import messagebox

import cv2
from detection.training import Training


class Record:
    def __init__(self, customerID) -> None:
        self.customerID = customerID
        self.roi_gray = None
        self.flag = False
        self.face_dir = fr'cafe_application\img\faces'
        try:
            os.mkdir(self.face_dir)
        except:
            pass

    def show_instruction(self):
        pass

    def take_pictures(self):
        new_dir = fr'{self.face_dir}\{self.customerID}'
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        self.i = 0
        while self.i < 40:
            sleep(1)
            if self.roi_gray is not None:
                cv2.imwrite(fr"{new_dir}\{self.i:03}.jpg", self.roi_gray)
            else:
                self.i -= 1
            self.i += 1
        self.flag = True

    def recording(self):
        face_cascade = cv2.CascadeClassifier(r'cafe_application\src\detection\haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        thread = Thread(target=self.take_pictures)
        thread.start()
        while (True):
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                self.roi_gray = gray[y:y+h, x:x+w]

                pos = (x + 10, y + h - 10)
                if self.i < 10:
                    cv2.putText(frame, "Nhin len", pos, cv2.FONT_HERSHEY_SIMPLEX, 1, (36, 255, 12), 2)
                elif self.i < 20:
                    cv2.putText(frame, "Nhin xuong", pos, cv2.FONT_HERSHEY_SIMPLEX, 1, (36, 255, 12), 2)
                elif self.i < 30:
                    cv2.putText(frame, "Nhin trai", pos, cv2.FONT_HERSHEY_SIMPLEX, 1, (36, 255, 12), 2)
                else:
                    cv2.putText(frame, "Nhin phai", pos, cv2.FONT_HERSHEY_SIMPLEX, 1, (36, 255, 12), 2)

            if self.flag:
                messagebox.showinfo("Message", "Đăng ký thành công!")
                break
            cv2.imshow('Sign up', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

        Training().train(self.customerID)
