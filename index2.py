# 1
# list = ['one', 'two', 'three']
# print(list)

# 2
# numbers = [10, 20, 30, 40, 50]
# print(sum(numbers))

# 3
# num_list = [10, 20, 30, 40, 50]
#
#
# def add_to_end(num):
#     if num not in num_list:
#         num_list.append(num)
#     else:
#         print('Already added')

# 4
# list = ['one', 'two', 'three']
# list.pop()
# print(list)

# 5
# strings = ['one', 'two', 'three']
# longest = max(strings, key=len)
# print(longest)

# 6
# numbers = [10, 20, 30, 40, 50]
# print(sum(numbers) / len(numbers))

# 7
# names = ["Ethan", "Alice", "Bob", "Diana", "Charlie"]
# names.sort()
# print(names)

# 8
# list1 = ["apple", "banana", "cherry"]
# list2 = ["grape", "banana", "orange"]
# print(list(set(list1) | set(list2)))

# 9
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum(num for num in numbers if num % 2 == 0))

# 10
# strings = ['one', 'two', 'three']
# copy_list = strings.copy()

# 11
# numbers = [1, 2, 3, 4, 2, 5, 3, 6, 7, 1, 8, 4, 9, 5, 10]
# numbers.sort()
# print(numbers[-2])

# 12
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# max_num = max(numbers)
# min_num = min(numbers)
# print(max_num - min_num)

# 13
# names = ["Ethan", "Alice", "Bob", "Diana", "Charlie"]
# names.reverse()
# print(names)

# 14
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
without_even = [num for num in numbers if num % 2 != 0]
print(without_even)

# 15
# numbers = [1, 2, 3, 4, 2, 5, 3, 6, 7, 1, 8, 4, 9, 5, 10]
# print(len(set(numbers)))
