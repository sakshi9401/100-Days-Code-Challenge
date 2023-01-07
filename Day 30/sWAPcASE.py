def swap_case(s):
    result = []
    for char in s:
        if char.isupper():
            result.append(char.lower())
        else:
            result.append(char.upper())
    return "".join(result)
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
