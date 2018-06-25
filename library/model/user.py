import datetime
from .dbcon import dbcon
from flask_login import UserMixin
from library import session_manager
import datetime


class model_user(UserMixin):
    """Wraps User object for Flask-Login"""
    user_id = ""
    user_name = ""
    user_email = ""
    pwd = ""
    authenticated = False

    def __init__(self, user_id, pwd=None, username=None, email=None, auth=False):
        """init method of class.."""
        self.user_id = user_id
        if username is not None:
            self.user_name = username
        if email is not None:
            self.user_email = email
        if pwd is not None:
            self.pwd = pwd
        self.authenticated = auth

    def change_login_view(self, endpoint=None):
        if endpoint is not None:
            session_manager.login_view = endpoint
        else:
            session_manager.login_view = "rtlogin"

    def is_active(self):
        """is_active property"""
        print("user_id===", self.user_id)
        return user().activateuser(self.user_id, check=True)[0][0]

    def is_authenticated(self):
        """is_authenticated property"""
        print("is_authenticated==", self.authenticated)
        return self.authenticated

    def is_anonymous(self):
        """is_anonymous property"""
        print("anonymous===", user().activateuser(self.user_id, check=True)[0][0])
        if user().activateuser(self.user_id, check=True)[0][0]:
            return False
        else:
            return True

    def get_id(self):
        return chr(int(self.user_id))

    def get_user(self):
        user_data = user().do_login(id=ord(self.user_id))
        self.user_id = user_data[0][0]
        self.user_email = user_data[0][3]
        self.user_name = user_data[0][1]
        self.pwd = user_data[0][2]
        self.authenticated = True
        return self


class user(object):
    def adduser(self,username,pwd,email,phone):
        insert = "insert into library.user(username,password,email,phone,last_login,live) values('%s','%s','%s','%s','%s','1') RETURNING username;" % (username, pwd, email, phone, self.currentdate())
        result = dbcon().do_insert(insert, response=True)
        return result

    def check_user_existance(self, username):
        select = "select username from library.user where username='%s';" % username
        return dbcon().do_select(select=select)

    def __getId__(self, username):
        select = "select id from library.user where username='%s';" %username
        row = dbcon().do_select(select)
        return row[0][0]

    def do_login(self,username=None, id=None, email=None):
        if id is not None:
            select = "select * from library.user where id=%d;" % int(id)
        elif username is not None:
            select = "select * from library.user where username='%s';" % username
        else:
            select = "select * from library.user WHERE email='%s';" % email
        print(select)
        return dbcon().do_select(select=select)

    def update_login(self,id):
        date = self.currentdate()
        update = "update library.user set last_login = '%s',live='1' where id=%d;" % (date,id)
        return dbcon().do_insert(update)

    def update_logout(self, user_name, user_id):
        update = "update library.user set live='0' where username='%s' AND id=%d;" % (user_name, int(user_id))
        print("update_logout==", user_name, user_id)
        return dbcon().do_insert(update)

    def currentdate(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def __getEmail__(self, id):
        select = "select email from library.user where id=%d;" % id
        row = dbcon().do_select(select)
        if len(row) > 0:
            return row[0][0]
        else:
            return None

    def getuserdata(self):
        select = "select * from library.user order by id;"
        return dbcon().do_select(select)

    def activateuser(self, user_id, check=None):
        if check is None:
            update = "update library.user set active='1' where id=%d;"%int(user_id)
            return dbcon().do_insert(update)
        elif check is True:
            select = "select active from library.user where id=%d;" % int(user_id)
            return dbcon().do_select(select)

    def inactivateuser(self,id):
        update = "update library.user set active='0' where id=%d"%int(id)
        return dbcon().do_insert(update)

    def getuserdataById(self,id):
        select = "select * from library.user where id=%d order by id" % int(id)
        return dbcon().do_select(select)

    def updateuserdata(self,id,username,password,email,phone,active):
        update = "update library.user set username='%s',password='%s',email='%s',phone='%s',active='%s' where id=%d"%(username,password,email,phone,active,int(id))
        return dbcon().do_insert(update)

    def changepwd(self, id, new_pwd, old_pwd=None):
        if old_pwd is not None:
            update = "update library.user set password='%s' where id=%d and password='%s';"%(new_pwd,int(id),old_pwd)
        else:
            update = "update library.user set password='%s' WHERE id=%d;" % (new_pwd, id)
        return dbcon().do_insert(update)

    def usercount(self):
        select = "select count(id) from library.user;"
        count = dbcon().do_select(select)
        del select
        return count[0][0]

    def update_otp_id(self,user_id, last_otp_id, string=False):
        update = "update library.user set last_otp_id=%d where id=%d;" % (last_otp_id, user_id)
        if string is True:
            return update
        else:
            return dbcon().do_insert(update)

    def currentdate(self):
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    user()