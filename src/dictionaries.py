""" Dictionaries are synonymous to objects in JS
- We can access each elements in the dictionaries using square brackets
- However, using the .get() makes sense as the mtd returns none if the key-value pair does not exist in the
dictionary, hence program does not bring an error

 """

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer.get("name"))

# phone = input("Phone: ")

# digits_mapping ={
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }

# output= ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)

message = input("Message: ")
words = message.split(' ')
emojis = {
    "happy": "\U0001F973",
    "sad": "\U0001F628"
}
output=""
for word in words:
    output += emojis.get(word, word) + " " 
print(output)