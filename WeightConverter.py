weight=float(input("Enter your weight: "))
unit=input("Kilograms or Pounds? (K/L): ")
if unit=='K':
    print(f"{weight*2.205}LB/S")
elif unit=='L':
    print(f"{weight/2.205}KG/S")
else:
    print(f"{unit} was not valid")