from library import library as app
from flask import url_for, redirect, render_template, request

from ..model.student import student


@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    pass


@app.route('/student/list', methods=['GET','POST'])
def student_list():
    if request.method is 'POST':
        pass
    else:
        title = 'Master | Admission'
        row = student().getAdmission()
        return render_template('master/student/list.html', row=row,title=title)


@app.route('/student/update', methods=['POST'])
def update_student():
    pass


@app.route('/student/activate', methods=['POST'])
def activate_student():
    if request.method == 'POST':
        sid = request.form['sid']
        valid = student().activate(int(sid))
        if valid is True:
            return redirect(url_for('student_list'))


@app.route('/student/delete', methods=['POST'])
def delete_student():
    if request.method == 'POST':
        sid = request.form['sid']
        valid = student().delete(int(sid))
        if valid is True:
            return redirect(url_for('student_list'))
