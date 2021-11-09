# © Jtech 2021


from flask import Flask, render_template, request, flash
from forms import ContactForm
import pandas as pd
import smtplib


flask_app = Flask(__name__)
flask_app.secret_key = b'\xf7\xadU\x1ae\x02\x04\xe341\x11\xa6.\x03\xee\xb0:dO\xb2\xfb\xd2\xb9\x9d'




@flask_app.route('/', methods=["GET", "POST"])
def get_contact():
    form = ContactForm()
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        #PANDAS
        res = pd.DataFrame({'name': name , 'email': email , 'subject': subject , 'message': message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        #SMTP
        message = 'subject: {0}\n\n{1}From: {2}'.format(subject, message, email)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("jtech.help2021@gmail.com", "Jtech2021")
        server.sendmail(email, "jtech.help2021@gmail.com", message.encode("utf-8"))
        server.quit()
        flash("Request sended / požadavek odeslán")
        return render_template("post_index.jinja")


    else:
        return render_template("indexx.jinja", form=form)


#Main loop
if __name__ == "__main__":
    debug = True
    host = "0.0.0.0"
    flask_app.run(host, debug=debug)

