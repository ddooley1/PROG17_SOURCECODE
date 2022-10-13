# 1 . This is a program that will calculate hourly wage rates, based on user given inputs for hours worked and pay rate.
# This will also account for overtime, if they worked over 40 hours in a week. 

hoursworked = float(input("Please enter the amount of hours you have worked this week: "))
hourlyrate = float(input("Please enter your hourly pay rate: $"))
overtimehours = float(40)
overtimepayrate = float(1.5)

# 2. Run initial calc ( hours worked * pay rate )
finalpay = float(hoursworked) * float(hourlyrate)

# 3. Find overtime hours.
overtimemultiplier = float(hoursworked) - float(overtimehours)


# 4. Run IF statements & Display info to user.

if hoursworked > float(40):
    overtimepay = (float(overtimemultiplier) * float(hourlyrate)) * float(overtimepayrate)
    finalpayOT = float(finalpay) + float(overtimepay)
    print("Your final pay for this week is: ${0:.2f}. You made ${1:.2f} in overtime for this pay period.".format(finalpayOT,overtimepay))

else:
    print("Your final pay for this week is: ${0:.2f}.".format(finalpay))

print("End of program.")

    