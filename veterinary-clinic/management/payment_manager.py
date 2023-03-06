from database.run_query import run_query
from management.manager import Manager
from models.payment import Payment

class PaymentManager(Manager):
    """Manages records in the Payment table."""

    def __init__(self):
        table_name = 'Payment'
        columns_name = (
            'payment_id',
            'payment_date',
            'amount',
            'appointment_id',
            'procedure_id'
        )
        super().__init__(table_name, columns_name)

    @staticmethod
    def get_all_payments():
        payments = []
        query = "SELECT * FROM Payment"
        results = run_query(query)
        for result in results:
            payment = Payment(*result)
            payments.append(payment)
        return payments

    @staticmethod
    def get_payment_by_id(payment_id):
        query = "SELECT * FROM Payment WHERE payment_id = %s"
        values = (payment_id,)
        result = run_query(query, values)
        if result:
            payment = Payment(*result[0])
            return payment
        else:
            return None
