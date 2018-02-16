#Password program using loop and break


def enter_user_pass():
    # global Variable
    global Input_username
    global Input_pass
    print("Username: ")
    Input_username = input()
    print("Password: ")
    Input_pass     = input()


Username = "Bang"
Password = "1234560"
print("Hi!")


while True:
    enter_user_pass()
    if Input_username == Username and Input_pass == Password:
        break
    else:
        print("Access denied.")

print("Access granted.")
