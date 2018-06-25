from library import library as app
from flask import url_for, render_template, request, redirect
from ..model.course import course


# ----------------------course-----------
@app.route('/course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        cname = request.form['cname_txt']
        branch = request.form['branch_txt']
        if course().AddCourse(cname, branch) is True:
            return redirect(url_for('course_list'))
    title = 'Library | Course'
    return render_template('master/course/addcourse.html', title=title)


@app.route('/course/list', methods=['GET', 'POST'])
def course_list():
    if request.method == 'POST':
        cid = request.form['cid']
        title = 'Library | Course'
        return render_template('master/course/updatecourse.html', row=course().getCourseData(int(cid)), title=title)
    title = 'Library | Course'
    return render_template('master/course/list.html', row=course().getCourseData(), title=title)


@app.route('/course/update', methods=['GET', 'POST'])
def update_course():
    if request.method == 'POST':
        cid = request.form['cid']
        cname = request.form['cname_txt']
        branch = request.form['branch_txt']
        if course().updateCourse(int(cid), cname, branch):
            return redirect(url_for('course_list'))


@app.route('/course/active', methods=['GET', 'POST'])
def activate_course():
    if request.method == 'POST':
        cid = request.form['cid']
        valid = course().Activate_Course(int(cid))
        if valid is True:
            return redirect(url_for('course_list'))


@app.route('/course/delete', methods=['GET', 'POST'])
def delete_course():
    if request.method == 'POST':
        cid = request.form['cid']
        valid = course().Delete_Course(int(cid))
        if valid is True:
            return redirect(url_for('course_list'))
