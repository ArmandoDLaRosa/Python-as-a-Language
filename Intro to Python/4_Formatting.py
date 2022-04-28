print("\n")

# Create a number with certain base other than 10
base_16 = int("E7", base = 16)
print(f"HEX to DEC: {base_16:d}")

# RGB to HEX
rgb = (12, 205, 81)
hex_color = "\n#" + "".join([f"{channel:02x}" for channel in rgb])
print(hex_color)

# Static f-String, won't change if variable changes
print("\nTesting Static F-Strings")

age = 21
fString = f"I'm {age} years old"
print(fString)

age = 22
print(fString)

decimal = 4863.4343091
percentage = .25
print(f"Percentage       {percentage:.2%}")  # Show as percentage
print(f"Thousands split  {decimal:,}")       # split thousands with , or _
print(f"Decimal rounding {decimal:.2}")      # will show as e+0#
print(f"Decimal rounding {decimal:.2f}")     # will show as float

base_10 = 100
print(f"Binary           {base_10:b}")  # binary
print(f"Octal            {base_10:o}")  # octal
print(f"Hex              {base_10:x}")  # hexadecimal

# NESTED STRING INTERPOLATION
number_of_files = 3
number_digits = int(input("\nHow many digits are used in the numbering scheme? "))

for file_number in range(1, number_of_files + 1):
	print("image{number:0{padding_amount}}.png".format(
		number=file_number,
		padding_amount=number_digits
	))

# UnStatic f-Strings, will change if variable changes
print("\nTesting Not Static F-Strings")

fString = "I'm {} years old, Hello {nameVar}"

age = 21
name = "Armando"
print(fString.format(age, nameVar = name))

age = 22
name = "Erick"
print(fString.format(age, nameVar = name))

decimal = 4863.4343091
print("Thousands split  {:_}".format(decimal))  # split thousands with , or _
print("Decimal rounding {:.2}".format(decimal))
print("Decimal rounding {:.2f}".format(decimal))

print("\n")
