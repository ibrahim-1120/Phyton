num = int(input("Enter a number"))
a,b=0,1

print("Fabonaci series")

for i in range(num):
    print(a,end="")
    a, b = b, a + b
    print()