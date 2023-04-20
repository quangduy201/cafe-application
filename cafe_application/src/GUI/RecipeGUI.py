from tkinter import *
from tkinter import ttk

from BLL.ProductBLL import ProductBLL
from BLL.RecipeBLL import RecipeBLL
from DTO.Recipe import Recipe


class RecipeGUI(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#333333", width=1040, height=740)
        self.recipeBLL = RecipeBLL()
        self.init_components()

    def init_components(self):
        self.panel1 = Frame(self, bg="#333333", width=680)
        self.panel1.pack(side="left", fill="y")

        self.panel2 = Frame(self, bg="#FFFFFF", width=360)
        self.panel2.pack(side="right", fill="y")

        self.columnNames = self.recipeBLL.getRecipeDAL().getColumnNames()
        self.productBLL = ProductBLL()
        self.recipeBLL = RecipeBLL()
        self.productsID = []
        self.recipesID = []
        for product in self.productBLL.getProductList():
            self.productsID.append(self.productBLL.getValueByKey(product, "PRODUCT_ID"))
        for recipe in self.recipeBLL.getRecipeList():
            self.recipesID.append(self.recipeBLL.getValueByKey(recipe, "RECIPE_ID"))

        self.tableFrame = Frame(self.panel1, width=660, height=720, bg="#333333", highlightthickness=0, borderwidth=0)
        self.tableFrame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.tableFrame.pack_propagate(False)

        self.table = ttk.Treeview(self.tableFrame, columns=self.columnNames[0:len(self.columnNames)-1], show="headings")
        self.table.heading("0", text="RECIPE_ID")
        self.table.heading("1", text="PRODUCT_ID")
        self.table.heading("2", text="INGREDIENT_ID")
        self.table.heading("3", text="MASS")
        self.table.heading("4", text="UNIT")
        self.data = self.recipeBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)
        self.table.pack(fill=BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tableFrame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="bottom", fill="x")

        self.table.bind('<<TreeviewSelect>>', self.showDetailsRecipe)

        self.pnlRecipeConfiguration = Frame(self.panel2, bg="#FFFFFF", width=350)
        self.pnlRecipeConfiguration.pack(padx=10, pady=10)

        self.labelForm = []
        self.TextFieldsForm = []
        self.row = 0
        self.column = 0
        for i in range(0, len(self.columnNames)-1):
            self.labelForm.append(Label(self.pnlRecipeConfiguration, text=self.columnNames[i] + ": ", fg="#000000", bg="#ffffff"))
            self.labelForm[i].grid(row=self.row, column=self.column, padx=20, pady=10)
            self.column = self.column + 1
            if self.columnNames[i] == "RECIPE_ID":
                self.TextFieldsForm.append(Entry(self.pnlRecipeConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, self.recipeBLL.getAutoID())
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "PRODUCT_ID":
                self.cbbproductID = ttk.Combobox(self.pnlRecipeConfiguration, values=self.productsID, width=27)
                self.cbbproductID.configure(state="readonly")
                self.cbbproductID.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "INGREDIENT_ID":
                self.cbbingredientID = ttk.Combobox(self.pnlRecipeConfiguration, values=self.recipesID, width=27)
                self.cbbingredientID.configure(state="readonly")
                self.cbbingredientID.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "UNIT":
                self.cbbUnit = ttk.Combobox(self.pnlRecipeConfiguration, values=["kg", "l", "bag"], width=27)
                self.cbbUnit.configure(state="readonly")
                self.cbbUnit.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            else:
                self.TextFieldsForm.append(Entry(self.pnlRecipeConfiguration, fg="#000000", bg="#ffffff", width=30))
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

    def showDetailsRecipe(self, event):
        for row in self.table.selection():
            item = self.table.item(row)
            values = item["values"]

            self.TextFieldsForm[0].configure(state="normal")
            self.TextFieldsForm[0].delete(0, END)
            self.TextFieldsForm[0].insert(END, values[0])
            self.TextFieldsForm[0].configure(state="readonly")

            self.TextFieldsForm[1].delete(0, END)
            self.TextFieldsForm[1].insert(END, values[3])

            self.cbbproductID.configure(state="normal")
            self.cbbproductID.set(values[1])
            self.cbbproductID.configure(state="readonly")

            self.cbbingredientID.configure(state="normal")
            self.cbbingredientID.set(values[2])
            self.cbbingredientID.configure(state="readonly")

            self.cbbUnit.configure(state="normal")
            self.cbbUnit.set(values[4])
            self.cbbUnit.configure(state="readonly")

            self.btAdd.configure(state="disabled")
            self.btUpd.configure(state="normal")
            self.btDel.configure(state="normal")

    def loadTable(self):
        for item in self.table.get_children():
            self.table.delete(item)
        self.data = self.recipeBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)

    def add(self):
        self.newRecipe = Recipe(self.TextFieldsForm[0].get(), self.cbbproductID.get(), self.cbbingredientID.get(), float(self.TextFieldsForm[1].get()), self.cbbUnit.get(), False)
        self.recipeBLL.addRecipe(self.newRecipe)
        self.ref()

    def upd(self):
        self.newRecipe = Recipe(self.TextFieldsForm[0].get(), self.cbbproductID.get(), self.cbbingredientID.get(), float(self.TextFieldsForm[1].get()), self.cbbUnit.get(), False)
        self.recipeBLL.updateRecipe(self.newRecipe)
        self.loadTable()

    def dele(self):
        self.recipeBLL.deleteRecipe(Recipe(recipeID = self.TextFieldsForm[0].get()))
        self.ref()

    def ref(self):
        self.loadTable()
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.recipeBLL.getAutoID())
        self.TextFieldsForm[0].configure(state="readonly")
        for i in range(1, len(self.TextFieldsForm)):
            self.TextFieldsForm[i].delete(0, END)

        self.cbbproductID.configure(state="normal")
        self.cbbproductID.delete(0, END)
        self.cbbproductID.configure(state="readonly")

        self.cbbingredientID.configure(state="normal")
        self.cbbingredientID.delete(0, END)
        self.cbbingredientID.configure(state="readonly")

        self.cbbUnit.configure(state="normal")
        self.cbbUnit.delete(0, END)
        self.cbbUnit.configure(state="readonly")

        self.btAdd.configure(state="normal")
        self.btUpd.configure(state="disabled")
        self.btDel.configure(state="disabled")



