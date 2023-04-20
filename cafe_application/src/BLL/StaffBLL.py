from typing import List

from BLL.Manager import Manager
from DAL.StaffDAL import StaffDAL
from DTO.Staff import Staff


class StaffBLL(Manager[Staff]):
    def __init__(self):
        try:
            self.__staffDAL = StaffDAL()
            self.__staffList = self.searchStaffs("DELETED = 0", "STAFF_ID != 'ST00'")
        except Exception:
            pass

    def getStaffDAL(self) -> StaffDAL:
        return self.__staffDAL

    def setStaffDAL(self, staffDAL: StaffDAL) -> StaffDAL:
        self.__staffDAL = staffDAL

    def getStaffList(self) -> list:
        return self.__staffList

    def setStaffList(self, staffList) -> list:
        self.__staffList = staffList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__staffList)

    def addStaff(self, staff: Staff) -> bool:
        if self.getIndex(staff, "PHONE", self.__staffList) != -1:
            print("Can't add new staff. Phone already exists.")
            return False
        self.__staffList.append(staff)
        return self.__staffDAL.addStaff(staff) != 0

    def updateStaff(self, staff: Staff) -> bool:
        self.__staffList[self.getIndex(staff, "STAFF_ID", self.__staffList)] = staff
        return self.__staffDAL.updateStaff(staff) != 0

    def deleteStaff(self, staff: Staff) -> bool:
        self.__staffList.pop(self.getIndex(staff, "STAFF_ID", self.__staffList))
        return self.__staffDAL.deleteStaff(f"STAFF_ID = '{staff.getStaffID()}'") != 0

    def searchStaffs(self, *conditions: str) -> List[Staff]:
        return self.__staffDAL.searchStaffs(*conditions)

    def findStaffsBy(self, conditions: dict) -> list[Staff]:
        staffs = self.__staffList
        for key, value in conditions.items():
            staffs = super().findObjectsBy(key, value, staffs)
        return staffs

    def getAutoID(self) -> str:
        return super().getAutoID("ST", 2, self.searchStaffs("STAFF_ID != 'ST00'"))

    def getValueByKey(self, staff: Staff, key: str) -> object:
        return {
            "STAFF_ID": staff.getStaffID(),
            "NAME": staff.getName(),
            "GENDER": staff.isGender(),
            "DOB": staff.getDateOfBirth(),
            "ADDRESS": staff.getAddress(),
            "PHONE": staff.getPhone(),
            "EMAIL": staff.getEmail(),
            "SALARY": staff.getSalary(),
            "DOENTRY": staff.getDateOfEntry()
        }.get(key, None)
