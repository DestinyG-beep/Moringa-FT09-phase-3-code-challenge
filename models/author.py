from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.save_db()

    def __repr__(self):
        return f'<Author {self.name}>'
    
    def save_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

  
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id    


    @property
    def name(self):
        return self._name
