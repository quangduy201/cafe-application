from database.run_query import run_query
from management.manager import Manager
from models.medical_procedure import MedicalProcedure

class MedicalProcedureManager(Manager):
    """Manages records in the Medical_Procedure table."""

    def __init__(self):
        table_name = 'Medical_Procedure'
        columns_name = (
            'procedure_id',
            'procedure_name',
            'cost'
        )
        super().__init__(table_name, columns_name)

    @staticmethod
    def get_all_procedures():
        procedures = []
        query = "SELECT * FROM Medical_Procedure"
        results = run_query(query)
        for result in results:
            procedure = MedicalProcedure(*result)
            procedures.append(procedure)
        return procedures

    @staticmethod
    def get_procedure_by_id(procedure_id):
        query = "SELECT * FROM Medical_Procedure WHERE procedure_id = %s"
        values = (procedure_id,)
        result = run_query(query, values)
        if result:
            procedure = MedicalProcedure(*result[0])
            return procedure
        else:
            return None
