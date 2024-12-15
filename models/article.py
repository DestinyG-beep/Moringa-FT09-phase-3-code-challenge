class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'
    
    @property
    def id (self):
        return self._id
    
    @id.setter
    def id (self, id):
        self._id = id 

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, content):
        if isinstance(content, str) and len(content):
            self._content = content
    
    @staticmethod
    def create(cursor, title, content, author_id, magazine_id):
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',(title, content, author_id, magazine_id))
        return cursor.lastrowid
    
    @staticmethod
    def get_by_id(cursor, id):
        cursor.execute('SELECT * FROM articles WHERE id = ?', (id,))
        row = cursor.fetchone()
        return Article(row['id'], row['title'], row['content'], row['author_id'], row['magazine_id']) if row else None
        