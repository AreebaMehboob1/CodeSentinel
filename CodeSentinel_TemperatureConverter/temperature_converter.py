temp = input("Enter temperature (e.g., 37C or 98F): ").strip()

value = float(temp[:-1])     
unit = temp[-1].upper()      

if unit == "C":
    converted = (value * 9/5) + 32
    print(f"{value}°C is equal to {converted:.2f}°F")
elif unit == "F":
    converted = (value - 32) * 5/9
    print(f"{value}°F is equal to {converted:.2f}°C")
else:
    print("Invalid input! Please enter temperature like 37C or 98F.")
