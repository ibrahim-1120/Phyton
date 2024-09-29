for i in range(100,1000):
    num_str=str(i)
    num_sum = sum(int(digit) ** len(num_str) for digit in num_str)
    if num_sum==i:
        print(i,end="")
        print()
        