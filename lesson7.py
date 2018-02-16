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
try_enter = 0

#3 Strikes
for try_enter in range(3):      # 3 times not try_enter = 3
    try_enter = try_enter + 1
    enter_user_pass()
    if Input_username == Username and Input_pass == Password and try_enter <= 3:
        print("Access granted.")
        break
    else:
        print("Access denied. " + str(try_enter))
        if try_enter == 3:
            print("No more")
            break
