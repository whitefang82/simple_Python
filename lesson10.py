# Collatz

print("Enter Number: ")
EnteredNumber = int(input())

while EnteredNumber != 1:
    Number = EnteredNumber % 2
    if Number == 0:
        EnteredNumber = EnteredNumber // 2
        print(EnteredNumber)
    elif Number == 1:
        EnteredNumber = EnteredNumber * 3 + 1
        print(EnteredNumber)
    else:
        break
