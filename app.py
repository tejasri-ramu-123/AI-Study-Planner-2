from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    subjects = request.form["subjects"]
    hours = float(request.form["hours"])
    exam_date = request.form["exam_date"]
    difficulty = request.form["difficulty"]

    # Separate subjects using comma
    subject_list = [s.strip() for s in subjects.split(",")]

    # Calculate time for each subject
    time_per_subject = hours / len(subject_list)

    # Calculate days remaining
    today = datetime.today().date()
    exam = datetime.strptime(exam_date, "%Y-%m-%d").date()

    days_left = (exam - today).days

    return render_template(
        "plan.html",
        subjects=subject_list,
        hours=hours,
        exam_date=exam_date,
        difficulty=difficulty,
        time_per_subject=time_per_subject,
        days_left=days_left
    )


if __name__ == "__main__":
    app.run(debug=True)