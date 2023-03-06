from database.run_query import run_query

class Appointment:
    def __init__(self, appointment_id, appointment_date, animal_id, vet_id):
        self.appointment_id = appointment_id
        self.appointment_date = appointment_date
        self.animal_id = animal_id
        self.vet_id = vet_id

    def save(self):
        if self.appointment_id:
            # Update existing appointment
            query = "UPDATE Appointment SET appointment_date = %s, animal_id = %s, vet_id = %s WHERE appointment_id = %s"
            values = (self.appointment_date, self.animal_id, self.vet_id, self.appointment_id)
            run_query(query, values)
        else:
            # Insert new appointment
            query = "INSERT INTO Appointment (appointment_date, animal_id, vet_id) VALUES (%s, %s, %s)"
            values = (self.appointment_date, self.animal_id, self.vet_id)
            self.appointment_id = run_query(query, values)

    def delete(self):
        query = "DELETE FROM Appointment WHERE appointment_id = %s"
        values = (self.appointment_id,)
        run_query(query, values)
