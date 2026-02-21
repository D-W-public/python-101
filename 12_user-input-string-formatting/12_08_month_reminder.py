# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

m = int(input("Please enter a number between 1-12: "))

if m not in range(1, 13):
    print("ERROR!")
elif m in range(1, 13):
    m -= 1
    print(months[m])

# came up with this, tried to nest this didnt work... had the llm do as you ask. horrible way to design code. dont know why you would have people learnig this write it.
