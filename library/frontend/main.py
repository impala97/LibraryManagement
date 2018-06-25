from register import register
from login import login


def student_login():
    print("student login...")
    username = input("Enter Username=>")
    password = input("Enter Password=>")

    error, error_string = login().check_login(username, password)

    if error is True:
        print(error, error_string)
        student_login()
    else:
        print("Login Successful!!")
        login().main()


def reset_student_pwd():
    print("\nReset Password...\n")


def main():
    choice = 0
    while choice !=4:

        print("1.Student Register")
        print("2.Student Login")
        print("3.Reset Password")
        print("4.Exit")

        choice = int(input("Enter choice =>"))

        if choice == 1:
            register().register_student()
        elif choice == 2:
            student_login()
        elif choice == 3:
            reset_student_pwd()
        elif choice == 4:
            exit()
        else:
            print("Invalid Choice")


main()
