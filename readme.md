# COMP 3613 A1 - Student Conduct Tracker

## Introduction

This repository contains a code solution for a **Student Conduct Tracker** system, which manages student-staff interactions. This CLI tool assists in tracking student behavior and performance evaluations. It includes functionalities like adding students, managing staff members, adding reviews, and viewing feedback for students.

## Project requirements

The need is for a command-line application that enables staff members to monitor and review student conduct. The requirements are:

- Create Student
- View Students
- Add Reviews for Students
- View Student Reviews

# Commands

| Command                | Description                                                             |
|------------------------|-------------------------------------------------------------------------|
| add_student            | Adds a new student to the database with the given student ID and name.  |
| add_review             | Adds a review for a student by a staff member with the provided rating. |
| search_student         | Displays the details of a student, given their student ID.              |
| view_student_reviews   | Displays all reviews for a given student by their student ID.           |                            

# format to enter command and arguments

| Command                            | Description                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| flask user add_student <student_id> <name>  | Adds a new student with the given student ID and name.                             |
| flask user search_student <student_id>      | Searches for a student and displays their details using the given student ID.       |
| flask user add_review <student_id> <staff_id> <review_text> <rating>  | Adds a review for a student from a staff member with the given rating.  |
| flask user view_reviews <student_id>        | Displays all reviews for the student with the given student ID.                     |

# example of commands

| Command                                              | Description                                                     |
|------------------------------------------------------|-----------------------------------------------------------------|
| `flask user add_student 123 "John Doe"`              | Adds a new student with ID `123` and name "John Doe".           |
| `flask user search_student 123`                      | Searches and displays the details of the student with ID `123`.  |
| `flask user add_review 123 1 "Great progress on reading!" 5` | Adds a review from staff ID `1` for student ID `123` with a rating of `5`. |
| `flask user view_reviews 123`                        | Displays all reviews for the student with ID `123`.              |


### Preparatory Functions

Before using the regular functions, the following command must be run to set up the database:

```bash
$ flask init

$ flask user add_student <student_id> <name>



