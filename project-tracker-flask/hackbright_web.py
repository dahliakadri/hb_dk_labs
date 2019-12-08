"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    project_grade_tup = hackbright.get_grades_by_github(github)
    print(project_grade_tup)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            project_grade_tup=project_grade_tup)
    #                       *orange "first" is what we'll be passing into 
    #                           template IE {{ first }}
    #                       *white "first" is the value coming from the 
    #                           get_student)by_github function
    return html

@app.route("/project")
def list_project_info():
    title = request.args.get('title')

    title, description, max_grade = hackbright.get_project_by_title(title)

    html = render_template("project_info.html",
                            title=title,
                            description=description,
                            max_grade=max_grade)
    return html
    
@app.route("/student-form")
def student_form():
    html = render_template("new_student.html")
    return html


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first = request.form.get('firstname')
    last = request.form.get('lastname')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    html = render_template("new_student_added.html",
                            first=first,
                            last=last,
                            github=github)

    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
