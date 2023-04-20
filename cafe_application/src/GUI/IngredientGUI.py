from tkinter import *
from tkinter import ttk

from BLL.IngredientBLL import IngredientBLL
from BLL.SupplierBLL import SupplierBLL
from DTO.Ingredient import Ingredient


class IngredientGUI(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#333333", width=1040, height=740)
        self.ingredientBLL = IngredientBLL()
        self.init_components()

    def init_components(self):
        self.panel1 = Frame(self, bg="#333333", width=680)
        self.panel1.pack(side="left", fill="y")

        self.panel2 = Frame(self, bg="#FFFFFF", width=360)
        self.panel2.pack(side="right", fill="y")

        self.columnNames = self.ingredientBLL.getIngredientDAL().getColumnNames()
        self.supplierBLL = SupplierBLL()
        self.suppliersID = []
        for supplier in self.supplierBLL.getSupplierList():
            self.suppliersID.append(self.supplierBLL.getValueByKey(supplier, "SUPPLIER_ID"))

        self.tableFrame = Frame(self.panel1, width=660, height=720, bg="#333333", highlightthickness=0, borderwidth=0)
        self.tableFrame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.tableFrame.pack_propagate(False)

        self.table = ttk.Treeview(self.tableFrame, columns=self.columnNames[0:len(self.columnNames)-1], show="headings")
        self.table.heading("0", text="INGREDIENT_ID")
        self.table.heading("1", text="NAME")
        self.table.heading("2", text="QUANTITY")
        self.table.heading("3", text="UNIT")
        self.table.heading("4", text="SUPPLIER_ID")
        self.data = self.ingredientBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)
        self.table.pack(fill=BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tableFrame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="bottom", fill="x")

        self.table.bind('<<TreeviewSelect>>', self.showDetailsIngredient)

        self.pnlIngredientConfiguration = Frame(self.panel2, bg="#FFFFFF", width=350)
        self.pnlIngredientConfiguration.pack(padx=10, pady=10)

        self.labelForm = []
        self.TextFieldsForm = []
        self.row = 0
        self.column = 0
        for i in range(0, len(self.columnNames)-1):
            self.labelForm.append(Label(self.pnlIngredientConfiguration, text=self.columnNames[i] + ": ", fg="#000000", bg="#ffffff"))
            self.labelForm[i].grid(row=self.row, column=self.column, padx=20, pady=10)
            self.column = self.column + 1
            if self.columnNames[i] == "INGREDIENT_ID":
                self.TextFieldsForm.append(Entry(self.pnlIngredientConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, self.ingredientBLL.getAutoID())
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "SUPPLIER_ID":
                self.cbbSupplierID = ttk.Combobox(self.pnlIngredientConfiguration, values=self.suppliersID, width=27)
                self.cbbSupplierID.configure(state="readonly")
                self.cbbSupplierID.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "UNIT":
                self.cbbUnit = ttk.Combobox(self.pnlIngredientConfiguration, values=["kg", "l", "bag"], width=27)
                self.cbbUnit.configure(state="readonly")
                self.cbbUnit.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            else:
                self.TextFieldsForm.append(Entry(self.pnlIngredientConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

        self.showImage = Frame(self.panel2, width=350, height=250, bg="#FFFFFF")
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

    def showDetailsIngredient(self, event):
        for row in self.table.selection():
            item = self.table.item(row)
            values = item["values"]

            self.TextFieldsForm[0].configure(state="normal")
            self.TextFieldsForm[0].delete(0, END)
            self.TextFieldsForm[0].insert(END, values[0])
            self.TextFieldsForm[0].configure(state="readonly")

            self.TextFieldsForm[1].delete(0, END)
            self.TextFieldsForm[1].insert(END, values[1])

            self.TextFieldsForm[2].delete(0, END)
            self.TextFieldsForm[2].insert(END, values[2])

            self.cbbUnit.configure(state="normal")
            self.cbbUnit.set(values[3])
            self.cbbUnit.configure(state="readonly")

            self.cbbSupplierID.configure(state="normal")
            self.cbbSupplierID.set(values[4])
            self.cbbSupplierID.configure(state="readonly")

            self.btAdd.configure(state="disabled")
            self.btUpd.configure(state="normal")
            self.btDel.configure(state="normal")

    def loadTable(self):
        for item in self.table.get_children():
            self.table.delete(item)
        self.data = self.ingredientBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)

    def add(self):
        self.newIngredient = Ingredient(self.TextFieldsForm[0].get(), self.TextFieldsForm[1].get(), float(self.TextFieldsForm[2].get()), self.cbbUnit.get(), self.cbbSupplierID.get(), False)
        self.ingredientBLL.addIngredient(self.newIngredient)
        self.ref()

    def upd(self):
        self.newIngredient = Ingredient(self.TextFieldsForm[0].get(), self.TextFieldsForm[1].get(), float(self.TextFieldsForm[2].get()), self.cbbUnit.get(), self.cbbSupplierID.get(), False)
        self.ingredientBLL.updateIngredient(self.newIngredient)
        self.loadTable()

    def dele(self):
        self.ingredientBLL.deleteIngredient(Ingredient(ingredientID = self.TextFieldsForm[0].get()))
        self.ref()

    def ref(self):
        self.loadTable()
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.ingredientBLL.getAutoID())
        self.TextFieldsForm[0].configure(state="readonly")
        for i in range(1, len(self.TextFieldsForm)):
            self.TextFieldsForm[i].delete(0, END)

        self.cbbUnit.configure(state="normal")
        self.cbbUnit.delete(0, END)
        self.cbbUnit.configure(state="readonly")

        self.cbbSupplierID.configure(state="normal")
        self.cbbSupplierID.delete(0, END)
        self.cbbSupplierID.configure(state="readonly")

        self.btAdd.configure(state="normal")
        self.btUpd.configure(state="disabled")
        self.btDel.configure(state="disabled")

