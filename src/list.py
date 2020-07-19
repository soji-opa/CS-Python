""" Synonymous to arrays in JS """

names = ["john", "kluivert", "tobey", "ailes"]
print(names[2:])

""" The idea here was to get out the max number in the array

the first thing we did was pick the first item in array 

the second thing we did is to compare the first number with other numbers in the list/array 

Lastly we iterate through the array
"""
data =  [2, 6, 1, 3, 4, 7, 9, 10]
# print(max(data))
max = data[0]
for item in data:
    if item > max:
        max = item
# print(max)

# Append -  add an element to the end of the list
numbers = [5, 7, 3, 4, 12]
numbers.append(20)


# Insert - add an element in a certain position in the array- insert (index, element to be inserted)
numbers.insert(0, 23)

# Remove - to remove an element from a list
numbers.remove(23)

# sort - organise the list in ascending order
numbers.sort()

# reverse - organise the list in  descending order
numbers.reverse()
print(numbers)
# clear - use clear to empty the list; this method takes no argument
numbers.clear()

data = [2, 2, 3, 4, 4, 5, 6, 7, 9, 9, 10]
store = []

for item in data:
   if item not in store:
       store.append(item)
print(store)

