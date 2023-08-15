from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"

debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

RESPONSES = "responses"


@app.route("/")
def home():
    """Survey home page"""

    return render_template("home.html", survey=survey)


@app.route("/begin", methods=["POST"])
def start_survey():
    """Clear the session of responses."""

    session[RESPONSES] = []

    return redirect("/questions/0")


@app.route("/answer", methods=["POST"])
def answers():
    """Save response and redirect to next question."""
    choice = request.form["answer"]

    responses = session[RESPONSES]
    responses.append(choice)
    session[RESPONSES] = responses

    if len(responses) == len(survey.questions):
        return redirect("/complete")

    else:
        return redirect(f"/questions/{len(responses)}")


@app.route("/questions/<int:num>")
def survey_questions(num):
    responses = session.get(RESPONSES)

    if responses is None:
        return redirect("/")
    if len(responses) == len(survey.questions):
        return redirect("/complete")
    if len(responses) != num:
        flash(f"Invalid question id: {num}.")
        return redirect(f"/questions/{len(responses)}")
    question = survey.questions[num]
    return render_template("questions.html", question_num=num, question=question)


@app.route("/complete")
def complete():
    """End of survey"""
    return render_template("complete.html")
