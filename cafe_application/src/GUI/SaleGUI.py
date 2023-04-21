import re
from datetime import datetime
from threading import Thread
from tkinter import *
from tkinter import messagebox, ttk

from BLL.BillBLL import BillBLL
from BLL.BillDetailsBLL import BillDetailsBLL
from BLL.CustomerBLL import CustomerBLL
from BLL.ProductBLL import ProductBLL
from BLL.StaffBLL import StaffBLL
from detection.detection import Detection
from DTO.Bill import Bill
from DTO.BillDetails import BillDetails
from PIL import Image, ImageTk


class SaleGUI(Frame):
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
        self.staffsID = []
        for staff in self.staffBLL.getStaffList():
            self.staffsID.append(self.staffBLL.getValueByKey(staff, "STAFF_ID"))

        self.tableFrame = Frame(self.panel1, width=660, height=720, bg="#333333", highlightthickness=0, borderwidth=0)
        self.tableFrame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.tableFrame.pack_propagate(False)

        self.canvas = Canvas(self.tableFrame, bg="#FFFFFF", highlightthickness=0, borderwidth=0)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.canvas.bind_all('<MouseWheel>', self.on_wheelCanvas)
        # self.scrollbar = ttk.Scrollbar(self.tableFrame, orient="vertical", command=self.canvas.yview)
        # self.canvas.configure(xscrollcommand=self.scrollbar.set)
        # self.scrollbar.pack(side="right", fill="y", expand=False)

        self.frameInCanvas = Frame(self.canvas, bg="#FFFFFF", width=660, height=720)
        self.canvas.create_window((0,0), window=self.frameInCanvas, anchor="nw")
        self.frameInCanvas.bind("<Configure>", lambda event, canvas=self.canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        self.productBLL = ProductBLL()
        self.productsList = self.productBLL.getProductList()
        self.frameProducts = []
        self.img = []
        self.imgProduct = []
        self.productsName = []
        self.productsCost = []
        self.row = 0
        self.column = 0
        for product in self.productsList:
            self.frameProducts.append(Frame(self.frameInCanvas, width=180, height=250, bg="#ffffff"))
            self.img.append(ImageTk.PhotoImage(Image.open(product.getImage()).resize((175, 150), Image.ANTIALIAS)))

            self.imgProduct.append(Label(self.frameProducts[len(self.frameProducts)-1], image=self.img[len(self.img)-1], bg="#FFFFFF"))
            self.imgProduct[len(self.imgProduct)-1].grid(row = 0, column = 0)
            self.imgProduct[len(self.imgProduct)-1].bind('<Button-1>', self.on_panel_click)

            self.productsName.append(Label(self.frameProducts[len(self.frameProducts)-1], font=("open sans", 9, "bold"), text=product.getName() + "-" + product.getProductID(), fg="#000000", bg="#ffffff"))
            self.productsName[len(self.productsName)-1].grid(row = 1, column = 0)

            self.productsCost.append(Label(self.frameProducts[len(self.frameProducts)-1], font=("open sans", 10, "bold"), text=product.getCost(), fg="#000000", bg="#ffffff"))
            self.productsCost[len(self.productsCost)-1].grid(row = 2, column = 0)

            self.frameProducts[len(self.frameProducts)-1].grid(row=self.row, column=self.column, padx=20, pady=10)

            if self.column == 2:
                self.row += 1
                self.column = 0
            else:
                self.column += 1


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
                self.TextFieldsForm.append(Entry(self.pnlBillConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
                self.TextFieldsForm[len(self.TextFieldsForm)-1].bind("<KeyRelease>", self.updateCustomerName)

                self.row = self.row + 1
                self.column = 0

                self.nameLabel = Label(self.pnlBillConfiguration, text="NAME: ", fg="#000000", bg="#ffffff")
                self.nameLabel.grid(row=self.row, column=self.column, padx=20, pady=10)

                self.column = self.column + 1

                self.customerName = Entry(self.pnlBillConfiguration, fg="#000000", bg="#ffffff", width=30, state="disabled")
                self.customerName.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            elif self.columnNames[i] == "STAFF_ID":
                self.cbbStaffID = ttk.Combobox(self.pnlBillConfiguration, values=self.staffsID, width=27)
                self.cbbStaffID.configure(state="readonly")
                self.cbbStaffID.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "TOTAL":
                self.TextFieldsForm.append(Entry(self.pnlBillConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, "0")
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "DOPURCHASE":
                self.TextFieldsForm.append(Entry(self.pnlBillConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, datetime.strftime(datetime.today(), "%Y-%m-%d"))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            else:
                self.TextFieldsForm.append(Entry(self.pnlBillConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

        self.billDetails = Frame(self.panel2, bg="#FFFFFF", width=350, height=350, highlightthickness=0, borderwidth=0)
        self.billDetails.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.billDetails.pack_propagate(False)

        self.canvas1 = Canvas(self.billDetails, bg="#FFFFFF", highlightthickness=0, borderwidth=0)
        self.canvas1.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar1 = ttk.Scrollbar(self.canvas1, orient="vertical", command=self.canvas1.yview)
        self.canvas1.configure(xscrollcommand=self.scrollbar1.set)
        self.scrollbar1.pack(side="right", fill="y")


        self.frameInCanvas1 = Frame(self.canvas1, bg="#FFFFFF", width=660, height=720, highlightthickness=2, highlightbackground="black")
        self.canvas1.create_window((0, 0), window=self.frameInCanvas1, anchor="nw")
        self.frameInCanvas1.bind("<Configure>", lambda event, canvas=self.canvas1: canvas.configure(scrollregion=canvas.bbox("all")))

        self.labelBillDetails = []
        self.TextFieldsBillDetails = []
        self.row = 0
        self.column = 0

        self.mode = Frame(self.panel2, width=350, height=150, bg="#FFFFFF")
        self.mode.pack(side="bottom", padx=10, pady=10)

        self.btBuy = Button(self.mode, text="BUY", width=15, bg="#23a661", state="normal", command=self.buy)
        self.btBuy.grid(row=0, column=0, padx=20, pady=10, ipady=4)

        self.detection = Detection(self.TextFieldsForm)
        self.btDec = Button(self.mode, text="DETECTION", width=15, bg="#23a661", state="normal", command=self.dec)
        self.btDec.grid(row=0, column=1, padx=20, pady=10, ipady=4)


    def on_panel_click(self, event):
        self.message = messagebox.askyesno("Comfirm", "Bạn muốn mua sản phẩm này?")
        if self.message:
            index = self.imgProduct.index(event.widget)
            for item in  self.TextFieldsBillDetails:
                if item.get() == self.productsList[index].getProductID():
                    messagebox.showinfo("Message", "Sản phẩm đã có trong hoá đơn!")
                    return
            self.labelBillDetails.append(Label(self.frameInCanvas1, text="PRODUCT_ID: ", fg="#000000", bg="#ffffff"))
            self.labelBillDetails[len(self.labelBillDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10)

            self.column = self.column + 1

            self.TextFieldsBillDetails.append(Entry(self.frameInCanvas1, fg="#000000", bg="#ffffff", width=30))
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].insert(0, self.productsList[index].getProductID())
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].configure(state='readonly')
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

            self.labelBillDetails.append(Label(self.frameInCanvas1, text="QUANTITY: ", fg="#000000", bg="#ffffff"))
            self.labelBillDetails[len(self.labelBillDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10)

            self.column = self.column + 1

            self.TextFieldsBillDetails.append(Entry(self.frameInCanvas1, fg="#000000", bg="#ffffff", width=30))
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].insert(0, "1")
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].bind('<Return>', self.calculate)
            self.TextFieldsBillDetails[len(self.TextFieldsBillDetails)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

            self.calculate(event=None)

    def calculate(self, event):
        self.total = 0
        for i in range(0, len(self.TextFieldsBillDetails)):
            if i%2==0:
                product = self.productBLL.findProductsBy({"PRODUCT_ID": self.TextFieldsBillDetails[i].get()})[0]
            else:
                self.total += product.getCost() * int(self.TextFieldsBillDetails[i].get())
        self.TextFieldsForm[3].configure(state="normal")
        self.TextFieldsForm[3].delete(0, END)
        self.TextFieldsForm[3].insert(END, self.total)
        self.TextFieldsForm[3].configure(state="readonly")

    def buy(self):
        dop = datetime.strptime(self.TextFieldsForm[2].get(), "%Y-%m-%d").date()
        name = ''
        if self.TextFieldsForm[1].get() == '':
            name = 'CUS000'
        else:
            name = self.TextFieldsForm[1].get()
        self.billBLL.addBill(Bill(self.TextFieldsForm[0].get(), name, self.cbbStaffID.get(), dop, float(0), False))
        for i in range(0, len(self.TextFieldsBillDetails)):
            if i % 2 == 0:
                product = self.productBLL.findProductsBy({"PRODUCT_ID": self.TextFieldsBillDetails[i].get()})[0]
            else:
                self.billDetailsBLL.addBillDetails(BillDetails(self.TextFieldsForm[0].get(), product.getProductID(), int(self.TextFieldsBillDetails[i].get())))
        self.ref()

    def dec(self):
        thread = Thread(target=self.detection.detect(self.customerName))
        thread.start()

    def on_wheelCanvas(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta/120)), "units")

    def updateCustomerName(self, event):
        text = event.widget.get()
        if re.match(r'^CUS\d{3}$', text):
            customers = CustomerBLL().findCustomersBy({"CUSTOMER_ID": text})
            if len(customers) > 0:
                self.customerName.configure(state='normal')
                self.customerName.delete(0, END)
                self.customerName.insert(END, customers[0].getName())
                self.customerName.configure(state='disabled')
        else:
            self.customerName.configure(state='normal')
            self.customerName.delete(0, END)
            self.customerName.configure(state='disabled')



    def ref(self):
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.billBLL.getAutoID())
        self.TextFieldsForm[0].configure(state="readonly")
        self.TextFieldsForm[1].delete(0, END)
        self.TextFieldsForm[2].configure(state="normal")
        self.TextFieldsForm[2].delete(0, END)
        self.TextFieldsForm[2].insert(0, datetime.strftime(datetime.today(), "%Y-%m-%d"))
        self.TextFieldsForm[3].configure(state="readonly")
        self.TextFieldsForm[3].configure(state="normal")
        self.TextFieldsForm[3].delete(0, END)
        self.TextFieldsForm[3].insert(END, "0")
        self.TextFieldsForm[3].configure(state="readonly")

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

