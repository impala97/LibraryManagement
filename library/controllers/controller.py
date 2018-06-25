from flask import url_for, redirect, request, render_template, jsonify, g
from library import library as app, session_manager
from flask_login import login_required
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user

from ..model.user import user, model_user
from ..model.otp import otp as otp_control
from .chat import chat
from .mail import SendMail


@session_manager.user_loader
def load_user(user_id):
    return model_user(user_id=user_id).get_user()


@app.route('/', methods=['GET', 'POST'])
def rtlogin():
    if request.method == 'POST':
        print(request.form)
        next_page = request.form['next_page']
        if not next_page or url_parse(next_page).netloc != '' or next_page == '/logout' or next_page == '/' or next_page == '/lock':
            next_page = url_for('rtindex')

        print("next_page==", next_page)

        """if g.user is not None and g.user.is_authenticated is True:
            print("g.user.is_authenticated==", g.user.is_authenticated)
            print("g.user.user_id==",g.user.user_id)
            return redirect(next_page)"""

        username = request.form['un_txt']
        if username is '' or request.form['pwd_txt'] is '':
            return jsonify(error='True', errstr='Please Enter Username Or Password.')
        else:
            row = user().do_login(username=username)
            print("rtlogin==row==len==", len(row))
            if len(row) > 0:
                if row[0][8] is True:
                    if row[0][2] == request.form['pwd_txt']:
                        if user().update_login(row[0][0]) is True:
                            app.config['user_name'] = username

                            var_set = {'user_id': row[0][0], 'username': row[0][1], 'email': row[0][3], 'auth': True, 'pwd': row[0][2]}
                            app_user = model_user(**var_set)
                            if 'remember_me' not in request.form:
                                remember = False
                            else:
                                remember = request.form['remember_me']
                            from datetime import timedelta
                            print(1)

                            login_user(app_user, remember=remember, duration=timedelta(minutes=3))
                            g.user = current_user
                            print("Successful Login!!!")
                            return jsonify(url=next_page, error='False')
                        else:
                            return jsonify(error='True', errstr="Something Went Wrong.")
                    else:
                        return jsonify(error='True', errstr="Password Does Not Match.")
                else:
                    return jsonify(error='True', errstr="You'er not allowed anymore to access this system.")
            else:
                return jsonify(error='True', errstr='Invalid Username')
    next_page = request.args.get('next', '')
    if not next_page or url_parse(next_page).netloc != '' or next_page == '/logout' or next_page == '/':
        next_page = url_for('rtindex')
    return render_template('master/login.html', title='Library | Login', next=next_page)


@app.route('/register', methods=['GET', 'POST'])
def rtregister():
    if request.method == 'POST':
        print("rtregister==", request.method)
        un = request.form['un_txt']
        email = request.form['email_txt']
        phone = request.form['phone_txt']
        pwd = request.form['pwd_txt']
        cpwd = request.form['cpwd_txt']
        print(request.form)
        if un != '' or pwd != '' or cpwd != '' or email != '' or phone != '':
            if pwd != cpwd:
                return jsonify(errstr='Password Did Not Match.')
            elif pwd == cpwd:
                print("result==", len(user().do_login(username=un)))
                if len(user().do_login(username=un)) == 0:
                    response = user().adduser(un,pwd,email,phone)
                    print(response)
                    if response == un:
                        return jsonify(error='False', url=url_for('rtlogin'), errstr="Successfully Registered.")
                    else:
                        return jsonify(errstr="Something went wrong.!")
                else:
                    return jsonify(errstr="User already exists!")
        else:
            return jsonify(errstr="Make sure that you input all the fields..")
    data = {'title': 'Library | Registeration'}
    return render_template('master/register.html', **data)


@login_required
@app.route('/home')
@app.route('/index', methods=['GET'])
def rtindex():
    if request.method == 'POST':
        return "index==post"
    elif request.method == 'GET':
        print("rtindex==GET==", current_user.is_authenticated)
        chat_data = chat().getchat()
        count = dict()
        count["user"] = user().usercount()
        """"""
        count["fees"] = 0  # invoice().getFeeSumByAid()
        count["student"] = 0  # admission().coountid()
        count["faculty"] = 0  # faculty().countid()
        return render_template('master/index.html', chat_data=chat_data, title='Library | Index', **count)


@app.route('/forgetpwd', methods=['GET', 'POST'])
def rtfpwd():
    if request.method == 'POST':
        print(request.form)
        user_email = request.form['email_txt']
        user_data = user().do_login(email=user_email)
        if len(user_data) == 1:
            from ..otp import create_otp
            generated_otp = create_otp().generate_otp()
            last_otp_id = otp_control().add(user_data[0][0], generated_otp=generated_otp)
            print(user().update_otp_id(user_data[0][0], last_otp_id))
            if user().update_otp_id(user_data[0][0], last_otp_id) is True:
                subject = "OTP for Change Password"
                line1 = "dear {},\n".format(user_data[0][1])
                line2 = "We detected that you are trying to change password.\n"
                line3 = "Your username is : {}\n".format(user_data[0][1])
                line4 = "Your email address is : {}\n".format(user_data[0][3])
                line5 = "Your One Time Password is : {} \n".format(generated_otp)
                line6 = "For security reasons, please do not share this OTP with anyone.\n\nThank You,\nTeam Library."
                body = "{}{}{}{}{}{}".format(line1.title(),line2,line3,line4,line5, line6)
                print(body)
                del line1, line2, line3, line4, line5, line6
                mail_send = SendMail().sent(recipients=user_data[0][3], subject=subject, body=body)
                # mail_send = True
                if mail_send is True:
                    return jsonify(error="False", errstr="Enter OTP before time's up!!!", user_id=user_data[0][0])
                else:
                    return jsonify(error='True', errstr='Sorry for inconsistency right now we are unable to send mail.')
            else:
                return jsonify(error=True, errstr='Something Went Wrong!!')
        elif len(user_data) > 1:
            return jsonify(error="True", errstr="This email address is associated with many accounts..Contact to support team.")
        else:
            return jsonify(error="True", errstr="Invalid Email Address.")
    else:
        return render_template('master/forgetpwd.html', title="Library | ForgetPWD")


@app.route('/otp', methods=['POST'])
def otp():
    if request.method == 'POST':
        print(request.form)
        if request.form['otp_txt'] != '':
            expired = False
            if expired is False:
                print(request.form)
                user_otp = otp_control().get(request.form['user_id'])
                print("generated_otp=",user_otp[0][2], user_otp[0][3])
                current_date = user().currentdate()
                print()
                if current_date <= str(user_otp[0][3]) is not True:
                    if request.form['otp_txt'] == user_otp[0][2]:
                        return jsonify(error='False')
                    else:
                        return jsonify(error='True', errstr='OTP did not match!!!')
                else:
                    return jsonify(error='True', errstr='OTP expired!!')
            else:
                return jsonify(error='True', errstr='Please try again, OTP is expired!')
        else:
            return jsonify(error='True', errstr='Please Enter OTP...')


@app.route('/changepwd', methods=['POST'])
def changepwd():
    if request.method == 'POST':
        user_id = request.form['user_id']
        pwd = request.form['pwd_txt']
        cpwd = request.form['cpwd_txt']
        if pwd != '' and cpwd != '':
            if pwd == cpwd:
                if user().changepwd(int(user_id), pwd):
                    return jsonify(error='False',url=url_for('rtlogin'))
                else:
                    return jsonify(error='True', errstr='Something went wrong!!')
            else:
                return jsonify(error='True', errstr='Confirm Password did not match!!')
        else:
            return jsonify(error='True', errstr='Please fill all the input fields..')


@app.route('/changepassword', methods=['GET', 'POST'])
@login_required
def rtcpwd():
    if request.method == 'POST':
        print(request.method)
        print(request.form)
        old_pwd = request.form['old_pwd']
        new_pwd = request.form['new_pwd']
        cnew_pwd = request.form['cnew_pwd']

        if new_pwd == cnew_pwd:
            valid = user().changepwd(int(current_user.user_id), new_pwd, old_pwd)
            if valid is True:
                return jsonify(url=url_for('rtindex'))
    return render_template('master/changepwd.html', title="Library | Change Password")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    print("logout=get")
    user().update_logout(current_user.user_name, current_user.user_id)
    print("logout==auth==", current_user.is_authenticated)
    # logout_user()
    return redirect(url_for('lock'))
    # return redirect(url_for('rtlogin'))


@app.route('/lock')
@session_manager.unauthorized_handler
def lock():
    if request.method == 'GET':
        next_page = request.args.get('next', '')
        if not next_page or url_parse(next_page).netloc != '' or next_page == '/':
            next_page = url_for('rtindex')
        data = {'tilte': 'LogicPlus | Lockscreen', 'next': next_page, 'user_name': app.config['user_name']}
        print("lock called")
        print(data)
        logout_user()
        return render_template('master/lockscreen.html', **data)
