s = input()

print(any(char.isalnum() for char in s))

print(any(char.isalpha() for char in s))

print(any(char.isnumeric() for char in s))

print(any(char.islower() for char in s))

print(any(char.isupper() for char in s))
