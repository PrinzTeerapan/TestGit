from email.mime import text


print("1")
print("*")
print("2")
print("**")
print("3")
print("***")
print("--------------------------------")
inputNumber = int(input("Enter a number: "))
for i in range(inputNumber):
    print("*" * (i + 1))
print("--------------------------------")
