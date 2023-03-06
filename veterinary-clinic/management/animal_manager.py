from database.run_query import run_query
from management.manager import Manager
from models.animal import Animal

class AnimalManager(Manager):
    """Manages records in the Animal table."""

    def __init__(self):
        table_name = 'Animal'
        columns_name = (
            'animal_id',
            'name',
            'species',
            'gender',
            'age',
            'weight',
            'owner_id'
        )
        super().__init__(table_name, columns_name)

    @staticmethod
    def get_all_animals():
        animals = []
        query = "SELECT * FROM Animal"
        results = run_query(query)
        for result in results:
            animal = Animal(*result)
            animals.append(animal)
        return animals

    @staticmethod
    def get_animal_by_id(animal_id):
        query = "SELECT * FROM Animal WHERE animal_id = %s"
        values = (animal_id,)
        result = run_query(query, values)
        if result:
            animal = Animal(*result[0])
            return animal
        else:
            return None
