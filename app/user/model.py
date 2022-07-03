from app.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    email = db.Column(db.String(50))
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean, default=False)

    def __init__(self, firstName,lastName, email, password,admin):
        self.firstName= firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.admin = admin

    def __repr__(self):
        return f'<User id:{self.id} firstName:{self.firstName} lastName:{self.lastName} is_admin:{self.admin}>'