from .dbcon import dbcon
import datetime

class student:
    def getAdmission(self, sid=0):
        """List student list"""
        if sid == 0:
            select = "select * from library.student order by id;"
        else:
            select = "select * from library.student where id=%d;" % sid
        return dbcon().do_select(select)

    def add_student(self,username, password, fname, lname, email, phone, gender, dob, address):
        insert = "insert into library.student(username, password, fname, lname, email, phone, gender, dob, address) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s') returning id;" % (username, password, fname, lname, email, phone, gender, dob, address)
        print("add student-->", insert)
        return dbcon().do_insert(insert)

    def update_pic(self,img, sid):
        update = "update library.student set picture='%s' WHERE id=%d;" %(img, sid)

    def activate(self, sid):
        update = "update library.student set active='1' where id=%d;"% sid
        return dbcon().do_insert(update)

    def delete(self, sid):
        update = "update library.student set active='0' where id=%d;"% sid
        return dbcon().do_insert(update)

    def do_login(self,username=None, id=None):
        if id is not None:
            select = "select * from library.student where id=%d;" % int(id)
        elif username is not None:
            select = "select * from library.student where username='%s';" % username
        return dbcon().do_select(select=select)

    def update_login(self, sid):
        date = self.currentdate()
        update = "update library.student set last_login = '%s',live='1' where id=%d;" % (date,sid)
        return dbcon().do_insert(update)

    def update_logout(self, sid):
        date = self.currentdate()
        update = "update library.student set last_login = '%s',live='0' where id=%d;" % (date, sid)
        return dbcon().do_insert(update)

    def currentdate(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")