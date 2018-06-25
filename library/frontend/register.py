import os
import re
# from .model.student import student
from library.model.student import student
from library.model.tmp import tmp
from shutil import copyfile

class register:
    def register_student(self):
        sdata = dict()

        sdata["username"] = input("Enter Username==>")
        sdata["password"] = input("Enter Password==>")
        sdata["fname"] = input("Enter First Name==>")
        sdata["lname"] = input("Enter Last Name==>")
        sdata["email"] = input("Enter Email Address==>")
        sdata["phone"] = input("Enter Phone Number==>")
        sdata["gender"] = input("Enter Your Gender(F/M)==>")
        sdata["dob"] = input("Enter Your DOB(YYYY-MM-DD)==>")
        sdata["address"] = input("Enter Your Address==>")

        if not self.check_email(sdata['email']):
            sdata["email"] = input("Enter Email Address")
            self.check_email(sdata['email'])

        if not self.check_phone(sdata['phone']):
            sdata["phone"] = input("Enter Phone Number")
            self.check_phone(sdata['phone'])

        if not self.check_gender(sdata['gender']):
            sdata['gender'] = input("Enter Your Gender(F/M)")
            self.check_gender(sdata['gender'])
        else:
            sdata['gender'] = True

        print(sdata['gender'])
        sdata['dob'] = self.check_dob(sdata['dob'])
        print(sdata)
        sid = student().add_student(**sdata)
        if sid is False:
            print("\nSomething went wrong.\n")
        else:
            print("\nInsert successfully.\n")
        """
        else:
            sdata['picture'] = input("Paste Here Your Picture Path==>")

            if not self.check_pic_path(sdata['picture']):
                sdata['picture'] = input("Paste Here Your Picture Path==>")
                self.check_pic_path(sdata['picture'])

            file_name = tmp().saveIMG(sdata['picture'], sid)
            if student().update_pic(file_name, sid) is True:
                print("Image name updated.")
            else:
                print("Error occurred during update image name.")
        """

    def check_pic_path(self, img):
        file_check = os.path.isfile(img)
        return file_check

    def check_dob(self, dob):
        dob = dob.split('-')
        if len(dob) == 3:
            from datetime import datetime, timedelta
            new_dob = datetime(year=int(dob[0]), month=int(dob[1]), day=int(dob[2]))
            return new_dob
        else:
            new_dob = input("Enter Your DOB(YYYY-MM-DD)")
            return self.check_dob(new_dob)
        
    def check_gender(self, gender):
        return gender is 'F' or gender is 'f' or gender is 'M' or gender is 'm'

    def check_email(self,email):
        return re.match("^[a-zA-Z0-9.!#$%&''*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zAZ0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email)

    def check_phone(self,phone):
        return re.match("^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$", phone)


if __name__ == '__main__':
    register()