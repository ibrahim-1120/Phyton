start = int(input("Enter the startng number :"))
end = int(input("Enter the ending number :"))
for i in range(start, end + 1):
 for j in range(1, 11):
  print(f"{i} x {j} = {i * j}")
print()