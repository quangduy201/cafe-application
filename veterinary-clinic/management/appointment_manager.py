from database.run_query import run_query
from management.manager import Manager
from models.appointment import Appointment

class AppointmentManager(Manager):
    """Manages records in the Appointment table."""

    def __init__(self):
        table_name = 'Appointment'
        columns_name = (
            'appointment_id',
            'appointment_date',
            'animal_id',
            'vet_id'
        )
        super().__init__(table_name, columns_name)

    @staticmethod
    def get_all_appointments():
        appointments = []
        query = "SELECT * FROM Appointment"
        results = run_query(query)
        for result in results:
            appointment = Appointment(*result)
            appointments.append(appointment)
        return appointments

    @staticmethod
    def get_appointment_by_id(appointment_id):
        query = "SELECT * FROM Appointment WHERE appointment_id = %s"
        values = (appointment_id,)
        result = run_query(query, values)
        if result:
            appointment = Appointment(*result[0])
            return appointment
        else:
            return None
