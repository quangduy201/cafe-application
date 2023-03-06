from database.run_query import run_query

class MedicalProcedure:
    def __init__(self, procedure_id, procedure_name, cost):
        self.procedure_id = procedure_id
        self.procedure_name = procedure_name
        self.cost = cost

    def save(self):
        if self.procedure_id:
            # Update existing medical procedure
            query = "UPDATE Medical_Procedure SET procedure_name = %s, cost = %s WHERE procedure_id = %s"
            values = (self.procedure_name, self.cost, self.procedure_id)
            run_query(query, values)
        else:
            # Insert new medical procedure
            query = "INSERT INTO Medical_Procedure (procedure_name, cost) VALUES (%s, %s)"
            values = (self.procedure_name, self.cost)
            self.procedure_id = run_query(query, values)

    def delete(self):
        query = "DELETE FROM Medical_Procedure WHERE procedure_id = %s"
        values = (self.procedure_id,)
        run_query(query, values)
