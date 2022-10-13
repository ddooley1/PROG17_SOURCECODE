16 lines (6 sloc)  254 Bytes

#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    
    # 1. - Define what data we need to collect from user. Name, KM delivery and record cost.

    custname =input("Enter the customers name: ")
    kilometers = input("Enter the distance in kilometers for delivery: ")
    recordcost = input("Enter the cost of records purchased: ")

    # 2. - Define values in memory.

    deliveryrate = float(15.00)
    salestax = float(0.14)
    deliverycost = float(0.0)

    # 3. - Calculate delivery cost. (deliverycost=kilometers*deliveryrate)

    deliverycost = float(kilometers) * float(deliveryrate)

    # 4. - Calculate sales tax. (recordcost * salestax)

    totaltax = float(recordcost) * (salestax)

    # 5. - Calculate purchase cost. (recordcost + salestax)

    purchasecost = float(recordcost) + float(totaltax)

    # 6. - Calculate final total. (finaltotal = recordcost + deliverycost + totaltax)

    finaltotal = float(recordcost) + float(deliverycost) + float(totaltax)

    # 7. - Display information to user.

    print("Purchase summary for {0}".format(custname))
    print("Delivery Cost: ${0:.2f}".format(deliverycost))
    print("Purchase Cost: ${0:.2f}".format(purchasecost))
    print("Total Cost: ${0:.2f}".format(finaltotal))

    # YOUR CODE ENDS HERE

main()