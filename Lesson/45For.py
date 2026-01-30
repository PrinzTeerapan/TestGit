inputRound = int(input("Enter a number to round: "))
sum = 0
for i in range(inputRound):
    inputNumber = int(input("i"+str(i+1)+":"))
    sum += inputNumber
print("The sum is:", sum)