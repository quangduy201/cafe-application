from tkinter import *
from tkinter import ttk
from BLL.CustomerBLL import CustomerBLL
from DTO.Customer import Customer
from datetime import datetime
from detection.record import Record
from detection.detection import Detection
from threading import Thread
class CustomerGUI(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="blue", width=200, height=720)
        self.customerBLL = CustomerBLL()
        self.init_components()

    def init_components(self):
        self.panel1 = Frame(self, bg="#333333", width=680)
        self.panel1.pack(side="left", fill="y")

        self.panel2 = Frame(self, bg="#FFFFFF", width=360)
        self.panel2.pack(side="right", fill="y")

        self.columnNames = self.customerBLL.getCustomerDAL().getColumnNames()

        self.search = Frame(self.panel1, width=660, height=40, bg="#FFFFFF", highlightthickness=0, borderwidth=0)
        self.search.pack(padx=10, pady=10, fill=BOTH, expand=True)

        self.tableFrame = Frame(self.panel1, width=660, height=650, bg="#333333", highlightthickness=0, borderwidth=0)
        self.tableFrame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.tableFrame.pack_propagate(False)

        self.table = ttk.Treeview(self.tableFrame, columns=self.columnNames[0:len(self.columnNames)-1], show="headings")
        self.table.heading("0", text="CUSTOMER_ID")
        self.table.heading("1", text="NAME")
        self.table.heading("2", text="GENDER")
        self.table.heading("3", text="DOB")
        self.table.heading("4", text="PHONE")
        self.table.heading("5", text="MEMBERSHIP")
        self.table.heading("6", text="DOSUP")
        self.data = self.customerBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)
        self.table.pack(fill=BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tableFrame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="bottom", fill="x")

        self.table.bind('<<TreeviewSelect>>', self.showDetailsCustomer)

        self.pnlCustomerConfiguration = Frame(self.panel2, bg="#FFFFFF", width=350)
        self.pnlCustomerConfiguration.pack(padx=10, pady=10)

        self.labelForm = []
        self.TextFieldsForm = []
        self.row = 0
        self.column = 0
        for i in range(0, len(self.columnNames)-1):
            self.labelForm.append(Label(self.pnlCustomerConfiguration, text=self.columnNames[i] + ": ", fg="#000000", bg="#ffffff"))
            self.labelForm[i].grid(row=self.row, column=self.column, padx=20, pady=10)
            self.column = self.column + 1
            if self.columnNames[i] == "CUSTOMER_ID":
                self.TextFieldsForm.append(Entry(self.pnlCustomerConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, self.customerBLL.getAutoID())
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "GENDER":
                self.cbbGender = ttk.Combobox(self.pnlCustomerConfiguration, values=["Nam", "Nữ"], width=27)
                self.cbbGender.configure(state="readonly")
                self.cbbGender.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "MEMBERSHIP":
                self.cbbMembership = ttk.Combobox(self.pnlCustomerConfiguration, values=["Có", "Không"], width=27)
                self.cbbMembership.bind("<<ComboboxSelected>>", self.active)
                self.cbbMembership.configure(state="readonly")
                self.cbbMembership.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            else:
                self.TextFieldsForm.append(Entry(self.pnlCustomerConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row +1
            self.column = 0

        self.detection = Detection(self.TextFieldsForm)
        self.btDetection = Button(self.search, text="Tìm kiếm bằng gương mặt", width=25, bg="#AFD1DF", command=self.findByFace)
        self.btDetection.pack(pady=5)


        self.btRecord = Button(self.pnlCustomerConfiguration, text="Đăng ký gương mặt", width=25, bg="#AFD1DF", command=self.sinupFace, state="disabled")
        self.btRecord.grid(row=self.row, column=1, padx=20, pady=10, ipady=4)

        self.showImage = Frame(self.panel2, width=350, height=200, bg="#FFFFFF")
        self.showImage.pack(padx=10, pady=0)

        self.mode = Frame(self.panel2, width=350, height=150, bg="#ffffff")
        self.mode.pack(side="bottom", padx=10, pady=10)

        self.btAdd = Button(self.mode, text="ADD", width=15, bg="#23a661", state="normal", command=self.add)
        self.btAdd.grid(row=0, column=0, padx=20, pady=10, ipady=4)

        self.btUpd = Button(self.mode, text="UPDATE", width=15, bg="#23a661", state="disabled", command=self.upd)
        self.btUpd.grid(row=0, column=1, padx=20, pady=10, ipady=4)

        self.btDel = Button(self.mode, text="DELETE", width=15, bg="#23a661", state="disabled", command=self.dele)
        self.btDel.grid(row=1, column=0, padx=20, pady=10, ipady=4)

        self.btRef = Button(self.mode, text="Refresh", width=15, bg="#23a661", state="normal", command=self.ref)
        self.btRef.grid(row=1, column=1, padx=20, pady=10, ipady=4)

    def findByFace(self):
        thread = Thread(target=self.detection.findByFace(self.cbbGender, self.cbbMembership, self.btAdd, self.btUpd, self.btDel))
        thread.start()

    def active(self, event):
        if event.widget.get() == "Có":
            self.btRecord.configure(state="normal")
        else:
            self.btRecord.configure(state="disabled")

    def sinupFace(self):
        self.record = Record(self.TextFieldsForm[0].get())
        thread = Thread(target=self.record.recording)
        thread.start()

    def showDetailsCustomer(self, event):
        for row in self.table.selection():
            item = self.table.item(row)
            values = item["values"]

            self.TextFieldsForm[0].configure(state="normal")
            self.TextFieldsForm[0].delete(0, END)
            self.TextFieldsForm[0].insert(END, values[0])
            self.TextFieldsForm[0].configure(state="readonly")

            self.TextFieldsForm[1].delete(0, END)
            self.TextFieldsForm[1].insert(END, values[1])

            self.cbbGender.configure(state="normal")
            self.cbbGender.set(values[2])
            self.cbbGender.configure(state="readonly")

            self.TextFieldsForm[2].delete(0, END)
            self.TextFieldsForm[2].insert(END, values[3])

            self.TextFieldsForm[3].delete(0, END)
            self.TextFieldsForm[3].insert(END, values[4])

            self.cbbMembership.configure(state="normal")
            self.cbbMembership.set(values[5])
            self.cbbMembership.configure(state="readonly")

            self.TextFieldsForm[4].delete(0, END)
            self.TextFieldsForm[4].insert(END, values[6])

            self.btAdd.configure(state="disabled")
            self.btUpd.configure(state="normal")
            self.btDel.configure(state="normal")

    def loadTable(self):
        for item in self.table.get_children():
            self.table.delete(item)
        self.data = self.customerBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)

    def add(self):
        gender = True if self.cbbGender.get() == "Nam" else False
        member = True if self.cbbMembership.get() == "Có" else False
        dob = datetime.strptime(self.TextFieldsForm[2].get(), "%Y-%m-%d").date()
        dos = datetime.strptime(self.TextFieldsForm[4].get(), "%Y-%m-%d").date()
        self.newCustomer = Customer(self.TextFieldsForm[0].get(), self.TextFieldsForm[1].get(), gender, dob, self.TextFieldsForm[3].get(), member, dos, False)
        self.customerBLL.addCustomer(self.newCustomer)
        self.ref()

    def upd(self):
        gender = True if self.cbbGender.get() == "Nam" else False
        member = True if self.cbbMembership.get() == "Có" else False
        dob = datetime.strptime(self.TextFieldsForm[2].get(), "%Y-%m-%d").date()
        dos = datetime.strptime(self.TextFieldsForm[4].get(), "%Y-%m-%d").date()
        self.newCustomer = Customer(self.TextFieldsForm[0].get(), self.TextFieldsForm[1].get(), gender, dob, self.TextFieldsForm[3].get(), member, dos, False)
        self.customerBLL.updateCustomer(self.newCustomer)
        self.loadTable()

    def dele(self):
        self.customerBLL.deleteCustomer(Customer(customerID = self.TextFieldsForm[0].get()))
        self.ref()

    def ref(self):
        self.loadTable()
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.customerBLL.getAutoID())
        self.TextFieldsForm[0].configure(state="readonly")
        for i in range(1, len(self.TextFieldsForm)):
            self.TextFieldsForm[i].delete(0, END)

        self.cbbGender.configure(state="normal")
        self.cbbGender.delete(0, END)
        self.cbbGender.configure(state="readonly")
        self.cbbMembership.configure(state="normal")
        self.cbbMembership.delete(0, END)
        self.cbbMembership.configure(state="readonly")
        self.btAdd.configure(state="normal")
        self.btUpd.configure(state="disabled")
        self.btDel.configure(state="disabled")




