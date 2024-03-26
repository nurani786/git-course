#Program for checking weight of a person
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
   converted = weight * 0.45
   print(f"You're {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You're {converted} pounds")
    print("-"*45)