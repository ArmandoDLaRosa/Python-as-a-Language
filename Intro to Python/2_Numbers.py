print("\n")

# DATA TYPES
age = 21 # Int
EULER = 0.577 #Float

# PEMDAS
print("PEMDAS________________")
print("Math Operation    ", 3**2-(1*2)+1)
print("Division          ", 5/5) # Division always outputs a float
                                 # Unlike SQL, that unless you've a float it
                                 # just sees the integer part of a number(in some SQL variants)
print("Division II       ", 5/2)

print("Int Division      ", 5//5)  # This works as SQL division, ignoring the decimals meaning no rounding
print("Int Division II   ", 5//2)  

print("Modulus/remainder ", 10%2)  # ODD
print("Modulus/remainder ", 11%2)  # EVEN

# USE case for % operator
x = int(input("\nInput an Integer Number:"))
print("is the input Even or Odd? ....", "Odd" if x%2 == 0 else "Even")

# DIVMOD
rawTime = 126 # minutes, for example
hours, minutes  = divmod(rawTime, 60)
print(f"\nDivMod Test - Hours: {hours}, Minutes: {minutes}" )

print("\n")