def findMaxOfThreeNumbers(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print("Greatest number:",num1)
    elif(num2>num1 and num2>num2):
        print("Greatest number:",num2)
    else:
        print("Greatest number:",num3)
        
print("find the greatest number among three numbers")
n1=int(input("Enter number1: "))
n2=int(input("Enter number2: "))
n3=int(input("Enter number3: "))

findMaxOfThreeNumbers(n1,n2,n3)