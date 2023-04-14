from typing import List

from DAL.Manager import Manager
from DTO.Staff import Staff


class StaffDAL(Manager):
    def __init__(self):
        super().__init__("staff", [
            "STAFF_ID",
            "NAME",
            "GENDER",
            "DOB",
            "ADDRESS",
            "PHONE",
            "EMAIL",
            "SALARY",
            "DOENTRY",
            "DELETED"
        ])

    def convertToStaffs(self, data: List[List[object]]) -> List[Staff]:
        return self.convert(data, lambda row: Staff(
            row['STAFF_ID'],
            row['NAME'],
            row['GENDER'],
            row['DOB'],
            row['ADDRESS'],
            row['PHONE'],
            row['EMAIL'],
            row['SALARY'],
            row['DOENTRY'],
            bool(row['DELETED'])
        ))

    def addStaff(self, staff: Staff) -> int:
        try:
            return self.create(
                staff.getStaffID(),
                staff.getName(),
                staff.isGender(),
                staff.getDateOfBirth(),
                staff.getAddress(),
                staff.getPhone(),
                staff.getEmail(),
                staff.getSalary(),
                staff.getDateOfEntry(),
                False
            ) # staff khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in StaffDAL.addStaff(): {e}")
        return 0

    def updateStaff(self, staff: Staff) -> int:
        try:
            updateValues = [
                staff.getStaffID(),
                staff.getName(),
                staff.isGender(),
                staff.getDateOfBirth(),
                staff.getAddress(),
                staff.getPhone(),
                staff.getEmail(),
                staff.getSalary(),
                staff.getDateOfEntry(),
                staff.isDeleted()
            ]
            return self.update(updateValues, f"STAFF_ID = '{staff.getStaffID()}'")
        except Exception as e:
            print(f"Error occurred in StaffDAL.updateStaff(): {e}")
        return 0

    def deleteStaff(self, *conditions: str) -> int:
        try:
            updateValues = [True]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in StaffDAL.deleteStaff(): {e}")
        return 0

    def searchStaffs(self, *conditions: str) -> List[Staff]:
        try:
            return self.convertToStaffs(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in StaffDAL.searchStaffs(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("ST", 2)
        except Exception as e:
            print(f"Error occurred in StaffDAL.getAutoID(): {e}")
        return ""
