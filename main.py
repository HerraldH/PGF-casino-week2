# Values for the mandatory fees,
ticket_price = 14.99
mandatory_drink = 3.99
gambling_tax = 0.99
total_fees = ticket_price + mandatory_drink + gambling_tax

# Program opening,
print("-----------------------------------------------------")
print("Casino the Golden Triangle")
print("-----------------------------------------------------")
print("Please enter your information")
name = input("Name: ")
lastname = input("Lastname: ")
suffix = input("Suffix: ")

name = name.capitalize()
lastname = lastname.capitalize()
suffix = suffix.lower()

# The following code properly formats the full name,
if suffix != "":
    fullname = f"{name} {lastname} {suffix}"
elif suffix == "":
    fullname = f"{name} {lastname}"

# Requesting the users date of birth,
print("-----------------------------------------------------")
print(f"Hello {fullname}.")
print("Please enter your date of birth.")
birthday = input("[dd-mm-yyyy]: ")
if len(birthday) != 10:
    print("Error")

# The following code properly formats the date of birth and requests a confirmation from the user,
day = int(birthday[:2])
month = int(birthday[3:5])
year = int(birthday[6:])

if day <1 or day >31:
    print("Error")

if month <1 or month >12:
    print("Error")

if month == 1:
    month = "January"
elif month == 2:
    month = "February"
elif month == 3:
    month = "March"
elif month == 4:
    month = "April"
elif month == 5:
    month = "May"
elif month == 6:
    month = "June"
elif month == 7:
    month = "July"
elif month == 8:
    month = "August"
elif month == 9:
    month = "September"
elif month == 10:
    month = "October"
elif month == 11:
    month = "November"
elif month == 12:
    month = "December"

birthday_validation = f"{str(month)} {int(day)}, {int(year)}"
print(f"Is your date of birth: {birthday_validation}?")
input("[Type ['Y' for yes] & ['N' for no]: ")

# TODO utilize the current date and time to validate if the user is old enough to enter the casino, shut down program if user is underage.

# Requesting and formatting the users gender.
print("-----------------------------------------------------")
print("Please enter your gender.")
gender = input("[male, female]: ")

if gender.lower == "male" or gender.lower() == "m":
    prefix = "Mr."
elif gender.lower() == "female" or gender.lower() == "f":
    prefix = "Ms."
else:
    prefix = f" {str(name[:1])}."

# Requesting the users budget for the day.
print("-----------------------------------------------------")
print(f"Welcome {prefix} {lastname}")
print("Please enter your budget for today.")
budget = input("Budget: €")
budget = float(budget)

# TODO Make it clear that the requested budget is in euro's, then save data as a float.

# Requesting the user if he/she wants to change their budget, then requesting confirmation
print(" ")
print(" ")
print(" ")
print("-----------------------------------------------------")
print("Casino the Golden Triangle")
print("-----------------------------------------------------")
print(f"Welcome, {prefix} {lastname}")
print("At Casino TGT, we charge the following fixed fees.")
print("-----------------------------------------------------")
print(f"Entree fee:                                   € {ticket_price:.2f}")
print(f"Mandatory drink:                              € {mandatory_drink:.2f}")
print(f"Gambling tax:                                 € {gambling_tax:.2f}")
print(" ")
print(f"Total:                                        € {total_fees:.2f}")
print("-----------------------------------------------------")
print(" ")
print("Do you wish to continue?")
fixed_fees_validation = input("Type ['Y' for yes] & ['N' for no]: ")

# TODO Turn the above into a loop to properly validate the users input.

# Validating the users input,
if fixed_fees_validation.lower() == "yes" or fixed_fees_validation.lower() == "y":
    print(" ")
else:
    print("Error")

# TODO Tell the user by how much their budget for the day is insufficient.

if budget < total_fees:
    print("You're budget for today is insufficient.")
    print("Have a nice day.")
else:
    print(" ")
    print(" ")
    print(" ")
    print("-----------------------------------------------------")
    print("Casino the Golden Triangle")
    print("-----------------------------------------------------")
    print(f"Welcome, {prefix} {lastname}")
    print(f"Your budget for today is €{round(budget - total_fees, 2)}")
    print("-----------------------------------------------------")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("-----------------------------------------------------")
    print(" ")

# TODO Improve writing comments. Explain why the code does something, not what it does.

