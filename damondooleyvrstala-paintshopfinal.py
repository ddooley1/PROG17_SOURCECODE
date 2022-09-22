# LAB 1 - THE PAINT SHOP
# Code a Python program that calculates the amount of paint you need to cover the walls in your family room. 
# The salesperson at the home improvement store told you to buy 1 gallon of paint for every 150 square feet of 
# wall you need to paint.

# Assuming that the room is rectangular in shape, the program should take in as input the width of your 
# two sets of walls and the height of the room.

# The program should output the number of gallons required to paint the room. 
# Paint is sold only by the gallon.

#Purpose/Concepts: Input and output to screen, string concatentation, datatype casting, simple math operations

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # 1 - Welcome Message
    print("Welcome to Damon's Paint Shop!")
    print("This is a program that will determine how much paint you will need to paint your walls in gallons.")

    # 2 - Enter inputs for dimensions of the room
    roomwidth1=input("Please enter the width the first wall in your room, in feet.") #testvalue = 14.5
    roomwidth2 = input("Please enter the width of the second wall in your room, in feet.") #testvalue = 19.12
    roomheight=input("Plese enter the height of your room in feet.") #testvalue =12.86
    roomarea = 0.0
    
    # 3 - Convert inputs to float
    convertedwidth1 = float(roomwidth1) * 2
    convertedwidth2 = float(roomwidth2) * 2
    convertedheight = float(roomheight)
    convertedarea = float(roomarea)
    gallontotal = 0.0

    # 4 - Calculate room area (height * width)
    convertedarea = convertedwidth1 + convertedwidth2 * convertedheight

    # 5 - Display amount of gallons needed for painting the room
    gallontotal = convertedarea / 150
    print("You will need "+ str(gallontotal)+ " gallons of paint to paint your room.")

    # 6 - Display thank you message to user
    print("Thank you for using Damon's Paint Shop. Have a great day!")

    
    # YOUR CODE ENDS HERE

main()