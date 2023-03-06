from database.run_query import run_query

class Owner:
    def __init__(self, owner_id, name, phone, email, address):
        self.owner_id = owner_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def save(self):
        if self.owner_id:
            # Update existing owner
            query = "UPDATE Owner SET name = %s, phone = %s, email = %s, address = %s WHERE owner_id = %s"
            values = (self.name, self.phone, self.email, self.address, self.owner_id)
            run_query(query, values)
        else:
            # Insert new owner
            query = "INSERT INTO Owner (name, phone, email, address) VALUES (%s, %s, %s, %s)"
            values = (self.name, self.phone, self.email, self.address)
            self.owner_id = run_query(query, values)

    def delete(self):
        query = "DELETE FROM Owner WHERE owner_id = %s"
        values = (self.owner_id,)
        run_query(query, values)
