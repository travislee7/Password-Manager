from time import sleep
import os

print("Welcome to your password storage device!") ; sleep(1)

def add():
    account = input("Account: ")
    username = input("Username: ")
    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write("Account: " + account + " | Username: " + username + " | Password: "  + password + "\n")
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line)

key = open('key.txt', 'a')
initiate = True
while initiate:
    master_password = input("What is the master password? ")
    if os.stat('key.txt').st_size == 0:
        key.write(master_password)
        initiate = False
    else:
        with open('key.txt') as k:
            if master_password in k:
                initiate = False
            else:
                initiate = True

while initiate == False:
    mode = input("Would you like to add a new password or view existing ones or quit (add, view, quit)? ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == 'quit':
        break
    else:
        print("Invalid input. Try again.")

