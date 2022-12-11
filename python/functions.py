def getNumber():
    num1 = int(input("Enter a number 1: "))
    num2 = int(input("Enter a number 2: "))
    num3 = int(input("Enter a number 3: "))
    calculator(num1, num2, num3)

def calculator(num1, num2, num3): 

    sum = (num1 + num2 + num3)
    print("Sum: ", sum)
    print("Product: ", num1 * num2 * num3)
    print("Smallest: ", min(num1, num2, num3))
    print("Largest: ", max(num1, num2, num3)) 

getNumber() 
   