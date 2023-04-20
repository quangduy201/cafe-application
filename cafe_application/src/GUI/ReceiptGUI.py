from datetime import datetime
from tkinter import *
from tkinter import ttk

from BLL.IngredientBLL import IngredientBLL
from BLL.ReceiptBLL import ReceiptBLL
from BLL.ReceiptDetailsBLL import ReceiptDetailsBLL
from BLL.StaffBLL import StaffBLL
from BLL.SupplierBLL import SupplierBLL
from DTO.Receipt import Receipt
from DTO.ReceiptDetails import ReceiptDetails


class ReceiptGUI(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="blue", width=200, height=720)
        self.receiptBLL = ReceiptBLL()
        self.receiptDetailsBLL = ReceiptDetailsBLL()
        self.init_components()

    def init_components(self):
        self.panel1 = Frame(self, bg="#333333", width=680)
        self.panel1.pack(side="left", fill="y")

        self.panel2 = Frame(self, bg="#FFFFFF", width=360)
        self.panel2.pack(side="right", fill="y")

        self.columnNames = self.receiptBLL.getReceiptDAL().getColumnNames()
        self.staffBLL = StaffBLL()
        self.supplierBLL = SupplierBLL()
        self.ingredientBLL = IngredientBLL()
        self.staffsID = []
        self.suppliersID = []
        self.ingredientsID = []
        for staff in self.staffBLL.getStaffList():
            self.staffsID.append(self.staffBLL.getValueByKey(staff, "STAFF_ID"))
        for supplier in self.supplierBLL.getSupplierList():
            self.suppliersID.append(self.supplierBLL.getValueByKey(supplier, "SUPPLIER_ID"))
        for ingredient in self.ingredientBLL.getIngredientList():
            self.ingredientsID.append(self.ingredientBLL.getValueByKey(ingredient, "INGREDIENT_ID"))

        self.tableFrame = Frame(self.panel1, width=660, height=720, bg="#333333", highlightthickness=0, borderwidth=0)
        self.tableFrame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.tableFrame.pack_propagate(False)

        self.table = ttk.Treeview(self.tableFrame, columns=self.columnNames[0:len(self.columnNames)-1], show="headings")
        self.table.heading("0", text="RECEIPT_ID")
        self.table.heading("1", text="STAFF_ID")
        self.table.heading("2", text="DOR")
        self.table.heading("3", text="GRAND_TOTAL")
        self.data = self.receiptBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)
        self.table.pack(fill=BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tableFrame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="bottom", fill="x")

        self.table.bind('<<TreeviewSelect>>', self.showDetailsReceipt)

        self.pnlReceiptConfiguration = Frame(self.panel2, bg="#FFFFFF", width=350)
        self.pnlReceiptConfiguration.pack(padx=10, pady=10)

        self.labelForm = []
        self.TextFieldsForm = []
        self.row = 0
        self.column = 0
        for i in range(0, len(self.columnNames)-1):
            self.labelForm.append(Label(self.pnlReceiptConfiguration, text=self.columnNames[i] + ": ", fg="#000000", bg="#ffffff"))
            self.labelForm[i].grid(row=self.row, column=self.column, padx=20, pady=10)
            self.column = self.column + 1
            if self.columnNames[i] == "RECEIPT_ID":
                self.TextFieldsForm.append(Entry(self.pnlReceiptConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, self.receiptBLL.getAutoID())
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "STAFF_ID":
                self.cbbStaffID = ttk.Combobox(self.pnlReceiptConfiguration, values=self.staffsID, width=27)
                self.cbbStaffID.configure(state="readonly")
                self.cbbStaffID.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "DOR":
                self.TextFieldsForm.append(Entry(self.pnlReceiptConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, datetime.strftime(datetime.today(), "%Y-%m-%d"))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "GRAND_TOTAL":
                self.TextFieldsForm.append(Entry(self.pnlReceiptConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, "0")
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            else:
                self.TextFieldsForm.append(Entry(self.pnlReceiptConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

        self.receiptDetails = Frame(self.panel2, bg="#FFFFFF", width=350, height=300, highlightthickness=0, borderwidth=0)
        self.receiptDetails.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.receiptDetails.pack_propagate(False)

        self.canvas1 = Canvas(self.receiptDetails, bg="#FFFFFF", highlightthickness=0, borderwidth=0)
        self.canvas1.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar1 = ttk.Scrollbar(self.receiptDetails, orient="vertical", command=self.canvas1.yview)
        self.canvas1.configure(xscrollcommand=self.scrollbar1.set)
        self.scrollbar1.pack(side="right", fill="y")

        self.frameInCanvas1 = Frame(self.canvas1, bg="#FFFFFF", width=660, height=720, highlightthickness=2, highlightbackground="black")
        self.canvas1.create_window((0,0), window=self.frameInCanvas1, anchor="nw")
        self.frameInCanvas1.bind("<Configure>", lambda event, canvas=self.canvas1: canvas.configure(scrollregion=canvas.bbox("all")))

        self.mode = Frame(self.panel2, width=350, height=250, bg="#FFFFFF")
        self.mode.pack(side="bottom", padx=10, pady=10)

        self.btAdd = Button(self.mode, text="ADD", width=15, bg="#23a661", state="normal", command=self.add)
        self.btAdd.grid(row=0, column=0, padx=20, pady=10, ipady=4)

        self.btUpd = Button(self.mode, text="UPDATE", width=15, bg="#23a661", state="disabled", command=self.upd)
        self.btUpd.grid(row=0, column=1, padx=20, pady=10, ipady=4)

        self.btDel = Button(self.mode, text="DELETE", width=15, bg="#23a661", state="disabled", command=self.dele)
        self.btDel.grid(row=1, column=0, padx=20, pady=10, ipady=4)

        self.btRef = Button(self.mode, text="Refresh", width=15, bg="#23a661", state="normal", command=self.ref)
        self.btRef.grid(row=1, column=1, padx=20, pady=10, ipady=4)


    def showDetailsReceipt(self, event):
        for row in self.table.selection():
            item = self.table.item(row)
            values = item["values"]

            self.TextFieldsForm[0].configure(state="normal")
            self.TextFieldsForm[0].delete(0, END)
            self.TextFieldsForm[0].insert(END, values[0])
            self.TextFieldsForm[0].configure(state="readonly")

            self.cbbStaffID.configure(state="normal")
            self.cbbStaffID.set(values[1])
            self.cbbStaffID.configure(state="readonly")

            self.TextFieldsForm[1].configure(state="normal")
            self.TextFieldsForm[1].delete(0, END)
            self.TextFieldsForm[1].insert(0, values[2])
            self.TextFieldsForm[1].configure(state="readonly")

            self.TextFieldsForm[2].configure(state="normal")
            self.TextFieldsForm[2].delete(0, END)
            self.TextFieldsForm[2].insert(END, values[3])
            self.TextFieldsForm[2].configure(state="readonly")

        self.frameInCanvas1.destroy()
        self.frameInCanvas1 = Frame(self.canvas1, bg="#FFFFFF", width=660, height=720, highlightthickness=2, highlightbackground="black")
        self.canvas1.create_window((0,0), window=self.frameInCanvas1, anchor="nw")
        self.frameInCanvas1.bind("<Configure>", lambda event, canvas=self.canvas1: canvas.configure(scrollregion=canvas.bbox("all")))

        self.labelReceiptDetails = []
        self.TextFieldsReceiptDetails = []
        self.cbbReceiptDetails = []
        self.row = 0
        self.column = 0

        self.receiptDetailsList = self.receiptDetailsBLL.findReceiptDetailsBy({"RECEIPT_ID": self.TextFieldsForm[0].get()})
        for receiptDetails in self.receiptDetailsList:

            self.labelReceiptDetails.append(Label(self.frameInCanvas1, text="INGREDIENT_ID: ", fg="#000000", bg="#ffffff"))
            self.labelReceiptDetails[len(self.labelReceiptDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10)

            self.column = self.column + 1

            self.cbbReceiptDetails.append(ttk.Combobox(self.frameInCanvas1, values=self.ingredientsID, width=27))
            self.cbbReceiptDetails[len(self.cbbReceiptDetails)-1].set(receiptDetails.getIngredientID())
            self.cbbReceiptDetails[len(self.cbbReceiptDetails)-1].configure(state='disabled')
            self.cbbReceiptDetails[len(self.cbbReceiptDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

            self.labelReceiptDetails.append(Label(self.frameInCanvas1, text="QUANTITY: ", fg="#000000", bg="#ffffff"))
            self.labelReceiptDetails[len(self.labelReceiptDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10)

            self.column = self.column + 1

            self.TextFieldsReceiptDetails.append(Entry(self.frameInCanvas1, fg="#000000", bg="#ffffff", width=30))
            self.TextFieldsReceiptDetails[len(self.TextFieldsReceiptDetails)-1].insert(0, receiptDetails.getQuantity())
            self.TextFieldsReceiptDetails[len(self.TextFieldsReceiptDetails)-1].configure(state='disabled')
            self.TextFieldsReceiptDetails[len(self.TextFieldsReceiptDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

            self.labelReceiptDetails.append(Label(self.frameInCanvas1, text="SUPPLIER_ID: ", fg="#000000", bg="#ffffff"))
            self.labelReceiptDetails[len(self.labelReceiptDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10)

            self.column = self.column + 1

            self.cbbReceiptDetails.append(ttk.Combobox(self.frameInCanvas1, values=self.suppliersID, width=27))
            self.cbbReceiptDetails[len(self.cbbReceiptDetails)-1].insert(0, receiptDetails.getSupplierID())
            self.cbbReceiptDetails[len(self.cbbReceiptDetails)-1].configure(state='disabled')
            self.cbbReceiptDetails[len(self.cbbReceiptDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            self.row = self.row + 1
            self.column = 0

            self.btAdd.configure(state="disabled")
            self.btUpd.configure(state="normal")
            self.btDel.configure(state="normal")

    def loadTable(self):
        for item in self.table.get_children():
            self.table.delete(item)
        self.data = self.receiptBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)

    def add(self):
        dor = datetime.strptime(self.TextFieldsForm[1].get(), "%Y-%m-%d").date()
        self.newReceipt = Receipt(self.TextFieldsForm[0].get(), self.cbbStaffID.get(), dor, float(self.TextFieldsForm[2].get()), False)
        self.receiptBLL.addReceipt(self.newReceipt)
        self.ref()

    def upd(self):
        dor = datetime.strptime(self.TextFieldsForm[1].get(), "%Y-%m-%d").date()
        self.newReceipt = Receipt(self.TextFieldsForm[0].get(), self.cbbStaffID.get(), dor, float(self.TextFieldsForm[2].get()), False)
        self.receiptBLL.updateReceipt(self.newReceipt)
        self.loadTable()

    def dele(self):
        self.receiptBLL.deleteReceipt(Receipt(receiptID = self.TextFieldsForm[0].get()))
        self.ref()

    def ref(self):
        self.loadTable()
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.receiptBLL.getAutoID())
        self.TextFieldsForm[0].configure(state="readonly")
        self.TextFieldsForm[1].configure(state="normal")
        self.TextFieldsForm[1].delete(0, END)
        self.TextFieldsForm[1].insert(0, datetime.strftime(datetime.today(), "%Y-%m-%d"))
        self.TextFieldsForm[1].configure(state="readonly")
        self.TextFieldsForm[2].configure(state="normal")
        self.TextFieldsForm[2].delete(0, END)
        self.TextFieldsForm[2].insert(END, "0")
        self.TextFieldsForm[2].configure(state="readonly")

        self.cbbStaffID.configure(state="normal")
        self.cbbStaffID.delete(0, END)
        self.cbbStaffID.configure(state="readonly")

        self.frameInCanvas1.destroy()
        self.frameInCanvas1 = Frame(self.canvas1, bg="#FFFFFF", width=660, height=720, highlightthickness=2, highlightbackground="black")
        self.canvas1.create_window((0,0), window=self.frameInCanvas1, anchor="nw")
        self.frameInCanvas1.bind("<Configure>", lambda event, canvas=self.canvas1: canvas.configure(scrollregion=canvas.bbox("all")))

        self.labelReceiptDetails = []
        self.TextFieldsReceiptDetails = []
        self.cbbReceiptDetails = []
        self.row = 0
        self.column = 0

        self.btAdd.configure(state="normal")
        self.btUpd.configure(state="disabled")
        self.btDel.configure(state="disabled")
