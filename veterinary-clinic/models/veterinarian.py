from database.run_query import run_query

class Veterinarian:
    def __init__(self, vet_id, name, dob, gender, degree, phone, email, address):
        self.vet_id = vet_id
        self.name = name
        self.dob = dob
        self.gender = gender
        self.degree = degree
        self.phone = phone
        self.email = email
        self.address = address

    def save(self):
        if self.vet_id:
            # Update existing veterinarian
            query = "UPDATE Veterinarian SET name = %s, dob = %s, gender = %s, degree = %s, phone = %s, email = %s, address = %s WHERE vet_id = %s"
            values = (self.name, self.dob, self.gender, self.degree, self.phone, self.email, self.address, self.vet_id)
            run_query(query, values)
        else:
            # Insert new veterinarian
            query = "INSERT INTO Veterinarian (name, dob, gender, degree, phone, email, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (self.name, self.dob, self.gender, self.degree, self.phone, self.email, self.address)
            self.vet_id = run_query(query, values)

    def delete(self):
        query = "DELETE FROM Veterinarian WHERE vet_id = %s"
        values = (self.vet_id,)
        run_query(query, values)
