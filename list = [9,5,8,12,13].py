list = [9,5,8,12,13]

def is_even(num):
    return num % 2 == 0

result = filter(is_even, list)

print(list(result))