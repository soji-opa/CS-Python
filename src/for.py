""" We use for loops to iterate over collections of a string/collection
note lists are synonymous to arrays in JS
"""

# for item in 'python':
#     print(item)

# for item in ['josh', 'qudus', 'hlupo']:
#     print(item)

# using range to iterate over a large "list" of numbers - It counts from 0 upto but does not include 10

# for item in range(10-1):
#     print (item)

"""
Example - calc total prices in a shopping cat
prices  = [10, 20, 30]

"""
# total = 0
# prices = [10, 20, 30]
# for item in range(0, len(prices)):
#     total += prices[item]
#     print(f"Total : {total}")

# guy = 'x'
# number = [5, 2, 5, 2, 2]
# for item in number:
#     product = guy * item
#     print(product)

numbers = [2, 2, 2, 2, 5, 5]
for item in numbers:
    output =''
    for count in range(item):
        output += 'x'
    print(output)


""" Nested forLoop"""
# for x in range(4):
#     for y in range (3):
#         print(f"{x},{y}")