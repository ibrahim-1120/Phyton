num1 = int(input("Enter the number 1 :"))
num2 = int(input("Enter the number 2 :"))
num3 = int(input("Enter the number 3 :"))

if num1>=num2 and num1>=num3:
 maximun=num1
elif num2>=num1 and num2>=num3:
 maximun=num2
else:
 maximun=num3

 print(f"The maximum number is {maximun}")
