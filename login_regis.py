import re
import csv

mail_reg = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-za-z0-9]+(\.[A-Z|a-z]{2,})+')
pwd_reg = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#$%^&*@!-]).{5,}$')


def is_valid_mail(email):
    if re.fullmatch(mail_reg, email):
        return True
    else:
        return False


def is_valid_pwd(password):
    if re.fullmatch(pwd_reg, password):
        return True
    else:
        return False

def register():
    print("\nRegister new user\n")
    email=input("Email ID : ")
    if is_valid_mail(email):
        password=input('Password: ')
        if is_valid_pwd(password):
            write_file(email,password)
            print("\nUser registered successfully")
        else:
            print("\nInvalid Password, Try again..")
    else:
        print("\nInvalid Username, Try again..")

def login():
    email=input("Email ID= ")
    if is_valid_mail(email):
        password=input("Password: ")
        if is_valid_pwd(password):
            if search_file(email, password):
                print("\nUser Logged in successfully..")
            else:
                print("\nUser not found")
                register()
        else:
            print("\nInvalid password, Try again..")
    else:
        print("\nInvalid username, Try again..")

def forget_pwd():
    email=input("Email ID: ")
    if is_valid_mail(email):
        if search_pwd(email):
            print("\nUser logged in successfully..")
        else:
            print("\nUser not found!!")
            register()
    else:
        print("\nInvalid username, Try again..")

def search_file(email, password, mode='r', encoding='UTF8', newline=''):
    with open('users.csv', mode, encoding=encoding, newline=newline) as f:
        reader= csv.reader(f)
        for row in reader:
            if email==row[0] and password==row[1]:
                return True
        return False

def search_pwd(email, mode='r', encoding='UTF8', newline=''):
    with open('users.csv', mode, encoding=encoding, newline=newline) as f:
            reader= csv.reader(f)
            for row in reader:
                if email == row[0]:
                    print("\nPassword for " + email + " is " + row[1])
                    return True
            return False

def write_file(email, password, mode='a', encoding='UTF8', newline=''):
    with open('users.csv', mode, encoding=encoding, newline=newline) as f:
        writer= csv.writer(f)
        writer.writerow([email,password])


if __name__ == "__main__":

    try:
        while True:
            print('''\nPlease select an option \n
                  1.Register
                  2.Login
                  3.Forgot Password
                  ''')
            option = int(input())
            if option == 1:
                register()
            elif option == 2:
                login()
            elif option == 3:
                forget_pwd()
            else:
                print("Invalid option")

    except:
        print("An exception occured")


