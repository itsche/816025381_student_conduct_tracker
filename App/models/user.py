from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model): #using it as staff
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    reviews = db.relationship('Review', backref='student', lazy=True)

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'reviews': [review.get_json() for review in self.reviews]
        }

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    staff = db.relationship('User', backref='reviews')

    def __init__(self, student_id, staff_id, review_text, rating):
        self.student_id = student_id
        self.staff_id = staff_id
        self.review_text = review_text
        self.rating = rating

    def get_json(self):
        staff_username = self.staff.username
        return {
            'review_text': self.review_text,
            'rating': self.rating,
            'staff_username': staff_username
        }

