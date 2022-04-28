print("\n")
# You can use " or ' as long as they match
myString = "Hello World!"
myString2 = 'Hello World!'
print("Test1: ", myString)

# But... sometimes you've ' inside the string
print("\nMix  : ", "It's cool")        # option 1 - mix "  and '
print("Scape: ", "He said \"hi\"" )  # option 2 - use \ before the " or '
print("Scape: ", 'He\'s happy') 

# Sometimes you need multiline, like for a query
query = """SELECT *
            FROM Table"""
print("\nMultiline: ", query)

# Operations
print( "\nConcatenation_" + str(5))

stringNumber = "5"
print( "Casting", int(stringNumber) + 5)

# LONG COMMENTS
"""
Write a longer comment
1)
2)
3)
"""
print("\n")