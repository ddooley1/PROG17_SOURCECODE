#Complex decisions - ELIF and multipart logic

#country = input("What country are you from?: ")

#if country == "Canada":
#    print("Hello, eh bud?")

#elif country == "Germany":
#    print("Guten tag!")

#elif country == "France":
#    print("Bonjour!")

#COMBINING ANDS / ORS
country = input("What country are you from?").upper()
pet = input("What kind of pet do you have?").upper()

if country == "CANADA" and\
    (pet == "MOOSE" or pet == "BEAVER"):
    print("Do you play hockey too?")

#print("End of program.")