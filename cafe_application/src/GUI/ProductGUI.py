import os
from tkinter import *
from tkinter import filedialog, ttk

from BLL.CategoryBLL import CategoryBLL
from BLL.ProductBLL import ProductBLL
from DTO.Product import Product
from PIL import Image, ImageTk


class ProductGUI(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#333333", width=1040, height=740)
        self.productBLL = ProductBLL()
        self.init_components()

    def init_components(self):
        self.panel1 = Frame(self, bg="#333333", width=680)
        self.panel1.pack(side="left", fill="y")

        self.panel2 = Frame(self, bg="#FFFFFF", width=360)
        self.panel2.pack(side="right", fill="y")

        self.columnNames = self.productBLL.getProductDAL().getColumnNames()
        self.categoryBLL = CategoryBLL()
        self.categoriesID = []
        for category in self.categoryBLL.getCategoryList():
            self.categoriesID.append(self.categoryBLL.getValueByKey(category, "CATEGORY_ID"))

        self.tableFrame = Frame(self.panel1, width=660, height=720, bg="#333333", highlightthickness=0, borderwidth=0)
        self.tableFrame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.tableFrame.pack_propagate(False)

        self.table = ttk.Treeview(self.tableFrame, columns=self.columnNames[0:5], show="headings")
        self.table.heading("0", text="PRODUCT_ID")
        self.table.heading("1", text="NAME")
        self.table.heading("2", text="CATEGORY_ID")
        self.table.heading("3", text="SIZED")
        self.table.heading("4", text="COST")
        self.data = self.productBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)
        self.table.pack(fill=BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tableFrame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="bottom", fill="x")

        self.table.bind('<<TreeviewSelect>>', self.showDetailsProduct)

        self.pnlProductConfiguration = Frame(self.panel2, bg="#FFFFFF", width=350)
        self.pnlProductConfiguration.pack(padx=10, pady=10)

        self.labelForm = []
        self.TextFieldsForm = []
        self.row = 0
        self.column = 0
        for i in range(0, len(self.columnNames)-1):
            self.labelForm.append(Label(self.pnlProductConfiguration, text=self.columnNames[i] + ": ", fg="#000000", bg="#ffffff"))
            self.labelForm[i].grid(row=self.row, column=self.column, padx=20, pady=10)
            self.column = self.column + 1
            if self.columnNames[i] == "PRODUCT_ID":
                self.TextFieldsForm.append(Entry(self.pnlProductConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, self.productBLL.getAutoID())
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "CATEGORY_ID":
                self.cbbCategoryID = ttk.Combobox(self.pnlProductConfiguration, values=self.categoriesID, width=27)
                self.cbbCategoryID.configure(state="readonly")
                self.cbbCategoryID.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "SIZED":
                self.cbbSized = ttk.Combobox(self.pnlProductConfiguration, values=["null", "S", "M", "L"], width=27)
                self.cbbSized.configure(state="readonly")
                self.cbbSized.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "IMAGE":
                self.btChooseImg = Button(self.pnlProductConfiguration, text="Choose an image", width=25, bg="#AFD1DF", command=self.selectImage)
                self.btChooseImg.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            else:
                self.TextFieldsForm.append(Entry(self.pnlProductConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

        self.showImage = Frame(self.panel2, width=350, height=250, bg="#FFFFFF")
        self.showImage.pack(padx=10, pady=0)
        self.imgProduct = Label(self.showImage, image=None, bg="#FFFFFF")

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


    def selectImage(self):
        self.initial_dir = os.path.expanduser('cafe_application\\img')
        self.path = filedialog.askopenfilename(initialdir=self.initial_dir, filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")]).split("/")[-1]
        self.chosenImg = "cafe_application\\img\\" + self.path
        self.imgProduct.destroy()
        self.img = ImageTk.PhotoImage(Image.open(self.chosenImg))
        self.imgProduct = Label(self.showImage, image=self.img, bg="#FFFFFF")
        self.imgProduct.pack()
        self.chosenImg = "cafe_application\\\\img\\\\" + self.path

    def showDetailsProduct(self, event):
        for row in self.table.selection():
            item = self.table.item(row)
            values = item["values"]

            self.TextFieldsForm[0].configure(state="normal")
            self.TextFieldsForm[0].delete(0, END)
            self.TextFieldsForm[0].insert(END, values[0])
            self.TextFieldsForm[0].configure(state="readonly")

            self.TextFieldsForm[1].delete(0, END)
            self.TextFieldsForm[1].insert(END, values[1])

            self.cbbCategoryID.configure(state="normal")
            self.cbbCategoryID.set(values[2])
            self.cbbCategoryID.configure(state="readonly")

            self.cbbSized.configure(state="normal")
            self.cbbSized.set(values[3])
            self.cbbSized.configure(state="readonly")

            self.TextFieldsForm[2].delete(0, END)
            self.TextFieldsForm[2].insert(END, values[4])

            self.imgProduct.destroy()
            self.product = self.productBLL.findProductsBy({"PRODUCT_ID": values[0]})[0]
            self.chosenImg = self.product.getImage()
            self.img = ImageTk.PhotoImage(Image.open(self.chosenImg))

            self.imgProduct = Label(self.showImage, image=self.img, bg="#FFFFFF")
            self.imgProduct.pack()

            self.btAdd.configure(state="disabled")
            self.btUpd.configure(state="normal")
            self.btDel.configure(state="normal")

    def loadTable(self):
        for item in self.table.get_children():
            self.table.delete(item)
        self.data = self.productBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)

    def add(self):
        self.newProduct = Product(self.TextFieldsForm[0].get(), self.TextFieldsForm[1].get(), self.cbbCategoryID.get(), self.cbbSized.get(), float(self.TextFieldsForm[2].get()), image = self.chosenImg, deleted = False)
        self.productBLL.addProduct(self.newProduct)
        self.ref()

    def upd(self):
        self.newProduct = Product(self.TextFieldsForm[0].get(), self.TextFieldsForm[1].get(), self.cbbCategoryID.get(), self.cbbSized.get(), float(self.TextFieldsForm[2].get()),  image = self.chosenImg, deleted = False)
        self.productBLL.updateProduct(self.newProduct)
        self.loadTable()

    def dele(self):
        self.productBLL.deleteProduct(Product(productID = self.TextFieldsForm[0].get()))
        self.ref()

    def ref(self):
        self.loadTable()
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.productBLL.getAutoID())
        self.TextFieldsForm[0].configure(state="readonly")
        self.TextFieldsForm[1].delete(0, END)
        self.TextFieldsForm[2].delete(0, END)
        self.cbbCategoryID.configure(state="normal")
        self.cbbCategoryID.delete(0, END)
        self.cbbCategoryID.configure(state="readonly")
        self.cbbSized.configure(state="normal")
        self.cbbSized.delete(0, END)
        self.cbbSized.configure(state="readonly")
        self.imgProduct.destroy()
        self.imgProduct = Label(self.showImage, image=None, bg="#FFFFFF")
        self.btAdd.configure(state="normal")
        self.btUpd.configure(state="disabled")
        self.btDel.configure(state="disabled")

