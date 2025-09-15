unit=input("Is this temperature in Celcius or Fahrenheit? (C/F): ")
temp=float(input("Enter temperature: "))
if unit=='C':
    temp=(temp*(9/5))+32
    print(f"{round(temp,2)}F")
elif unit=='F':
    temp=(temp-32)*(5/9)
    print(f"{round(temp)}C")
else:
    print(f"{unit} is invalid")