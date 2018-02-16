birthdays = {'Alice' : 'Apr 1', 'Bob' : 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print("Enter the name: (blank to quit)")
    name = input()
    if name == '':
        break
    if name == 'dev':
        print(birthdays)
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print("I do not have this info for " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name]= bday #<- updating
        print("Birthday database updated.")
