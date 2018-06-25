from library.model.student import student
from library.model.book import book,book_occupied

class login():
    user_data = dict()

    def main(self):
        choice = 0
        while choice != 6:

            print("1.List of all books")
            print("2.List of Occupied Books")
            print("3.Occupy Book")
            print("4.Return Book")
            print("5.Renew Book")
            print("6.Logout")

            choice = int(input("Enter choice =>"))

            if choice == 1:
                self.all_books()
            elif choice == 2:
                self.occupied_book(self.user_data['sid'])
            elif choice == 3:
                bid = int(input("Enter Book ID to purchased book=>"))
                self.occupy_book(bid)
            elif choice == 4:
                bid = int(input("Enter Book ID to return book=>"))
                book_check = len(book_occupied().same_book_check(bid, self.user_data['sid']))
                if book_check > 0:
                    if book_occupied().return_book(bid, self.user_data['sid']) is True:
                        print("Book Returned.")
                    else:
                        print("Book not Returned.")
                else:
                    print("You have not purchased this book yet.")
            elif choice == 5:
                bid = int(input("Enter Book ID to return book=>"))
                if book_occupied().renew_book(bid,self.user_data['sid']) is True:
                    print("book renewed.")
            elif choice == 6:
                if student().update_logout(self.user_data['sid']) is True:
                    print("You have loged out.")
                else:
                    print("Please try to login again.")
            else:
                print("Invalid Choice")

    def check_login(self, username, password):
        if username is '' or password is '' or username is None or password is None:
            error = True
            errstr = 'Please Enter Username Or Password.'
            return error, errstr
        else:
            row = student().do_login(username=username)

            if len(row) > 0 and row[0][1] == username:
                if row[0][15] is True:
                    if row[0][2] == password:
                        if student().update_login(row[0][0]) is True:
                            self.user_data['username'] = username
                            self.user_data['sid'] = row[0][0]
                            return False, 'Successful Login!!!'
                        else:
                            return True, "Update login fails."
                    else:
                        return True, "Password Does Not Match."
                else:
                    return True, "You'er not allowed anymore to access this system."
            else:
                return True, 'Invalid Username'

    def all_books(self):
        books_data = book().getBookData()

        print("books data\n",books_data)
        """
        0 1 3 6 12
        """
        for r in books_data:
            print("\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t".format(r[0], r[1], r[3], r[6], r[12]))

    def check_book_quantity(self, bid):
        quantity = book().getQuantity(int(bid))
        remaining_book = quantity[0][0] - book_occupied().count_occupied_book(bid=int(bid))[0][0]
        return remaining_book

    def occupied_book(self, sid):
        occupied_book_data = book().getOccupiedBooks(sid)

        if len(occupied_book_data) == 0:
            print("You have not purchased any book yet.")
        else:
            for r in occupied_book_data:
                print("\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t".format(r[0], r[5], r[1], r[2], r[3]))

    def occupy_book(self, bid):
        if self.count_occupied_book(self.user_data['sid']) is False:
            print("You Purchased Maximum number of book.")
        else:
            same_book = len(book_occupied().same_book_check(bid, self.user_data['sid']))
            if same_book == 0 and self.check_book_quantity(int(bid)) > 0:
                if book_occupied().occupy_book(bid, self.user_data['sid']) is True:
                    print("Book Successfully Purchased.")
                else:
                    print("Error occurred during book occupation.")
            else:
                print("You can not purchased this book.")

    def count_occupied_book(self, sid):
        book_count = len(book_occupied().count_occupied_book(sid=self.user_data['sid']))
        if book_count == 5:
            return False
        else:
            return book_count


# login().all_books()
# login().occupied_book(1)

if __name__ == '__main__':
    login()