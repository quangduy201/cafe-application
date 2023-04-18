import numpy as np
import cv2
from tkinter import *
from tkinter import messagebox
from BLL.CustomerBLL import CustomerBLL
from DTO.Customer import Customer
class Detection:
    def __init__(self, textfield) -> None:
        self.customerBLL = CustomerBLL()
        self.textfield = textfield
        self.customersID = []
        for customer in self.customerBLL.searchCustomers("MEMBERSHIP = 1"):
            self.customersID.append(self.customerBLL.getValueByKey(customer, "CUSTOMER_ID"))

    def detect(self):
        face_cascade = cv2.CascadeClassifier('D:\\vscode\\veterinary-clinic\\cafe_application\\src\\detection\\haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        customer_list = []
        self.diff_mean = dict()
        for customerID in self.customersID:
            for i in range(0,20):
                customer_list.append("face." + customerID + "." + str(i)+ ".jpg")

        self.countFailed = 0

        self.flag = 0
        while (self.flag == 0):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                for customer in customer_list:
                    customer_img = cv2.imread(customer, cv2.IMREAD_GRAYSCALE)
                    customer_img = cv2.resize(customer_img, (w, h))
                    diff = cv2.absdiff(roi_gray, customer_img)
                    mean = np.mean(diff)
                    name = customer
                    self.diff_mean[name] = mean

                min_key = min(self.diff_mean, key = self.diff_mean.get)
                if (self.diff_mean.get(min_key) <= 35):
                    self.customer = self.customerBLL.searchCustomers("CUSTOMER_ID = '" + min_key.split(".")[1] + "'")[0]
                    print(self.customer.__str__())
                    self.textfield[1].delete(0, END)
                    self.textfield[1].insert(END, self.customer.getCustomerID())
                    messagebox.showinfo("Message", "Nhận diện khách hàng thành viên thành công!")
                    self.flag = 1
                else:
                    print ("Khach hang chua dang ky thanh vien")
                    self.textfield[1].delete(0, END)
                    self.countFailed = self.countFailed + 1
                    if self.countFailed == 50:
                        self.customer = Customer(customerID=self.customerBLL.getAutoID())
                        self.customerBLL.addCustomer(self.customer)
                        self.textfield[1].delete(0, END)
                        self.textfield[1].insert(END, self.customer.getCustomerID())
                        messagebox.showinfo("Message", "Khách hàng chưa đăng ký thành viên!")
                        self.flag = 1
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def findByFace(self, cbbGender, cbbMembership, btAdd, btUpd, btDel):
        face_cascade = cv2.CascadeClassifier('D:\\vscode\\veterinary-clinic\\cafe_application\\src\\detection\\haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        customer_list = []
        self.diff_mean = dict()
        for customerID in self.customersID:
            for i in range(0,20):
                customer_list.append("face." + customerID + "." + str(i)+ ".jpg")

        self.countFailed = 0

        self.flag = 0
        while (self.flag == 0):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                for customer in customer_list:
                    customer_img = cv2.imread(customer, cv2.IMREAD_GRAYSCALE)
                    customer_img = cv2.resize(customer_img, (w, h))
                    diff = cv2.absdiff(roi_gray, customer_img)
                    mean = np.mean(diff)
                    name = customer
                    self.diff_mean[name] = mean

                min_key = min(self.diff_mean, key = self.diff_mean.get)
                if (self.diff_mean.get(min_key) <= 35):
                    self.customer = self.customerBLL.searchCustomers("CUSTOMER_ID = '" + min_key.split(".")[1] + "'")[0]
                    values = self.customer.__str__().split(" | ")
                    print(self.customer.__str__())
                    self.textfield[0].configure(state="normal")
                    self.textfield[0].delete(0, END)
                    self.textfield[0].insert(END, values[0])
                    self.textfield[0].configure(state="readonly")

                    self.textfield[1].delete(0, END)
                    self.textfield[1].insert(END, values[1])

                    cbbGender.configure(state="normal")
                    cbbGender.set(values[2])
                    cbbGender.configure(state="readonly")

                    self.textfield[2].delete(0, END)
                    self.textfield[2].insert(END, values[3])

                    self.textfield[3].delete(0, END)
                    self.textfield[3].insert(END, values[4])

                    cbbMembership.configure(state="normal")
                    cbbMembership.set(values[5])
                    cbbMembership.configure(state="readonly")

                    self.textfield[4].delete(0, END)
                    self.textfield[4].insert(END, values[6])

                    btAdd.configure(state="disabled")
                    btUpd.configure(state="normal")
                    btDel.configure(state="normal")
                    messagebox.showinfo("Message", "Nhận diện khách hàng thành viên thành công!")
                    self.flag = 1
                else:
                    print ("Khach hang chua dang ky thanh vien")
                    self.textfield[1].delete(0, END)
                    self.countFailed = self.countFailed + 1
                    if self.countFailed == 50:
                        messagebox.showinfo("Message", "Khách hàng chưa đăng ký thành viên!")
                        self.flag = 1
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

