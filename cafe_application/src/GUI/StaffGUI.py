from datetime import datetime
from tkinter import *
from tkinter import ttk

from BLL.StaffBLL import StaffBLL
from DTO.Staff import Staff


class StaffGUI(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="blue", width=200, height=720)
        self.staffBLL = StaffBLL()
        self.init_components()

    def init_components(self):
        self.panel1 = Frame(self, bg="#333333", width=680)
        self.panel1.pack(side="left", fill="y")

        self.panel2 = Frame(self, bg="#FFFFFF", width=360)
        self.panel2.pack(side="right", fill="y")

        self.columnNames = self.staffBLL.getStaffDAL().getColumnNames()

        self.tableFrame = Frame(self.panel1, width=660, height=720, bg="#333333", highlightthickness=0, borderwidth=0)
        self.tableFrame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.tableFrame.pack_propagate(False)

        self.table = ttk.Treeview(self.tableFrame, columns=self.columnNames[0:len(self.columnNames)-1], show="headings")
        self.table.heading("0", text="STAFF_ID")
        self.table.heading("1", text="NAME")
        self.table.heading("2", text="GENDER")
        self.table.heading("3", text="DOB")
        self.table.heading("4", text="ADDRESS")
        self.table.heading("5", text="PHONE")
        self.table.heading("6", text="EMAIL")
        self.table.heading("7", text="SALARY")
        self.table.heading("8", text="DOENTRY")
        self.data = self.staffBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)
        self.table.pack(fill=BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tableFrame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="bottom", fill="x")

        self.table.bind('<<TreeviewSelect>>', self.showDetailsStaff)

        self.pnlStaffConfiguration = Frame(self.panel2, bg="#FFFFFF", width=450)
        self.pnlStaffConfiguration.pack(padx=10, pady=10)

        self.labelForm = []
        self.TextFieldsForm = []
        self.row = 0
        self.column = 0
        for i in range(0, len(self.columnNames)-1):
            self.labelForm.append(Label(self.pnlStaffConfiguration, text=self.columnNames[i] + ": ", fg="#000000", bg="#ffffff"))
            self.labelForm[i].grid(row=self.row, column=self.column, padx=20, pady=10)
            self.column = self.column + 1
            if self.columnNames[i] == "STAFF_ID":
                self.TextFieldsForm.append(Entry(self.pnlStaffConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].insert(0, self.staffBLL.getAutoID())
                self.TextFieldsForm[len(self.TextFieldsForm)-1].configure(state='readonly')
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            elif self.columnNames[i] == "GENDER":
                self.cbbGender = ttk.Combobox(self.pnlStaffConfiguration, values=["Nam", "Nữ"], width=27)
                self.cbbGender.configure(state="readonly")
                self.cbbGender.grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)
            else:
                self.TextFieldsForm.append(Entry(self.pnlStaffConfiguration, fg="#000000", bg="#ffffff", width=30))
                self.TextFieldsForm[len(self.TextFieldsForm)-1].grid(row=self.row, column=self.column, padx=20, pady=10, ipady=4)

            self.row = self.row + 1
            self.column = 0

        self.showImage = Frame(self.panel2, width=350, height=150, bg="#FFFFFF")
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

    def showDetailsStaff(self, event):
        for row in self.table.selection():
            item = self.table.item(row)
            values = item["values"]

            self.TextFieldsForm[0].configure(state="normal")
            self.TextFieldsForm[0].delete(0, END)
            self.TextFieldsForm[0].insert(END, values[0])
            self.TextFieldsForm[0].configure(state="readonly")

            self.TextFieldsForm[1].delete(0, END)
            self.TextFieldsForm[1].insert(END, values[1])

            self.cbbGender.configure(state="normal")
            self.cbbGender.set(values[2])
            self.cbbGender.configure(state="readonly")

            self.TextFieldsForm[2].delete(0, END)
            self.TextFieldsForm[2].insert(END, values[3])

            self.TextFieldsForm[3].delete(0, END)
            self.TextFieldsForm[3].insert(END, values[4])

            self.TextFieldsForm[4].delete(0, END)
            self.TextFieldsForm[4].insert(END, values[5])

            self.TextFieldsForm[5].delete(0, END)
            self.TextFieldsForm[5].insert(END, values[6])

            self.TextFieldsForm[6].delete(0, END)
            self.TextFieldsForm[6].insert(END, values[7])

            self.TextFieldsForm[7].delete(0, END)
            self.TextFieldsForm[7].insert(END, values[8])

            self.btAdd.configure(state="disabled")
            self.btUpd.configure(state="normal")
            self.btDel.configure(state="normal")

    def loadTable(self):
        for item in self.table.get_children():
            self.table.delete(item)
        self.data = self.staffBLL.getData()
        for row in self.data:
            self.table.insert('', END, values = row)

    def add(self):
        gender = True if self.cbbGender.get() == "Nam" else False
        dob = datetime.strptime(self.TextFieldsForm[2].get(), "%Y-%m-%d").date()
        doe = datetime.strptime(self.TextFieldsForm[7].get(), "%Y-%m-%d").date()
        self.newStaff = Staff(self.TextFieldsForm[0].get(), self.TextFieldsForm[1].get(), gender, dob, self.TextFieldsForm[3].get(), self.TextFieldsForm[4].get(), self.TextFieldsForm[5].get(), float(self.TextFieldsForm[6].get()), doe, False)
        self.staffBLL.addStaff(self.newStaff)
        self.ref()

    def upd(self):
        gender = True if self.cbbGender.get() == "Nam" else False
        dob = datetime.strptime(self.TextFieldsForm[2].get(), "%Y-%m-%d").date()
        doe = datetime.strptime(self.TextFieldsForm[7].get(), "%Y-%m-%d").date()
        self.newStaff = Staff(self.TextFieldsForm[0].get(), self.TextFieldsForm[1].get(), gender, dob, self.TextFieldsForm[3].get(), self.TextFieldsForm[4].get(), self.TextFieldsForm[5].get(), float(self.TextFieldsForm[6].get()), doe, False)
        self.staffBLL.updateStaff(self.newStaff)
        self.loadTable()

    def dele(self):
        self.staffBLL.deleteStaff(Staff(staffID = self.TextFieldsForm[0].get()))
        self.ref()

    def ref(self):
        self.loadTable()
        self.TextFieldsForm[0].configure(state="normal")
        self.TextFieldsForm[0].delete(0, END)
        self.TextFieldsForm[0].insert(END, self.staffBLL.getAutoID())
        self.TextFieldsForm[0].configure(state="readonly")
        for i in range(1, len(self.TextFieldsForm)):
            self.TextFieldsForm[i].delete(0, END)

        self.cbbGender.configure(state="normal")
        self.cbbGender.delete(0, END)
        self.cbbGender.configure(state="readonly")
        self.btAdd.configure(state="normal")
        self.btUpd.configure(state="disabled")
        self.btDel.configure(state="disabled")





