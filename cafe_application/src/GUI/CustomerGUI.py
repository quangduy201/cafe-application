from tkinter import *
from tkinter import ttk
from BLL.CustomerBLL import CustomerBLL
from DTO.Customer import Customer
from datetime import datetime

class CustomerGUI(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="blue", width=200, height=720)
        self.customerBLL = CustomerBLL()
        self.init_components()
        self.run()

    def init_components(self):
        self.panel1 = Frame(self, bg="#333333", width=680)
        self.panel1.pack(side="left", fill="y")

        self.panel2 = Frame(self, bg="#FFFFFF", width=360)
        self.panel2.pack(side="right", fill="y")

        self.columnNames = self.customerBLL.getCustomerDAL().getColumnNames()

        self.tableFrame = Frame(self.panel1, width=660, height=450, bg="#333333", highlightthickness=0, borderwidth=0)
        self.tableFrame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.tableFrame.pack_propagate(False)

        self.menu = Frame(self.panel1, width=660, height=200, bg="#333333", highlightthickness=0, borderwidth=0)
        self.menu.pack(padx=10, pady=0, fill=BOTH, expand=True)
        self.menu.pack_propagate(False)

        self.toolBar = Frame(self.panel1, bg="#FFFFFF", width=660, height=60)
        self.toolBar.pack(padx=10, pady=10, fill=BOTH, expand=True)

        self.textArea = Text(self.tableFrame, font=("open sans", 12), highlightthickness=0, borderwidth=0)
        self.textArea.pack(fill=BOTH, expand=True)
        self.scrollbar = Scrollbar(self.tableFrame)
        self.scrollbar.pack(side=RIGHT, fill="x", expand=True)
        self.textArea.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textArea.yview)
        self.textArea.configure(state='disabled')

        self.textArea1 = Text(self.menu, font=("open sans", 12), highlightthickness=0, borderwidth=0)
        self.textArea1.pack(fill=BOTH, expand=True)
        self.scrollbar1 = Scrollbar(self.menu)
        self.scrollbar1.pack(side=RIGHT, fill="x", expand=True)
        self.textArea1.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.textArea1.yview)
        self.textArea1.configure(state='disabled')

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
                self.cbbMembership.configure(state="readonly")
                self.cbbMembership.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            else:
                self.TextFieldsForm.append(Entry(self.pnlCustomerConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row +1
            self.column = 0

        self.showImage = Frame(self.panel2, width=350, height=250, bg="#FFFFFF")
        self.showImage.pack(padx=10, pady=0)

        self.mode = Frame(self.panel2, width=350, height=150, bg="#ffffff")
        self.mode.pack(side="bottom", padx=10, pady=10)

        self.btAdd = Button(self.mode, text="ADD", width=25, bg="#23a661", state="disabled", command=self.add)
        self.btAdd.grid(row=0, column=0, padx=20, pady=10, ipady=4)

        self.btUpd = Button(self.mode, text="UPDATE", width=25, bg="#23a661", state="disabled", command=self.upd)
        self.btUpd.grid(row=1, column=0, padx=20, pady=10, ipady=4)

        self.input = Entry(self.toolBar, fg="#000000", bg="#ffffff", width=30)
        self.input.grid(row=0, column=0, padx=20, pady=10, ipady=4)
    def run(self):
        self.menu = 'Choose one of these options:\n' \
            + '1. View customer details .\n' \
            + '2. Add new customer.\n' \
            + '3. Edit customer.\n' \
            + '4. Delete customer.\n'

        self.selection = None

        self.textArea.configure(state='normal')
        self.textArea.delete(1.0, END)

        self.reloadTable()

        self.textArea1.configure(state="normal")
        self.textArea1.delete(1.0, END)
        self.textArea1.insert(END, self.menu)
        self.textArea1.configure(state="disabled")

        self.input.bind("<Return>", self.selection_Menu)


    def selection_Menu(self, event):
        self.selection = self.input.get()
        self.input.delete(0, END)
        if self.selection == "1":
            self.menuViewDetails = 'Choose one of these customers ID.\n' \
                + '(Press 0 to back).\n'

            self.selection = None

            self.textArea1.configure(state="normal")
            self.textArea1.delete(1.0, END)
            self.textArea1.insert(END, self.menuViewDetails)
            self.textArea1.configure(state="disabled")

            self.input.bind("<Return>", self.selection_MenuViewDetails)

        if self.selection == "2":
            self.menuAdd = '(Press 0 to back).\n'

            self.selection = None

            self.textArea1.configure(state="normal")
            self.textArea1.delete(1.0, END)
            self.textArea1.insert(END, self.menuAdd)
            self.textArea1.configure(state="disabled")

            self.input.bind("<Return>", self.selection_MenuViewDetails)
            self.btAdd.configure(state="normal")
            self.btUpd.configure(state="disabled")

        if self.selection == "3":
            self.menuUpdate = 'Choose one of these customers ID.\n' \
                + '(Press 0 to back).\n'

            self.selection = None

            self.textArea1.configure(state="normal")
            self.textArea1.delete(1.0, END)
            self.textArea1.insert(END, self.menuUpdate)
            self.textArea1.configure(state="disabled")

            self.input.bind("<Return>", self.selection_MenuViewDetails)
            self.btUpd.configure(state="normal")
            self.btAdd.configure(state="disabled")

        if self.selection == "4":
            self.menuUpdate = 'Choose one of these customers ID.\n' \
                + '(Press 0 to back).\n'

            self.selection = None

            self.textArea1.configure(state="normal")
            self.textArea1.delete(1.0, END)
            self.textArea1.insert(END, self.menuUpdate)
            self.textArea1.configure(state="disabled")

            self.input.bind("<Return>", self.selection_MenuDelete)
            self.btUpd.configure(state="disabled")
            self.btAdd.configure(state="disabled")

    def selection_MenuViewDetails(self, event):
        self.selection = self.input.get()
        self.input.delete(0, END)
        if self.selection == "0":
            self.btUpd.configure(state="disabled")
            self.btAdd.configure(state="disabled")
            self.TextFieldsForm[0].configure(state="normal")
            self.TextFieldsForm[0].delete(0, END)
            self.TextFieldsForm[0].insert(END, self.customerBLL.getAutoID())
            self.TextFieldsForm[0].configure(state="readonly")
            self.TextFieldsForm[1].delete(0, END)
            self.TextFieldsForm[2].delete(0, END)
            self.run()

        else:
            self.list = self.customerBLL.findCustomersBy({"CUSTOMER_ID": self.selection})
            if len(self.list) != 0:
                self.showDetailsCustomer(self.list[0])

    def selection_MenuDelete(self, event):
        self.selection = self.input.get()
        self.input.delete(0, END)
        if self.selection == "0":
            self.btUpd.configure(state="disabled")
            self.btAdd.configure(state="disabled")
            self.TextFieldsForm[0].configure(state="normal")
            self.TextFieldsForm[0].delete(0, END)
            self.TextFieldsForm[0].insert(END, self.customerBLL.getAutoID())
            self.TextFieldsForm[0].configure(state="readonly")
            self.TextFieldsForm[1].delete(0, END)
            self.TextFieldsForm[2].delete(0, END)
            self.TextFieldsForm[3].delete(0, END)
            self.TextFieldsForm[4].delete(0, END)
            self.run()

        else:
            self.customerBLL.deleteCustomer(Customer(customerID=self.selection))
            self.reloadTable()


    def showDetailsCustomer(self, customer):
        self.customer = self.list[0]

        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.customer.getCustomerID())
        self.TextFieldsForm[0].configure(state="readonly")

        self.TextFieldsForm[1].delete(0, END)
        self.TextFieldsForm[1].insert(END, self.customer.getName())

        self.cbbGender.configure(state="normal")
        if self.customer.isGender():
            self.cbbGender.set("Nam")
        else:
            self.cbbGender.set("Nữ")
        self.cbbGender.configure(state="readonly")

        self.TextFieldsForm[2].delete(0, END)
        self.TextFieldsForm[2].insert(END, self.customer.getDateOfBirth())

        self.TextFieldsForm[3].delete(0, END)
        self.TextFieldsForm[3].insert(END, self.customer.getPhone())

        self.cbbMembership.configure(state="normal")
        if self.customer.isMembership():
            self.cbbMembership.set("Có")
        else:
            self.cbbMembership.set("Không")
        self.cbbMembership.configure(state="readonly")

        self.TextFieldsForm[4].delete(0, END)
        self.TextFieldsForm[4].insert(END, self.customer.getDateOfSup())

    def add(self):
        gender = True if self.cbbGender.get() == "Nam" else False
        member = True if self.cbbMembership.get() == "Có" else False
        dob = datetime.strptime(self.TextFieldsForm[2].get(), "%Y-%m-%d").date()
        dos = datetime.strptime(self.TextFieldsForm[4].get(), "%Y-%m-%d").date()
        self.newCustomer = Customer(self.TextFieldsForm[0].get(), self.TextFieldsForm[1].get(), gender, dob, self.TextFieldsForm[3].get(), member, dos, False)
        self.customerBLL.addCustomer(self.newCustomer)
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.customerBLL.getAutoID())
        self.TextFieldsForm[0].configure(state="readonly")
        self.TextFieldsForm[1].delete(0, END)
        self.TextFieldsForm[2].delete(0, END)
        self.TextFieldsForm[3].delete(0, END)
        self.TextFieldsForm[4].delete(0, END)
        self.reloadTable()

    def upd(self):
        gender = True if self.cbbGender.get() == "Nam" else False
        member = True if self.cbbMembership.get() == "Có" else False
        dob = datetime.strptime(self.TextFieldsForm[2].get(), "%Y-%m-%d").date()
        dos = datetime.strptime(self.TextFieldsForm[4].get(), "%Y-%m-%d").date()
        self.newCustomer = Customer(self.TextFieldsForm[0].get(), self.TextFieldsForm[1].get(), gender, dob, self.TextFieldsForm[3].get(), member, dos, False)
        self.customerBLL.updateCustomer(self.newCustomer)
        self.reloadTable()

    def reloadTable(self):
        self.textArea.configure(state='normal')
        self.textArea.delete(1.0, END)

        self.data = self.customerBLL.getCustomerList()
        row_str = " | ".join(self.columnNames[0: len(self.columnNames)-1]) + '\n\n'
        self.textArea.insert(END, row_str)
        for row in self.data:
            row_str = row.__str__() + '\n'
            self.textArea.insert(END, row_str)
        self.textArea.configure(state='disabled')




