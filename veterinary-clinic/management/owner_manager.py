from database.run_query import run_query
from management.manager import Manager
from models.owner import Owner

class OwnerManager(Manager):
    """Manages records in the Owner table."""

    def __init__(self):
        table_name = 'Owner'
        columns_name = (
            'owner_id',
            'name',
            'phone',
            'email',
            'address'
        )
        super().__init__(table_name, columns_name)

    @staticmethod
    def get_all_owners():
        owners = []
        query = "SELECT * FROM Owner"
        results = run_query(query)
        for result in results:
            owner = Owner(*result)
            owners.append(owner)
        return owners

    @staticmethod
    def get_owner_by_id(owner_id):
        query = "SELECT * FROM Owner WHERE owner_id = %s"
        values = (owner_id,)
        result = run_query(query, values)
        if result:
            owner = Owner(*result[0])
            return owner
        else:
            return None
