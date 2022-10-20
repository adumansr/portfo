
import csv
from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# @app.route("/components.html")
# def component():
#     return render_template('components.html')


# @app.route("/work.html")
# def work():
#     return render_template('work.html')


# @app.route("/works.html")
# def works():
#     return render_template("works.html")


# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")


# @app.route("/about.html")
# def about():

#     return render_template('about.html')

def save_to_db(data):
    with open('database.csv', mode='a', newline='') as db_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(db_csv, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_to_db(data)

    return redirect('thankyou.html')
