"""Hackbright Project Tracker.

A front-end for a database that allows users to work with students, class
projects, and the grades students receive in class projects.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hackbright'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def get_student_by_github(github):
    """Given a GitHub account name, print info about the matching student."""

    QUERY = """
        SELECT first_name, last_name, github
        FROM students
        WHERE github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})

    row = db_cursor.fetchone()
    if row:
        print("Student: {} {}\nGitHub account: {}".format(row[0], row[1], row[2]))
    else:
        print("Not a valid student")



def make_new_student(first_name, last_name, github):
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student to the
    database and print a confirmation message.
    """
    QUERY = """
        INSERT INTO students (first_name, last_name, github)
            VALUES (:first_name, :last_name, :github)
        """

    db.session.execute(QUERY, {'first_name': first_name,
                                'last_name': last_name,
                                'github': github})
    db.session.commit()

    print(f'Successfully added student: {first_name} {last_name}')


def get_project_by_title(title):
    """Given a project title, print information about the project."""
    QUERY = """
        SELECT title, description, max_grade
        FROM projects
        WHERE title = :project_title
        """
    db_cursor = db.session.execute(QUERY, {'project_title': title})

    row = db_cursor.fetchone()
    if row:
        print("{}: {}. Max Grade is {}".format(row[0], row[1], row[2]))
    else:
        print("Project title does not exist")

def get_grade_by_github_title(github, title):
    """Print grade student received for a project."""
    github = github
    title = title

    QUERY = """
        SELECT grade
        FROM grades
        WHERE student_github = :github
        AND project_title = :title
        """
    db_cursor = db.session.execute(QUERY, {'github': github,
                                            'title': title})

    row = db_cursor.fetchone()

    print("{} received a grade of {} for {}.".format(github, row[0], title))


def assign_grade(github, title, grade):
    """Assign a student a grade on an assignment and print a confirmation."""
    QUERY = """
        INSERT INTO grades (student_github, project_title, grade)
            VALUES(:github, :title, :grade)
            """
    db.session.execute(QUERY, {'github':github, 'title':title, 'grade':grade})
    db.session.commit()

    print('For {} added a grade of {} for project {}.'.format(github, grade, title))

def make_new_project(project_title, description, max_grade):
    """Add a new project and print confirmation.

    Given a project title, description, and max grade, add project to the
    database and print a confirmation message.
    """
    QUERY = """
        INSERT INTO projects (title, description, max_grade)
            VALUES(:project_title, :description, :max_grade)
    """
    db.session.execute(QUERY, {'project_title':project_title, 'description':description, 'max_grade':max_grade})
    db.session.commit()

    print('{} was added to DB. Project description: {}. Max Grade: {}'.format(project_title, description, max_grade))

def get_grades_by_student(github):
    """ Get all grades for a student, given their github handle."""
    QUERY = """
        SELECT project_title, grade
        FROM grades
        WHERE student_github = :github
        """
    db_cursor = db.session.execute(QUERY, {'github':github})
    rows = db_cursor.fetchall()

    for row in rows:
        print('Title: {} \n Grade: {}'.format(row[0], row[1]))


def handle_input():
    """Main loop.

    Repeatedly prompt for commands, performing them, until 'quit' is received
    as a command.
    """

    command = None

    while command != "quit":
        input_string = input("HBA Database> ")
        tokens = input_string.split('|')
        command = tokens[0].lower()
        args = tokens[1:]

        if command == "student":
            if len(args) != 1:
                print('Invalid number of arguments. Expect 1')
            else:
                github = args[0]
                get_student_by_github(github)

        elif command == "new_student":
            if len(args) != 3:
                print("Invalid number of arguments. Expect 3")
            else:
                first_name, last_name, github = args  # unpack!
                make_new_student(first_name, last_name, github)
        
        elif command == "assign_grade":
            if len(args) != 3:
                print("Invalid number of arguments. Expect 3.")
            else:
                github, title, grade = args
                assign_grade(github, title, grade)
       
        elif command == "get_grade_by_title":
            if len(args) != 2:
                print("Invalid number of arguments. Expect 2")
            else:
                github, title = args
                get_grade_by_github_title(github, title)

        elif command == "get_project_by_title":
            if len(args) != 1:
                print("Invalid number of arguments. Expect 1.")
            else:
                title = args[0]
                get_project_by_title(title)

        elif command == "make_new_student":
            if len(args) != 3:
                print("Invalid number of arguments. Expect 3.")
            else:
                first_name, last_name, github = args
                make_new_student(first_name, last_name, github)

        elif command == "make_new_project":
            if len(args) != 3:
                print("Invalid number of arguments. Expect 3.")
            else:
                project_title, description, max_grade = args
                make_new_project(project_title, description, max_grade)

        elif command == "get_grades_by_student":
            if len(args) != 1:
                print("Invalid number of arguments. Expect 1.")
            else:
                github = args[0]
                get_grades_by_student(github)

        else:
            if command != "quit":
                print("Invalid Entry. Try again.")


if __name__ == "__main__":
    connect_to_db(app)
    print("Seperate arguments by '|'")
    handle_input()

    # To be tidy, we close our database connection -- though,
    # since this is where our program ends, we'd quit anyway.

    db.session.close()
