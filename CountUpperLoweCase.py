sentence = input("Enter the sentence")
uppercase = sum(1 for char in sentence if char.isupper())
lowercase = sum(1 for char in sentence if char.islower())
digit = sum(1 for char in sentence if char.isdigit())
special_char = sum(1 for char in sentence if not char.isalnum()and not char.isspace())
space = sum(1 for char in sentence if char.isspace())
print(f"Upper case : {uppercase}")
print(f"Lower case : {lowercase}")
print(f"Digit :{digit}")
print(f"Special character :{special_char}")
print(f"Space :{space}")
