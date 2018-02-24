#Password

"""while True:
    print("Enter your age: ")
    age = input()
    if age.isdecimal():
        break
    print("Only number!")"""

while True:
    print("Enter your Password: ")
    password = input()
    length = len(password)
    print(length)
    if password.isalnum() and length >= 6:
        break
    print("Only letters and numbers and at least 6 characters!")
