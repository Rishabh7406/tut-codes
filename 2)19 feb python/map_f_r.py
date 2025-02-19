from functools import reduce

nums = [1, 2, 3, 4, 5]

# Map: Square each number
squared = list(map(lambda x: x**2, nums))
print("Map:", squared)  # [1, 4, 9, 16, 25]

# Filter: Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Filter:", evens)  # [2, 4]

# Reduce: Sum all numbers
sum_all = reduce(lambda x, y: x + y, nums)
print("Reduce:", sum_all)  # 15

# from functools import reduce
# nums = [1, 2, 3, 4]
# print(list(map(lambda x: x**2, nums)))  # Map
# print(list(filter(lambda x: x%2 == 0, nums)))  # Filter
# print(reduce(lambda x, y: x+y, nums))  # Reduce
