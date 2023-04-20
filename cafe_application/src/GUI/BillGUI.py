from datetime import datetime
from threading import Thread
from tkinter import *
from tkinter import ttk

from BLL.BillBLL import BillBLL
from BLL.BillDetailsBLL import BillDetailsBLL
from BLL.CustomerBLL import CustomerBLL
from BLL.StaffBLL import StaffBLL
from detection.detection import Detection
from DTO.Bill import Bill


class BillGUI(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="blue", width=200, height=720)
        self.billBLL = BillBLL()
        self.billDetailsBLL = BillDetailsBLL()
        self.init_components()


    def init_components(self):
        self.panel1 = Frame(self, bg="#333333", width=680)
        self.panel1.pack(side="left", fill="y")

        self.panel2 = Frame(self, bg="#FFFFFF", width=360)
        self.panel2.pack(side="right", fill="y")

        self.columnNames = self.billBLL.getBillDAL().getColumnNames()
        self.staffBLL = StaffBLL()
        self.customerBLL = CustomerBLL()
        self.staffsID = []
        self.customersID = []
        for staff in self.staffBLL.getStaffList():
            self.staffsID.append(self.staffBLL.getValueByKey(staff, "STAFF_ID"))
        for customer in self.customerBLL.getCustomerList():
            self.customersID.append(self.customerBLL.getValueByKey(customer, "CUSTOMER_ID"))

        self.tableFrame = Frame(self.panel1, width=660, height=720, bg="#333333", highlightthickness=0, borderwidth=0)
        self.tableFrame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.tableFrame.pack_propagate(False)

        self.table = ttk.Treeview(self.tableFrame, columns=self.columnNames[0:len(self.columnNames)-1], show="headings")
        self.table.heading("0", text="BILL_ID")
        self.table.heading("1", text="CUSTOMER_ID")
        self.table.heading("2", text="STAFF_ID")
        self.table.heading("3", text="DOPURCHASE")
        self.table.heading("4", text="TOTAL")
        self.data = self.billBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)
        self.table.pack(fill=BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tableFrame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="bottom", fill="x")

        self.table.bind('<<TreeviewSelect>>', self.showDetailsBill)

        self.pnlBillConfiguration = Frame(self.panel2, bg="#FFFFFF", width=350)
        self.pnlBillConfiguration.pack(padx=10, pady=10)

        self.labelForm = []
        self.TextFieldsForm = []
        self.row = 0
        self.column = 0
        for i in range(0, len(self.columnNames)-1):
            self.labelForm.append(Label(self.pnlBillConfiguration, text=self.columnNames[i] + ": ", fg="#000000", bg="#ffffff"))
            self.labelForm[i].grid(row=self.row, column=self.column, padx=20, pady=10)
            self.column = self.column + 1
            if self.columnNames[i] == "BILL_ID":
                self.TextFieldsForm.append(Entry(self.pnlBillConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, self.billBLL.getAutoID())
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "CUSTOMER_ID":
                self.cbbCustomerID = ttk.Combobox(self.pnlBillConfiguration, values=self.customersID, width=27)
                self.cbbCustomerID.configure(state="readonly")
                self.cbbCustomerID.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "STAFF_ID":
                self.cbbStaffID = ttk.Combobox(self.pnlBillConfiguration, values=self.staffsID, width=27)
                self.cbbStaffID.configure(state="readonly")
                self.cbbStaffID.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "TOTAL":
                self.TextFieldsForm.append(Entry(self.pnlBillConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, "0")
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            else:
                self.TextFieldsForm.append(Entry(self.pnlBillConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

        self.billDetails = Frame(self.panel2, bg="#FFFFFF", width=350, height=300, highlightthickness=0, borderwidth=0)
        self.billDetails.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.billDetails.pack_propagate(False)

        self.canvas1 = Canvas(self.billDetails, bg="#FFFFFF", highlightthickness=0, borderwidth=0)
        self.canvas1.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar1 = ttk.Scrollbar(self.canvas1, orient="vertical", command=self.canvas1.yview)
        self.canvas1.configure(xscrollcommand=self.scrollbar1.set)
        self.scrollbar1.pack(side="right", fill="y")

        self.frameInCanvas1 = Frame(self.canvas1, bg="#FFFFFF", width=660, height=720, highlightthickness=2, highlightbackground="black")
        self.canvas1.create_window((0,0), window=self.frameInCanvas1, anchor="nw")
        self.frameInCanvas1.bind("<Configure>", lambda event, canvas=self.canvas1: canvas.configure(scrollregion=canvas.bbox("all")))

        self.mode = Frame(self.panel2, width=350, height=250, bg="#FFFFFF")
        self.mode.pack(side="bottom", padx=10, pady=10)

        self.btUpd = Button(self.mode, text="UPDATE", width=15, bg="#23a661", state="disabled", command=self.upd)
        self.btUpd.grid(row=0, column=0, padx=20, pady=10, ipady=4)

        self.btDel = Button(self.mode, text="DELETE", width=15, bg="#23a661", state="disabled", command=self.dele)
        self.btDel.grid(row=0, column=1, padx=20, pady=10, ipady=4)

        self.btRef = Button(self.mode, text="Refresh", width=15, bg="#23a661", state="normal", command=self.ref)
        self.btRef.grid(row=1, column=0, padx=20, pady=10, ipady=4)

        self.detection = Detection(self.TextFieldsForm)
        self.btDec = Button(self.mode, text="DETECTION", width=15, bg="#23a661", state="normal", command=self.dec)
        self.btDec.grid(row=1, column=1, padx=20, pady=10, ipady=4)


    def showDetailsBill(self, event):
        for row in self.table.selection():
            item = self.table.item(row)
            values = item["values"]

            self.TextFieldsForm[0].configure(state="normal")
            self.TextFieldsForm[0].delete(0, END)
            self.TextFieldsForm[0].insert(END, values[0])
            self.TextFieldsForm[0].configure(state="readonly")

            self.cbbCustomerID.configure(state="normal")
            self.cbbCustomerID.set(values[1])
            self.cbbCustomerID.configure(state="readonly")

            self.cbbStaffID.configure(state="normal")
            self.cbbStaffID.set(values[2])
            self.cbbStaffID.configure(state="readonly")

            self.TextFieldsForm[1].delete(0, END)
            self.TextFieldsForm[1].insert(END, values[3])

            self.TextFieldsForm[2].configure(state="normal")
            self.TextFieldsForm[2].delete(0, END)
            self.TextFieldsForm[2].insert(END, values[4])
            self.TextFieldsForm[2].configure(state="readonly")

        self.frameInCanvas1.destroy()
        self.frameInCanvas1 = Frame(self.canvas1, bg="#FFFFFF", width=660, height=720, highlightthickness=2, highlightbackground="black")
        self.canvas1.create_window((0,0), window=self.frameInCanvas1, anchor="nw")
        self.frameInCanvas1.bind("<Configure>", lambda event, canvas=self.canvas1: canvas.configure(scrollregion=canvas.bbox("all")))

        self.labelBillDetails = []
        self.TextFieldsBillDetails = []
        self.row = 0
        self.column = 0

        self.billDetailsList = self.billDetailsBLL.findBillDetailsBy({"BILL_ID": self.TextFieldsForm[0].get()})
        for billDetails in self.billDetailsList:

            self.labelBillDetails.append(Label(self.frameInCanvas1, text="PRODUCT_ID: ", fg="#000000", bg="#ffffff"))
            self.labelBillDetails[len(self.labelBillDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10)

            self.column = self.column + 1

            self.TextFieldsBillDetails.append(Entry(self.frameInCanvas1, fg="#000000", bg="#ffffff", width=30))
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].insert(0, billDetails.getProductID())
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].configure(state='readonly')
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

            self.labelBillDetails.append(Label(self.frameInCanvas1, text="QUANTITY: ", fg="#000000", bg="#ffffff"))
            self.labelBillDetails[len(self.labelBillDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10)

            self.column = self.column + 1

            self.TextFieldsBillDetails.append(Entry(self.frameInCanvas1, fg="#000000", bg="#ffffff", width=30))
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].insert(0, billDetails.getQuantity())
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].configure(state='readonly')
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

            self.btUpd.configure(state="normal")
            self.btDel.configure(state="normal")

    def loadTable(self, data):
        for item in self.table.get_children():
            self.table.delete(item)
        for row in data:
            self.table.insert('', END, values = row)

    def upd(self):
        dop = datetime.strptime(self.TextFieldsForm[1].get(), "%Y-%m-%d").date()
        self.newBill = Bill(self.TextFieldsForm[0].get(), self.cbbCustomerID.get(), self.cbbStaffID.get(), dop, float(self.TextFieldsForm[2].get()), False)
        self.billBLL.updateBill(self.newBill)
        self.loadTable(self.billBLL.getData())

    def dele(self):
        self.billBLL.deleteBill(Bill(billID = self.TextFieldsForm[0].get()))
        self.ref()

    def dec(self):
        self.ref()
        thread = Thread(target=self.detection.findBills(self.table))
        thread.start()
    def ref(self):
        self.loadTable(self.billBLL.getData())
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.billBLL.getAutoID())
        self.TextFieldsForm[0].configure(state="readonly")
        self.TextFieldsForm[1].delete(0, END)
        self.TextFieldsForm[2].configure(state="normal")
        self.TextFieldsForm[2].delete(0, END)
        self.TextFieldsForm[2].insert(END, "0")
        self.TextFieldsForm[2].configure(state="readonly")

        self.cbbCustomerID.configure(state="normal")
        self.cbbCustomerID.delete(0, END)
        self.cbbCustomerID.configure(state="readonly")

        self.cbbStaffID.configure(state="normal")
        self.cbbStaffID.delete(0, END)
        self.cbbStaffID.configure(state="readonly")

        self.frameInCanvas1.destroy()
        self.frameInCanvas1 = Frame(self.canvas1, bg="#FFFFFF", width=660, height=720, highlightthickness=2, highlightbackground="black")
        self.canvas1.create_window((0,0), window=self.frameInCanvas1, anchor="nw")
        self.frameInCanvas1.bind("<Configure>", lambda event, canvas=self.canvas1: canvas.configure(scrollregion=canvas.bbox("all")))

        self.labelBillDetails = []
        self.TextFieldsBillDetails = []
        self.row = 0
        self.column = 0

        self.btUpd.configure(state="disabled")
        self.btDel.configure(state="disabled")
