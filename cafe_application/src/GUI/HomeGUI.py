from tkinter import *

from BLL.DecentralizationBLL import DecentralizationBLL
from BLL.StaffBLL import StaffBLL
from GUI.AccountGUI import AccountGUI
from GUI.BillGUI import BillGUI
from GUI.CategoryGUI import CategoryGUI
from GUI.CustomerGUI import CustomerGUI
from GUI.DecentralizationGUI import DecentralizationGUI
from GUI.IngredientGUI import IngredientGUI
from GUI.ProductGUI import ProductGUI
from GUI.ReceiptGUI import ReceiptGUI
from GUI.RecipeGUI import RecipeGUI
from GUI.SaleGUI import SaleGUI
from GUI.StaffGUI import StaffGUI
from GUI.SupplierGUI import SupplierGUI
from PIL import Image, ImageTk


class HomeGUI(Frame):
    def __init__(self, account):
        self.__account = account
        self.__staff = StaffBLL().searchStaffs("STAFF_ID = '" + self.__account.getStaffID() + "'")[0]
        self.__decentralization = DecentralizationBLL().searchDecentralizations("DECENTRALIZATION_ID = '" + self.__account.getDecentralizationID() + "'")[0]
        self.__arr = []
        self.__arr.append(0)
        self.__arr.append(self.__decentralization.getIsSale())
        self.__arr.append(self.__decentralization.getIsProduct())
        self.__arr.append(self.__decentralization.getIsCategory())
        self.__arr.append(self.__decentralization.getIsRecipe())
        self.__arr.append(self.__decentralization.getIsImport())
        self.__arr.append(self.__decentralization.getIsBill())
        self.__arr.append(self.__decentralization.getIsWarehouses())
        self.__arr.append(self.__decentralization.getIsDecentralize())
        self.__arr.append(self.__decentralization.getIsAccount())
        self.__arr.append(self.__decentralization.getIsStaff())
        self.__arr.append(self.__decentralization.getIsCustomer())
        self.__arr.append(self.__decentralization.getIsDiscount())
        self.__arr.append(self.__decentralization.getIsDecentralize())
        self.__arr.append(1)

        self.__master = Tk()
        self.init_components()


    def init_components(self):
        self.__master.configure(bg="#23a661")
        self.__master.title("Home")
        self.__master.resizable(False, False)
        x_cordinate = int((self.__master.winfo_screenwidth()/2) - (1350/2))
        y_cordinate = int((self.__master.winfo_screenheight()/2) - (760/2))
        self.__master.geometry("{}x{}+{}+{}".format(1350, 760, x_cordinate, y_cordinate))

        self.contentPane = Frame( bg="#ffffff", width=1350, height=760)
        self.contentPane.master = self.__master
        self.contentPane.pack(fill="both", expand=True)

        self.west = Frame(self.contentPane, bg="#23a661", width=300, height=760)
        self.west.pack(side="left")
        self.west.pack(fill="both", expand=True)

        self.info = Frame(self.west, bg="#333333", width=280, height=80)
        self.info.place(x=10, y=10)

        self.imgAvartar = ImageTk.PhotoImage(Image.open("cafe_application\\img\\bell-boy.png").resize((60, 60), Image.ANTIALIAS))

        self.avatar = Label(self.info, image=self.imgAvartar, bg="#333333")
        self.avatar.place(x=10, y=10)

        self.name = Label(self.info, text="Tên: " + self.__staff.getName(), font=("Tahoma", 10), fg="#ffffff", bg="#333333")
        self.name.place(x=80, y=15)
        self.rule = Label(self.info, text="Vai trò: " + self.__decentralization.getDecentralizationName(), font=("Tahoma", 10), fg="#ffffff", bg="#333333")
        self.rule.place(x=80, y=40)

        self.imgMode = ImageTk.PhotoImage(Image.open("cafe_application\\img\\sun.png").resize((30, 30), Image.ANTIALIAS))
        self.mode = Label(self.info, image=self.imgMode, bg="#333333")
        self.mode.bind('<Button-1>', self.changeMode)
        self.mode.place(x=230, y=40)
        self.darkMode = True

        self.fram_cate = Frame(self.west, bg="#333333", width=280, height=650)
        self.fram_cate.place(x=10, y=100)

        self.cate = Frame(self.fram_cate, bg="#333333", width=260, height=630)
        self.cate.place(x=10, y=10)

        self.panel = []
        self.panel.append(None)
        for i in range(1, 15):
            self.panel.append(Frame(self.cate, bg="#333333", width=250, height=40))
            self.panel[i].bind('<Button-1>', self.on_panel_click)

        self.label = []
        self.label.append(None)
        self.label.append(Label(self.panel[1], text="Bán hàng", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[2], text="Sản phẩm", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[3], text="Loại sản phẩm", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[4], text="Công Thức", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[5], text="Nhập hàng", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[6], text="Hóa đơn", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[7], text="Nhà kho", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[8], text="Thống kê", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[9], text="Tài khoản", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[10], text="Nhân viên", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[11], text="Khách hàng", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[12], text="Giảm giá", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[13], text="Phân quyền", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))
        self.label.append(Label(self.panel[14], text="Nhà cung cấp", font=("Times New Roman", 15), fg="#ffffff", bg="#333333"))

        self.icon = []
        self.image = []
        self.icon.append(None)
        self.image.append(None)
        for i in range(1, 14):
            url = "cafe_application\\img\\0" + str(i) + ".png"
            self.icon.append(ImageTk.PhotoImage(Image.open(url).resize((30, 30), Image.ANTIALIAS)))
            self.image.append(Label(self.panel[i], image=self.icon[i], bg="#333333"))
        self.icon.append(ImageTk.PhotoImage(Image.open(url).resize((30, 30), Image.ANTIALIAS)))
        self.image.append(Label(self.panel[len(self.label)-1], image=self.icon[len(self.icon)-1], bg="#333333"))
        self.x = 5
        self.y = 5
        for i in range(1, 15):
            if self.__arr[i] != 0:
                self.panel[i].place(x=self.x, y=self.y)
                self.image[i].place(x=20, y=4)
                self.label[i].place(x=70, y=5)
                self.y = self.y + 45

        for i in range(1, 15):
            for child in self.panel[i].winfo_children():
                child.bind('<Button-1>', self.on_childPanel_click)

        self.east = Frame(self.contentPane, bg="#333333", width=1040, height=740)
        self.east.place(x=300, y=10)

        self.function = Frame(self.east, bg="#333333", width=1040, height=740)
        self.function.pack()


        self.__master.mainloop()

    def changeMode(self, event):
        if self.darkMode:
            self.imgMode = ImageTk.PhotoImage(Image.open("cafe_application\\img\\moon.png").resize((30, 30), Image.ANTIALIAS))
            self.mode.configure(image=self.imgMode, bg="#4fc235")

            self.__master.configure(bg="#ffffff")
            self.west.configure(bg="#ffffff")

            self.info.configure(bg="#4fc235")
            self.avatar.configure(bg="#4fc235")
            self.name.configure(bg="#4fc235")
            self.rule.configure(bg="#4fc235")
            self.fram_cate.configure(bg="#4fc235")
            self.cate.configure(bg="#4fc235")

            for i in range(1, 15):
                self.panel[i].configure(bg="#f0f0f0")
                self.image[i].configure(bg="#f0f0f0")
                self.label[i].configure(bg="#f0f0f0", fg="#000000")

            self.darkMode = False
        else:
            self.imgMode = ImageTk.PhotoImage(Image.open("cafe_application\\img\\sun.png").resize((30, 30), Image.ANTIALIAS))
            self.mode.configure(image=self.imgMode, bg="#333333")

            self.__master.configure(bg="#23a661")
            self.west.configure(bg="#23a661")

            self.info.configure(bg="#333333")
            self.avatar.configure(bg="#333333")
            self.name.configure(bg="#333333")
            self.rule.configure(bg="#333333")
            self.fram_cate.configure(bg="#333333")
            self.cate.configure(bg="#333333")

            for i in range(1, 15):
                self.panel[i].configure(bg="#333333")
                self.image[i].configure(bg="#333333")
                self.label[i].configure(bg="#333333", fg="#FFFFFF")

            self.darkMode = True

    def on_panel_click(self, event):
        self.disable()
        for child in event.widget.winfo_children():
            child.configure(background='#23a661')
        event.widget.configure(background='#23a661')
        self.callChildFrom(event.widget)

    def on_childPanel_click(self, event):
        self.disable()
        if self.darkMode:
            parent_frame = event.widget.master
            for child in parent_frame.winfo_children():
                child.configure(background='#23a661')
            parent_frame.configure(background='#23a661')
            self.callChildFrom(parent_frame)
        else:
            parent_frame = event.widget.master
            for child in parent_frame.winfo_children():
                child.configure(background='#44963C')
            parent_frame.configure(background='#44963C')
            self.callChildFrom(parent_frame)

    def disable(self):
        frame = self.cate
        if self.darkMode:
            for child1 in frame.winfo_children():
                child1.configure(background='#333333')
                for child2 in child1.winfo_children():
                    child2.configure(background='#333333')
        else:
            for child1 in frame.winfo_children():
                child1.configure(background='#f0f0f0')
                for child2 in child1.winfo_children():
                    child2.configure(background='#f0f0f0')

    def callChildFrom(self, frame):
        if frame == self.panel[1]:
            self.openChildForm(SaleGUI(self.function))
        elif frame == self.panel[2]:
            self.openChildForm(ProductGUI(self.function))
        elif frame == self.panel[3]:
            self.openChildForm(CategoryGUI(self.function))
        elif frame == self.panel[4]:
            self.openChildForm(RecipeGUI(self.function))
        elif frame == self.panel[5]:
            self.openChildForm(ReceiptGUI(self.function))
        elif frame == self.panel[6]:
            self.openChildForm(BillGUI(self.function))
        elif frame == self.panel[7]:
            self.openChildForm(IngredientGUI(self.function))
        elif frame == self.panel[8]:
            pass
        elif frame == self.panel[9]:
            self.openChildForm(AccountGUI(self.function))
        elif frame == self.panel[10]:
            self.openChildForm(StaffGUI(self.function))
        elif frame == self.panel[11]:
            self.openChildForm(CustomerGUI(self.function))
        elif frame == self.panel[12]:
            pass
        elif frame == self.panel[13]:
            self.openChildForm(DecentralizationGUI(self.function))
        elif frame == self.panel[14]:
            self.openChildForm(SupplierGUI(self.function))


    def openChildForm(self, frame):
        for child in self.function.winfo_children():
            if child != frame:
                child.destroy()
        frame.pack()
        self.function.update()
