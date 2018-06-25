from library import library as app
from flask_mail import Mail, Message
from flask import flash, request, redirect, url_for
import time


"""
# use SSL to send mail
app.config['SECRET_KEY'] = 'logicplus'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'vcr.student@gmail.com'
app.config['MAIL_PASSWORD'] = 'eclassroom'
mail = Mail(app)
"""

# use TLS to send mail
app.config['SECRET_KEY'] = 'logicplus'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'vcr.student@gmail.com'
app.config['MAIL_PASSWORD'] = 'eclassroom'
mail = Mail(app)


class SendMail:
    def sent(self,recipients, subject, body, html=None):
        if 'user_name' not in app.config:
            app.config['user_name'] = "Logicplus"
        msg = Message(subject=subject, reply_to=(app.config['user_name'], app.config['MAIL_USERNAME']), sender=(app.config['user_name'], app.config['MAIL_USERNAME']), recipients=[recipients])
        # msg = Message(subject=subject, reply_to=app.config['MAIL_USERNAME'], sender=app.config['MAIL_USERNAME'], recipients=[recipients])
        msg.body = "%s \n%s" % (body, msg.sender)
        if html is not None:
            msg.html = str(html)
        time.strftime('%A ,%d %B %Y %H:%M:%S')
        mail.connect()
        mail.send(msg)
        print("mail sent")
        return True


@app.route('/mail', methods=['GET', 'POST'])
def rtmail():
    if request.method == 'POST':
        toaddrs = request.form['email_txt']
        subject = request.form['subject_txt']
        msg = request.form['msg_txt']
        if SendMail().sent(toaddrs, subject, msg):
            flash("Email Sent!")
            return redirect(url_for('rtindex'))
    return "Sent"

