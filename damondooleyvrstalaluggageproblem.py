# 1. - Determine the weight of the luggage as a user defined input.
luggage = input("Welcome to the baggage check-in. Please enter the weight of your luggage in pounds: ")

# 2. - Decisions if luggage exceeds weight limit or not.
if int(luggage) >= 50.00:
    print("\nUnfortunately, your luggage exceeds the 50lb weight limit. A surcharge of $25 will be applied.")
if int(luggage) < 50.00:
    print("\nGreat. Since your bag is under the weight limit, no surcharge will be applied.")

# 3. End message.
print("\nThank you for flying with us today. Have a safe flight!")
