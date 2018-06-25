# -*- coding: <utf-8> -*-

from library import library as app
from flask import url_for, render_template, redirect, request, jsonify
from ..model.book import book
from ..model.tmp import tmp
from ..model.course import course
""" controller : book module """


# -----------book--------------------
@app.route('/book/add', methods=['GET', 'POST'])
def addbook():
    """ add book """
    if request.method == 'POST':
        print(request.form)

        name = request.form['name_txt']
        publication = request.form['publication_txt']
        author1 = request.form['author1_txt']
        author2 = request.form['author2_txt']
        quantity = request.form['quantity_txt']
        year = request.form['year_txt']
        price = request.form['price_txt']
        course_id = request.form.get('course_txt')

        if name is not None and publication is not None and author1 is not None and author2 is not None and quantity is not None and year is not None and price is not None and course_id is not None:
            bid = book().addbook(name, publication, author1, author2, quantity, year, price, course_id)
            print("bid==", bid)
            print(request.files)
            if not request.form.get('dp_img', None) and 'dp_img' in request.files:
                dp = request.files['dp_img']
                ufolder = 'library/static/master/profile/book'
                filename = tmp().saveIMG(dp, name, ufolder)
                print(filename)
                valid = book().updateimg(filename, bid)
                print(valid)
                if valid is True:
                    return jsonify(url=url_for('booklist'), error='false')
                else:
                    return jsonify(error='true', errstr='Can not update image.')
        else:
            return jsonify(error=True, errstr='Something went wrong.')
    title = 'Library | book'
    return render_template('master/book/addbook.html', course_data=course().getCourseList(), title=title)


@app.route('/book/update', methods=['POST'])
def updatebook():
    if request.method == 'POST':
        if request.method == 'POST':
            print(request.form)
            name = request.form['name_txt']
            publication = request.form['publication_txt']
            author1 = request.form['author1_txt']
            author2 = request.form['author2_txt']
            quantity = request.form['quantity_txt']
            year = request.form['year_txt']
            price = request.form['price_txt']
            course_id = request.form.get('course_txt')
            print("step1")
            bid = request.form['bid']

            if name is not None and publication is not None and author1 is not None and author2 is not None and quantity is not None and year is not None and price is not None and course_id is not None:
                valid = book().UpdateBook(int(bid), name, publication, author1, author2, quantity, year, price, course_id)
                print("step3", valid)
                if valid is True:
                    if not request.form.get('dp_img', None) and 'dp_img' in request.files:
                        dp = request.files['dp_img']
                        ufolder = 'library/static/master/profile/book'
                        filename = tmp().saveIMG(dp, name, ufolder)
                        print(filename)
                        valid = book().updateimg(filename, int(bid))
                        print(valid)
                        if valid is True:
                            print("Image Uploaded.")
                            return jsonify(url=url_for('booklist'), error='false')
                        else:
                            return jsonify(error='true', errstr='Can not update image.')
                    else:
                        return jsonify(url=url_for('booklist'), error='false')
                else:
                    return jsonify(error='true', errstr='problem occurred during save your data.')
            else:
                return jsonify(error='true', errstr='Please enter data into all fields.')


@app.route('/book/list/', methods=['GET', 'POST'])
def booklist():
    if request.method == 'POST':
        bid = request.form['bid']
        print(bid)
        book_data = book().getBookData(bid)
        print(book_data)
        title = 'Library | book'
        return render_template('master/book/updatebook.html', row=book_data, course_data=course().getCourseList(),title=title)
    title = 'Library | book'
    book_data = book().getBookData()
    print("book_data",book_data)
    return render_template('/master/book/booklist.html', row=book_data, title=title)


@app.route('/book/active', methods=['POST'])
def activatebook():
    if request.method == 'POST':
        bid = request.form['bid']
        if book().ActivateBook(int(bid)):
            return redirect(url_for('booklist'))
        else:
            return redirect(url_for('booklist'))


@app.route('/book/delete', methods=['POST'])
def deletebook():
    if request.method == 'POST':
        bid = request.form['bid']
        if book().DeleteBook(int(bid)):
            return redirect(url_for('booklist'))
        else:
            return redirect(url_for('booklist'))