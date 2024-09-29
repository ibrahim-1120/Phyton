# swap using third variable

a=input("Enter the value of a :")
b=input("Enter the value of b :")
temp=a
a=b
b=temp
print(f"After swapping,a: {a},b:{b}")

# swap without using third variable

c=input("Enter the nvalue of c")
d=input("Enter the value of d")
c,d=d,c
print(f"After swapping ,c:{c},d:{d}")