#This program says hello and asks for my nameself.

print('Hello World')
print("What's your name?")      # Ask for your name
myName = input()
print("It's good to meet you, " + myName)
print("The length of your name is: ")
print(len(myName))
print("What is your age?")
myAge = input()
print('You will be ' + str(int(myAge)+1)+' in a year.')
