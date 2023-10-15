# This code determines the chinese zodiac sign of the user input year.
# And also only accepts an integer input.

# Validates if the input is an integer and gets the valid input year
def valid_year():
    while True:
        try:
            year_1 = int(input("Enter a year: "))
            return year_1
        except ValueError:
            print("Invalid year, Please enter an integer.")


# Get the input year using the function
year_2 = valid_year()

# Determine the Chinese zodiac sign based on the given year
if year_2 % 12 == 0:
    zodiac_sign = "Monkey"
elif year_2 % 12 == 1:
    zodiac_sign = "Rooster"
elif year_2 % 12 == 2:
    zodiac_sign = "Dog"
elif year_2 % 12 == 3:
    zodiac_sign = "Pig"
elif year_2 % 12 == 4:
    zodiac_sign = "Rat"
elif year_2 % 12 == 5:
    zodiac_sign = "Ox"
elif year_2 % 12 == 6:
    zodiac_sign = "Tiger"
elif year_2 % 12 == 7:
    zodiac_sign = "Rabbit"
elif year_2 % 12 == 8:
    zodiac_sign = "Dragon"
elif year_2 % 12 == 9:
    zodiac_sign = "Snake"
elif year_2 % 12 == 10:
    zodiac_sign = "Horse"
else:
    zodiac_sign = "Sheep"

# Print the result
print("The Chinese zodiac sign for the year " + str(year_2) + " is " + str(zodiac_sign) + ".")
