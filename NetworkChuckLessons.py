# Let's start a coffee shop together! We're going to build a coffee shop using some new Python programming concepts!

# Let's build a robot Barista!

# Greet your customer
print("Hello, welcome to Network Coffee!")

#Ask your customer what their name is with the input() function and store that in the variable NAME.
name = input("What is your name?\n")

#Greet the customer with their name and thank them for coming in today using concatenation.
if name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes" or "yes":
        print("You are not welcome here Evil Ben! Get out!")
        exit()
    else:
        print("Oh, so you are one of those good Bens. Come on in!")
else:
    print("Hello " + name + ", Thank you for coming in today!\n")

#Coffee Menu
menu = "Black Coffee, Expresso, Latte, Cappuccino, Frappuccino"

#Ask the customer what they would like from the menu and store it in the variable order.
order = input(name + ", what would you like from our menu today? Here is what are serving.\n" + menu + "\n")

#Ask the customer how many coffees they would like and store it in the variable QUANTITY
quantity = input("How many coffees would you like?\n")

#set the price for coffee

if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    price = 6
elif order == "Cappuccino":
    price = 4
else:
    print("Sorry, we do not have that today.")
    price = 0





print(price)