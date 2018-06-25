from .dbcon import dbcon


class course:
    def AddCourse(self, cname, branch):
        insert = "insert into library.course(cname,branch) values('%s','%s');" % (cname, branch)
        print(insert)
        return dbcon().do_insert(insert)

    def getCourseName(self, id=None):
        if id is not None:
            select = "select cname from library.course where id=%d and active='1';"%(int(id))
            row = dbcon().do_select(select)
            return row[0]
        else:
            select = "select cname,fees from library.course WHERE active='1';"
            return dbcon().do_select(select)

    def getCourseData(self, cid=None):
        if cid is None:
            select = "select * from library.course order by id;"
        else:
            select = "select * from library.course where id=%d;" % cid
        return dbcon().do_select(select)

    def updateCourse(self, cid, cname, branch):
        update = "update library.course set cname='%s',branch='%s' where id=%d;" % (cname, branch, cid)
        return dbcon().do_insert(update)

    def CountTotalBooks(self, cid):
        select = "select count(cid) from library.book WHERE active='1';"
        return dbcon().do_select(select)

    def Activate_Course(self, cid):
        update = "update library.course set active='1' where id='%d';" % cid
        return dbcon().do_insert(update)

    def Delete_Course(self, cid):
        update = "update library.course set active='0' where id='%d';" % cid
        return dbcon().do_insert(update)

    def getCourseList(self):
        select = "select id,cname from library.course where active='1' order by id;"
        return dbcon().do_select(select)


if __name__ == "__main__":
    course()
