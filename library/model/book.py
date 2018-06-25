from .dbcon import dbcon


class book:
    def getQuantity(self, bid):
        select = "select quantity from library.book WHERE id={};".format(int(bid))
        return dbcon().do_select(select)

    def addbook(self,name, publication, author1, author2, quantity, year, price, course_id):
        print("course_id",course_id)
        insert = "insert into library.book(name, publication, author1, author2, quantity, /year, price, cid) values('%s','%s','%s','%s','%s','%s','%s') returning id;" % (name, publication, author1, author2, quantity, year, price, course_id)
        return dbcon().do_insert(insert, response=True)

    def __getId__(self,email):
        select = "select id from lp.faculty where email='%s'" %email
        row = dbcon().do_select(select)
        return row[0][0]

    def updateimg(self, filename, bid):
        print(type(bid),bid)
        update = "update library.book set picture='%s' where id=%d;" % (filename, bid)
        print(update)
        return dbcon().do_insert(update)

    def count_books(self, bid):
        select = "select count(bid) from library.book_occupied WHERE RETURNED='0';"
        return dbcon().do_select(select)

    def getBookData(self, bid=None, active=None):
        if bid is None and active is None:
            if active is not None:
                select = "select * from library.book WHERE active='1';"
            else:
                select = "select * from library.book order by id;"
            data = dbcon().do_select(select)
            for i in range(0, len(data)):
                data[i] = data[i] + self.getCourseName(data[i][10])[0] + self.count_books(data[i][0])[0] + self.check_book_quantity(data[i][0])
            return data
        else:
            select = "select * from library.book where id=%d;" % int(bid)
            data = dbcon().do_select(select)
            data[0] = data[0] + self.getCourseName(data[0][10])[0] + self.count_books(data[0][0])[0] + self.check_book_quantity(data[0][0])
            print(data)
            return data

    def getOccupiedBooks(self, sid):
        select = "select bid,purchased_date,return_date,auto_renew from library.book_occupied WHERE sid=%d AND returned='0';" % (int(sid))
        bid = dbcon().do_select(select)
        for i in range(0,len(bid)):
            bid[i] = bid[i] + self.getBookData(bid=bid[i][0])[0]
        return bid

    def getCourseName(self, cid):
        select = "select cname from library.course WHERE id=%d;" % int(cid)
        return dbcon().do_select(select)

    def ActivateBook(self, bid):
        update = "update library.book set active='1' where id=%d" % bid
        return dbcon().do_insert(update)

    def DeleteBook(self, bid):
        update = "update library.book set active='0' where id=%d" % bid
        return dbcon().do_insert(update)

    def UpdateBook(self, bid, name, publication, author1, author2, quantity, year, price, course_id):
        print("course_id", course_id)
        update = "update library.book set name='%s',publication='%s',author1='%s',author2='%s',quantity=%d,year=%d,price=%d,cid=%d where id=%d;" % (name, publication, author1, author2, int(quantity), int(year), int(price), int(course_id), int(bid))
        print(update)
        return dbcon().do_insert(update)

    def getFacultyName(self,id=None):
        if id is not None:
            select = "select name from lp.faculty where id=%d;" % int(id)
            row = dbcon().do_select(select)
            return row[0][0]
        else:
            select = "select id,name from lp.faculty where active='1' order by id;"
            return dbcon().do_select(select)

    def countid(self):
        select = "select count(id) from lp.faculty;"
        count = dbcon().do_select(select)
        return count[0][0]

    def check_book_quantity(self, bid):
        quantity = self.getQuantity(int(bid))
        remaining_book = [0]
        remaining_book[0] = quantity[0][0] - book_occupied().count_occupied_book(bid=int(bid))[0][0]
        return tuple(remaining_book)


class book_occupied():
    def return_book(self, bid, sid):
        update = "update library.book_occupied set returned='1' WHERE bid={} AND sid={};".format(int(bid), int(sid))
        return dbcon().do_insert(update)

    def same_book_check(self, bid, sid):
        select = "select * from library.book_occupied WHERE returned='0' AND bid={} AND sid={};".format(int(bid), int(sid))
        return dbcon().do_select(select)

    def occupy_book(self,bid,sid):
        insert = "insert into library.book_occupied(bid,sid) VALUES ({},{});".format(int(bid), int(sid))
        return dbcon().do_insert(insert)

    def count_occupied_book(self,sid=None, bid=None):
        if sid is not None:
            select = "select count(sid) from library.book_occupied WHERE returned='0' AND sid={};".format(int(sid))
            return dbcon().do_select(select)
        if bid is not None:
            select = "select count(bid) from library.book_occupied WHERE RETURNED='0' AND bid={};".format(int(bid))
            return dbcon().do_select(select)

    def renew_book(self, bid, sid):
        update = "update library.book_occupied set return_date=return_date + INTERVAL '15 days' WHERE bid={} AND sid={} AND returned='0';".format(bid,sid)
        return dbcon().do_insert(update)


if __name__ == "__main__":
    faculty()



