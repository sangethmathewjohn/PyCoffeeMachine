from os import system
import time
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}
profit =0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def clear(n):
    time.sleep(n)
    system('cls')
    #sytem('clear') for linux system 

def sufficient(resources,ingredients):
    for item in resources:
        if resources[item]<ingredients[item]:
            print(f"Sorry {item} is insufficient!!!")
            return False
    return True

def calculate():
    print("Insert coins !!!")
    total =int(input("How many 1 value coins: "))
    total +=int(input("How many 2 value coins: "))*2
    total +=int(input("How many 5 value coins: "))*5
    total +=int(input("How many 10 value coins: "))*10
    return total

def transaction(money,cost):
    if money<cost:
        print("Transaction is insufficient")
        return False
    else:
        global profit
        profit+=cost
        print("Transaction Succeeded")
        if money>cost:
            print(f"Transaction Balance:{money-cost}")
        return True

def make(cofee,choice):
    for item in cofee:
        global resources
        resources[item]-=cofee[item]
    print(f"Here is Your {choice}")
select=True
state = True
while state:
    while select:
        choice = input("What would you like to have: (espresso, cappuccino, latte):").lower()
        list=["espresso","cappuccino","latte","report","off"]
        if choice not in list:
            print("Invalid choice!!!") 
            clear(2)
        else:
            select = False

    if choice =='off':
        state = False
    elif choice =='report':
        print(f"water  :{resources['water']}ml")
        print(f"milk   :{resources['milk']}ml")
        print(f"coffee :{resources['coffee']}gm")
        print(f"Profit :{profit}")
        back = input("Enter to go back:")
    else:
        drink = MENU[choice]
        if sufficient(resources,drink['ingredients']):
            print(f"Cost: {drink['cost']}")
            payment =calculate()

            if transaction(payment,drink["cost"]):
                make(drink["ingredients"],choice)
                choice=""             
                clear(3)
       
    for item in resources:
        if resources[item]==0:
            print("Machine out of Order!!!")
            clear(20)
            choice='off'
            state=False
        else:
            choice=""
    select= True 
    clear(0)
    
    

