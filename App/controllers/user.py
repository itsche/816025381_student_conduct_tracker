from App.models import User
from App.models import Student
from App.models import Review
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

#search for students
def search_student(student_id):                                 
    student = Student.query.filter_by(id=student_id).first()
    if student:
        return student.get_json()
    else:
        return {"message": "Student doesn't exist."}

#add students to database
def add_student(student_id, student_name):
    student = Student.query.filter_by(id=student_id).first()
    if student:
        return {"message": "Student already exists."}

    new_student = Student(id=student_id, name=student_name)
    db.session.add(new_student)
    db.session.commit()

    return {"message": f"Student {student_name} added successfully."}

#add review to a specific student
def add_review(student_id, staff_id, review_text, rating):
    student = Student.query.get(student_id)
    staff = User.query.get(staff_id)

    if not student:
        return {"message": "Student not found."}
    if not staff:
        return {"message": "Staff not found."}

    new_review = Review(student_id=student_id, staff_id=staff_id, review_text=review_text, rating=rating)
    db.session.add(new_review)
    db.session.commit()
    return {"message": f"Review added successfully"}

#view reviews for a particular student
def view_student_reviews(student_id):
    student = Student.query.get(student_id)
    if not student:
        return {"message": "Student not found."}

    reviews = Review.query.filter_by(student_id=student_id).all()
    if not reviews:
        return {"message": "No reviews found for this student."}

    review_list = [review.get_json() for review in reviews]
    return {"reviews": review_list}