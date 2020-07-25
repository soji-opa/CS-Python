""" Try and Except 

- In this case we try to stop our code from crashing and handling errors in our programme

- It is needed to handle exceptions so as to stop our code from crashing
"""

try:
    age = int(input('Age: '))
    print(age)
    income = 3000 
    risk = income/age
    print(risk)
except ZeroDivisionError:
    print('Use a value larger than zero')

except ValueError:
    print('Invalid value')