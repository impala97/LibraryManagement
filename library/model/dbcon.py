import psycopg2 as db


class dbcon:
    con = None
    cursor = None

    def __init__(self):
        self.con = db.connect(dbname='library', host='localhost', user='postgres', password='root')
        self.cursor = self.con.cursor()

    def do_select(self, select):
        try:
            self.cursor.execute(select)
            row = self.cursor.fetchall()
            self.cursor.close()
            return row
        except db.DatabaseError as error:
            return error
        finally:
            if self.con is not None:
                self.con.close()

    def do_insert(self, query, response=False):
        """ Insert the query in database and return the response"""
        try:
            self.cursor.execute(query)
            result = True
            if response is True:
                result = self.cursor.fetchone()[0]
            self.con.commit()
            self.cursor.close()
            return result
        except db.DatabaseError as error:
            return error
        finally:
            if self.con is not None:
                self.con.close()

    def do_bulk(self, query):
        if isinstance(query, list):
            try:
                self.cursor.execute("SAVEPOINT do_bulk;")
                self.cursor.execute("BEGIN;")
                print(query)
                for que in query:
                    self.cursor.execute(que)
            except db.Error as e:
                print(e.pgerror)
                self.cursor.execute("ROLLBACK TO SAVEPOINT do_bulk;")
                return e.pgerror
            else:
                self.con.commit()
                return True
            finally:
                self.cursor.close()
                if self.con is not None:
                    self.con.close()
        """
        sub_str = ""
        for que in query:
            sub_str = sub_str + "\n\t" + que
        final_str = "BEGIN; savepoint do_bulk;\n\t %s \n ROLLBACK to savepoint do_bulk;" % sub_str
        print(final_str)
        self.do_insert(final_str)
        """


if __name__ == "__main__":
    dbcon()
