from tkinter import *
from tkinter import ttk
from BLL.DecentralizationBLL import DecentralizationBLL
from DTO.Decentralization import Decentralization

class DecentralizationGUI(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#333333", width=1040, height=740)
        self.decentralizationBLL = DecentralizationBLL()
        self.init_components()
        self.run()

    def init_components(self):
        self.panel1 = Frame(self, bg="#333333", width=680)
        self.panel1.pack(side="left", fill="y")

        self.panel2 = Frame(self, bg="#FFFFFF", width=360)
        self.panel2.pack(side="right", fill="y")

        self.columnNames = self.decentralizationBLL.getDecentralizationDAL().getColumnNames()

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

        self.pnlDecentralizationConfiguration = Frame(self.panel2, bg="#FFFFFF", width=350, height=500)

        self.canvas = Canvas(self.pnlDecentralizationConfiguration, bg="#FFFFFF", width=350, height=500, highlightthickness=0, borderwidth=0)
        self.canvas.pack(fill=BOTH, expand=True)
        # self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.scrollbar2 = Scrollbar(self.pnlDecentralizationConfiguration, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar2.pack(side=RIGHT, fill="x", expand=True)

        self.canvas.configure(yscrollcommand=self.scrollbar2.set)

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

        # self.showImage = Frame(self.panel2, width=350, height=250, bg="#FFFFFF")
        # self.showImage.pack(padx=10, pady=0)

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
            + '1. View decentralization details .\n' \
            + '2. Add new decentralization.\n' \
            + '3. Edit decentralization.\n' \
            + '4. Delete decentralization.\n'

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
            self.menuViewDetails = 'Choose one of these decentralizations ID.\n' \
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
            self.menuUpdate = 'Choose one of these decentralizations ID.\n' \
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
            self.menuUpdate = 'Choose one of these decentralizations ID.\n' \
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
            self.TextFieldsForm[0].insert(END, self.decentralizationBLL.getAutoID())
            self.TextFieldsForm[0].configure(state="readonly")
            self.TextFieldsForm[1].delete(0, END)
            self.run()

        else:
            self.list = self.decentralizationBLL.findDecentralizationsBy({"DECENTRALIZATION_ID": self.selection})
            if len(self.list) != 0:
                self.showDetailsDecentralization(self.list[0])

    def selection_MenuDelete(self, event):
        self.selection = self.input.get()
        self.input.delete(0, END)
        if self.selection == "0":
            self.btUpd.configure(state="disabled")
            self.btAdd.configure(state="disabled")
            self.TextFieldsForm[0].configure(state="normal")
            self.TextFieldsForm[0].delete(0, END)
            self.TextFieldsForm[0].insert(END, self.decentralizationBLL.getAutoID())
            self.TextFieldsForm[0].configure(state="readonly")
            self.TextFieldsForm[1].delete(0, END)
            self.run()

        else:
            self.decentralizationBLL.deleteDecentralization(Decentralization(decentralizationID=self.selection))
            self.reloadTable()


    def showDetailsDecentralization(self, decentralization):
        self.decentralization = self.list[0]
        array = self.decentralization.getArray()
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.decentralization.getDecentralizationID())
        self.TextFieldsForm[0].configure(state="readonly")

        self.TextFieldsForm[1].delete(0, END)
        self.TextFieldsForm[1].insert(END, self.decentralization.getDecentralizationName())

        for i in range(0,len(self.cbbForm)):
            if array[i] == 0:
                self.cbbForm[i].set("Không")
            if array[i] == 1:
                self.cbbForm[i].set("Xem")
            if array[i] == 2:
                self.cbbForm[i].set("Sửa")
            if array[i] == 3:
                self.cbbForm[i].set("Xem và sửa")

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
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.decentralizationBLL.getAutoID())
        self.TextFieldsForm[0].configure(state="readonly")
        self.TextFieldsForm[1].delete(0, END)
        self.reloadTable()

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
        print(self.newDecentralization)
        self.decentralizationBLL.updateDecentralization(self.newDecentralization)
        self.reloadTable()

    def reloadTable(self):
        self.textArea.configure(state='normal')
        self.textArea.delete(1.0, END)

        self.data = self.decentralizationBLL.getDecentralizationList()
        row_str = " | ".join(self.columnNames[0: len(self.columnNames)-1]) + '\n\n'
        self.textArea.insert(END, row_str)
        for row in self.data:
            row_str = row.__str__() + '\n'
            self.textArea.insert(END, row_str)
        self.textArea.configure(state='disabled')

