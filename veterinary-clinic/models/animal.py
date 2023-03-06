from database.run_query import run_query

class Animal:
    def __init__(self, animal_id, name, species, gender, age, weight, owner_id):
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.gender = gender
        self.age = age
        self.weight = weight
        self.owner_id = owner_id

    def save(self):
        if self.animal_id:
            # Update existing animal
            query = "UPDATE Animal SET name = %s, species = %s, gender = %s, age = %s, weight = %s, owner_id = %s WHERE animal_id = %s"
            values = (self.name, self.species, self.gender, self.age, self.weight, self.owner_id, self.animal_id)
            run_query(query, values)
        else:
            # Insert new animal
            query = "INSERT INTO Animal (name, species, gender, age, weight, owner_id) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (self.name, self.species, self.gender, self.age, self.weight, self.owner_id)
            self.animal_id = run_query(query, values)

    def delete(self):
        query = "DELETE FROM Animal WHERE animal_id = %s"
        values = (self.animal_id,)
        run_query(query, values)
