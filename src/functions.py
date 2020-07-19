""" In this section we look at functions in python
- A basic python program is written below
"""

# def greet_user():
#     print("Hi there")
#     print("Welcome to functions in python")

# print("start")
# greet_user()
# print("finished")

""" With parameters, functions can receive information 
- Parameters - are place holders that we define in our function to receive information
-Arguments are the actual pieces of information that we pass into our functions

- For regular functions use positional arguments 
- However, when dealing functions that take numerical values use keyword arguments in your functions
"""

def greet_user(name):
    print(f"Hi {name}, its nice to meet you")

print("start")
greet_user("Tyronne")
print("finished")


""" Return Statements """

def emoji_converter(msg):
    words = message.split(' ')
    emojis = {
        "happy": "\U0001F973",
        "sad": "\U0001F628"
    }
    output=""
    for word in words:
        output += emojis.get(word, word) + " " 
    return output

message = input("> ")
print(emoji_converter(message))