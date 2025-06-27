def remove_char(s):
    return f"{s[1:len(s) - 1]}"


# 2

def square_sum(numbers):
    squared = []
    for i in numbers:
        squared.append(i**2)
    return sum(squared)

# 3

def find_smallest_int(arr):
    return min(arr)

# 4

def count_sheeps(sheep):
    return sheep.count(True)