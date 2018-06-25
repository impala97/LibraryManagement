# For database operation
from .dbcon import dbcon


class otp:
    def add(self, user_id, generated_otp):
        insert = "insert into library.otp(user_id,otp) VALUES(%d, '%s') RETURNING id;" % (user_id, generated_otp)
        return dbcon().do_insert(insert, response=True)

    def get(self, user_id):
        select = "select * from library.otp,(select last_otp_id from library.user where id=%d) as last_otp_id where id=last_otp_id;" % int(user_id)
        return dbcon().do_select(select)


if __name__ == "__main__":
    otp()