year= int(input("Enter the year"))
if(year%4==0 and year%100!=0)or(year%4==0):
 print(f"{year} Is a leap year")
else:
 print(f"{year} Is not a leap year")