from library import library as app
from flask import url_for, render_template, redirect, request
from ..model.user import user
from flask_login import login_required


# ------------------table user--------------
@app.route('/user', methods=['GET', 'POST'])
@login_required
def tbluser():
    if request.method == 'POST':
        uid = request.form['id']
        t = {'title': 'Library | User | Update'}
        udata = user().getuserdataById(uid)
        return render_template('master/pages/tables/userform.html', row=udata, **t)
    udata = user().getuserdata()
    return render_template('master/pages/tables/tbluser.html', row=udata, title='Library | User')


@app.route('/user/update', methods=['POST'])
@login_required
def update():
    if request.method == 'POST':
        uid = request.form['id']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        mobile = request.form['mobile']
        active = request.form['active']
        valid = user().updateuserdata(uid, username, password, email, mobile, active)
        if valid is True:
            return redirect(url_for('tbluser'))


@app.route('/user/active', methods=['POST'])
@login_required
def active():
    if request.method == 'POST':
        uid = request.form['id']
        if user().activateuser(int(uid)):
            return redirect(url_for('tbluser'))


@app.route('/user/delete', methods=['POST'])
@login_required
def delete():
    if request.method == 'POST':
        uid = request.form['id']
        if user().inactivateuser(int(uid)):
            return redirect(url_for('tbluser'))
