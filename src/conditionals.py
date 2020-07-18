""" If statements """

# is_hot = False
# is_cold =  False

# if is_hot:
#     print("it's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("it's a cold day")
#     print("wear warm clothes")
# else: 
#     print("it's a lovely day")
# print("Enjoy your day")

##

# is_credit = False
# price = 100000
# if is_credit:
#     down_payment = 0.1 * price   
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")

""" Logical Operators """

#logical and operators -  the two statements have to be true to ensure outcome is positive
# has_high_income = True
# has_good_credit = True
# if has_good_credit and has_high_income:
#     print("Eligible for loan")

# logical OR operator - one of the conditions must be evaluated to true to ensure outcome is positive

# has_high_income = True
# has_good_credit = False
# if has_good_credit or has_high_income:
#     print("Eligible for loan")

#logical NOT operator - the NOT operator inverses things 

# has_criminal_record = True
# has_good_credit = True

# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")
# else: 
#     print("Not eligible for loan has criminal records")

""" Comparison Operators """
# greater than >
# less than <
# equal to ==
# greater than/ equal to >=
# less than / equal to <=

# character_lenght = 3

# if character_lenght < 3:
#     print("name must be atleast three characters")
# elif character_lenght > 50:
#     print("name can be only be a maximum of 50 characters")
# else:
#     print("name is perfect")


name = input("Please enter a name: ")

if len(name)<3:
    print("name must be atleast three characters")
elif len(name) > 50:
    print ("name can be only be a maximum of 50 characters")
else:
    print ("name is perfect")