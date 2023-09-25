colors = {
    "apple": "red", 
    "lemon": "yellow",
    "orange": "orange",
    "honeydew": "green",
    "blueberry": "blue",
    "plum": "purple"
}
cost = {
    "apple": 10,
    "lemon": 15,
    "orange": 30,
    "honeydew": 80,
    "blueberry": 20,
    "plum": 35
}
sweet=["apple", "blueberry","plum", "orange"]
sour=["lemon", "kiwi"]
fruits = ["apple", "lemon", "orange", "kiwi", "blueberry", "plum"]
print("Would you like to list info about all the fruits we offer here, or buy a fruit?")
option=input("list/buy \n")
if option.lower()=="buy":
    print("This is what we have for mainly sweet fruits:")
    for i in fruits:
        if i in sweet:
            print(i)    
    print("This is what we have for more sour fruits:")
    for i in fruits:
        if i in sour:
            print(i)
    print("This is the cost of all the fruits in shekels, and blueberries are sold in batches of 150:")
    for item, value in cost.items():
        print(item,":", value)
    buy=input("What would you like to buy? Please only one fruit at a time. \n")
    if buy in fruits:
        if buy == "blueberry":
            amt=int(input("How many bunches? There are 150 in 1 bunch.\n"))
            money=(amt*cost[buy])
            print(f"You have bought {150*amt} {buy}(s) for {money} shekels")
        else:
            amt=int(input("How many?\n"))
            money=(amt*cost[buy])
            print(f"You have bought {amt} {buy}(s) for {money} shekels.")
if option.lower()=="list":
    print("This is all of the fruits we have, and their color")
    for item, value in colors.items():
        print(item,":", value)
elif option.lower() not in ["buy", "list"]:
    print("Sorry, this input is not accepted.")

    

