from tkinter import *
from tkinter import ttk
from BLL.DecentralizationBLL import DecentralizationBLL
from DTO.Decentralization import Decentralization

class DecentralizationGUI(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#333333", width=1040, height=740)
        self.decentralizationBLL = DecentralizationBLL()
        self.init_components()

    def init_components(self):
        self.panel1 = Frame(self, bg="#333333", width=680)
        self.panel1.pack(side="left", fill="y")

        self.panel2 = Frame(self, bg="#FFFFFF", width=360)
        self.panel2.pack(side="right", fill="y")

        self.columnNames = self.decentralizationBLL.getDecentralizationDAL().getColumnNames()

        self.tableFrame = Frame(self.panel1, width=660, height=720, bg="#333333", highlightthickness=0, borderwidth=0)
        self.tableFrame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.tableFrame.pack_propagate(False)

        self.table = ttk.Treeview(self.tableFrame, columns=self.columnNames[0:len(self.columnNames)-1], show="headings")
        self.table.heading("0", text="DECENTRALIZATION_ID")
        self.table.heading("1", text="IS_SALE")
        self.table.heading("2", text="IS_PRODUCT")
        self.table.heading("3", text="IS_CATEGORY")
        self.table.heading("4", text="IS_RECIPE")
        self.table.heading("5", text="IS_IMPORT")
        self.table.heading("6", text="IS_BILL")
        self.table.heading("7", text="IS_WAREHOUSES")
        self.table.heading("8", text="IS_ACCOUNT")
        self.table.heading("9", text="IS_STAFF")
        self.table.heading("10", text="IS_CUSTOMER")
        self.table.heading("11", text="IS_DISCOUNT")
        self.table.heading("12", text="IS_DECENTRALIZE")
        self.table.heading("13", text="DECENTRALIZATION_NAME")
        self.data = self.decentralizationBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)
        self.table.pack(fill=BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tableFrame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="bottom", fill="x")

        self.table.bind('<<TreeviewSelect>>', self.showDetailsDecentralization)
        self.pnlDecentralizationConfiguration = Frame(self.panel2, bg="#FFFFFF", width=350, height=500)

        self.canvas = Canvas(self.pnlDecentralizationConfiguration, bg="#FFFFFF", width=350, height=500, highlightthickness=0, borderwidth=0)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        self.frameInCanvas = Frame(self.canvas, bg="#FFFFFF")
        self.canvas.create_window((0,0), window=self.frameInCanvas, anchor="nw")

        self.frameInCanvas.bind("<Configure>", lambda event, canvas=self.canvas: canvas.configure(scrollregion=canvas.bbox("all")))
        self.pnlDecentralizationConfiguration.pack(padx=10, pady=10, expand=True)

        self.labelForm = []
        self.TextFieldsForm = []
        self.cbbForm = []
        self.row = 0
        self.column = 0
        for i in range(0, len(self.columnNames)-1):
            self.labelForm.append(Label(self.frameInCanvas, text=self.columnNames[i] + ": ", fg="#000000", bg="#ffffff"))
            self.labelForm[i].grid(row=self.row, column=self.column, padx=5, pady=10)
            self.column = self.column + 1
            if self.columnNames[i] == "DECENTRALIZATION_ID":
                self.TextFieldsForm.append(Entry(self.frameInCanvas, fg="#000000", bg="#ffffff", width=27))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, self.decentralizationBLL.getAutoID())
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=5, pady=10, ipady=4)
            elif self.columnNames[i] == "DECENTRALIZATION_NAME":
                self.TextFieldsForm.append(Entry(self.frameInCanvas, fg="#000000", bg="#ffffff", width=27))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=5, pady=10, ipady=4)
            else:
                self.cbbForm.append(ttk.Combobox(self.frameInCanvas, values=["Không", "Xem", "Sửa", "Xem và sửa"], width=24))
                self.cbbForm[len(self.cbbForm)-1].configure(state="readonly")
                self.cbbForm[len(self.cbbForm)-1].grid(row=self.row, column=self.column, padx=5, pady=10, ipady=4)

            self.row = self.row +1
            self.column = 0


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

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def showDetailsDecentralization(self, event):
        for row in self.table.selection():
            item = self.table.item(row)
            values = item["values"]

            self.TextFieldsForm[0].configure(state="normal")
            self.TextFieldsForm[0].delete(0, END)
            self.TextFieldsForm[0].insert(END, values[0])
            self.TextFieldsForm[0].configure(state="readonly")

            self.TextFieldsForm[1].delete(0, END)
            self.TextFieldsForm[1].insert(END, values[13])

            for i in range(0,len(self.cbbForm)):
                self.cbbForm[i].set(values[i+1])

            self.btAdd.configure(state="disabled")
            self.btUpd.configure(state="normal")
            self.btDel.configure(state="normal")

    def loadTable(self):
        for item in self.table.get_children():
            self.table.delete(item)
        self.data = self.decentralizationBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)

    def add(self):
        self.arr = []
        for i in range(0,len(self.cbbForm)):
            if self.cbbForm[i].get() == "Không":
                self.arr.append(0)
            if self.cbbForm[i].get() == "Xem":
                self.arr.append(1)
            if self.cbbForm[i].get() == "Sửa":
                self.arr.append(2)
            if self.cbbForm[i].get() == "Xem và sửa":
                self.arr.append(3)

        self.newDecentralization = Decentralization(self.TextFieldsForm[0].get(), self.arr[0], self.arr[1], self.arr[2], self.arr[3], self.arr[4], self.arr[5], self.arr[6], self.arr[7], self.arr[8], self.arr[9], self.arr[10], self.arr[11], self.TextFieldsForm[1].get(), False)
        self.decentralizationBLL.addDecentralization(self.newDecentralization)
        self.ref()

    def upd(self):
        self.arr = []
        for i in range(0,len(self.cbbForm)):
            if self.cbbForm[i].get() == "Không":
                self.arr.append(0)
            if self.cbbForm[i].get() == "Xem":
                self.arr.append(1)
            if self.cbbForm[i].get() == "Sửa":
                self.arr.append(2)
            if self.cbbForm[i].get() == "Xem và sửa":
                self.arr.append(3)

        self.newDecentralization = Decentralization(self.TextFieldsForm[0].get(), self.arr[0], self.arr[1], self.arr[2], self.arr[3], self.arr[4], self.arr[5], self.arr[6], self.arr[7], self.arr[8], self.arr[9], self.arr[10], self.arr[11], self.TextFieldsForm[1].get(), False)
        self.decentralizationBLL.updateDecentralization(self.newDecentralization)
        self.loadTable()

    def dele(self):
        self.decentralizationBLL.deleteDecentralization(Decentralization(decentralizationID = self.TextFieldsForm[0].get()))
        self.ref()

    def ref(self):
        self.loadTable()
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.decentralizationBLL.getAutoID())
        self.TextFieldsForm[0].configure(state="readonly")
        for i in range(1, len(self.TextFieldsForm)):
            self.TextFieldsForm[i].delete(0, END)

        for i in range(0,len(self.cbbForm)):
            self.cbbForm[i].configure(state="normal")
            self.cbbForm[i].delete(0, END)
            self.cbbForm[i].configure(state="readonly")

        self.btAdd.configure(state="normal")
        self.btUpd.configure(state="disabled")
        self.btDel.configure(state="disabled")

