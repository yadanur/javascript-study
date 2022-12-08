num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

small=None
if (num1<num2):
    small=num1
else:
    small=num2

print (small)

for i in range(1,small):
    if (num1%i==0 and num2%i==0):
        print("common denominator: ", i)