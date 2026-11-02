"""RECORD CHECK"""

label = input("Enter a label: ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

# Calculate the missing values.
difference = first - second
percent = (first / second) * 100

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  First value      : {first:>10.2f}")
print(f"  Second value     : {second:>10.2f}")
print(f"  Difference       : {difference:>+10.2f}")
print(f"  First as % of 2nd: {percent:>10.2f}%")
print(f"  Check complete   : {'OK' :>8}")
print("=" * 34)
