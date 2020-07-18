Weight = int(input("Weight: ")) 
Dimension = input("(L)bs or (K)g: ")

is_kilo = "K"
is_pound = "L"

if Dimension.upper() == is_kilo:
     size = Weight / 0.45
     print(f" You are {size} pounds")
elif Dimension.upper() == is_pound:
    size = Weight * 0.45
    print(f" you are {size} kilograms")
