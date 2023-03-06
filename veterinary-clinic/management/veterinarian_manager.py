from database.run_query import run_query
from management.manager import Manager
from models.veterinarian import Veterinarian

class VeterinarianManager(Manager):
    """Manages records in the Veterinarian table."""

    def __init__(self) -> None:
        table_name = 'Veterinarian'
        columns_name = (
            'vet_id',
            'name',
            'dob',
            'gender',
            'degree',
            'phone',
            'email',
            'address'
        )
        super().__init__(table_name, columns_name)

    @staticmethod
    def get_all_veterinarians():
        veterinarians = []
        query = "SELECT * FROM Veterinarian"
        results = run_query(query)
        for result in results:
            veterinarian = Veterinarian(*result)
            veterinarians.append(veterinarian)
        return veterinarians

    @staticmethod
    def get_veterinarian_by_id(vet_id):
        query = "SELECT * FROM Veterinarian WHERE vet_id = %s"
        values = (vet_id,)
        result = run_query(query, values)
        if result:
            veterinarian = Veterinarian(*result[0])
            return veterinarian
        else:
            return None
