#Find the common denominators of 2 given numbers

def comDenominators(num1,num2):
    small=num1
    commonDenominatorArray=[]
    if (num1>num2):
        small=num2

    for i in range (1,small):
        if (num1 % i == 0 and num2 % i == 0):
            print("Common denominator: ",i)
            commonDenominatorArray.append(i)

    return (commonDenominatorArray)

num1=int(input("Please enter the 1st number: "))
num2=int(input("Please enter the 2nd number: "))
print(comDenominators(num1,num2))