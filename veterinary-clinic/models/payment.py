from database.run_query import run_query

class Payment:
    def __init__(self, payment_id, payment_date, amount, appointment_id, procedure_id):
        self.payment_id = payment_id
        self.payment_date = payment_date
        self.amount = amount
        self.appointment_id = appointment_id
        self.procedure_id = procedure_id

    def save(self):
        if self.payment_id:
            # Update existing payment
            query = "UPDATE Payment SET payment_date = %s, amount = %s, appointment_id = %s, procedure_id = %s WHERE payment_id = %s"
            values = (self.payment_date, self.amount, self.appointment_id, self.procedure_id, self.payment_id)
            run_query(query, values)
        else:
            # Insert new payment
            query = "INSERT INTO Payment (payment_date, amount, appointment_id, procedure_id) VALUES (%s, %s, %s, %s)"
            values = (self.payment_date, self.amount, self.appointment_id, self.procedure_id)
            self.payment_id = run_query(query, values)

    def delete(self):
        query = "DELETE FROM Payment WHERE payment_id = %s"
        values = (self.payment_id,)
        run_query(query, values)
