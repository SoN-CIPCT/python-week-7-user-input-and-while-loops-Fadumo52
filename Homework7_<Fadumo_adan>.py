Pizza_Orders= ["Cheese","Chicken","Veggie","Hawaiian","Margherita"]
Finished_Pizzas= []
while Pizza_Orders:
    Current_Pizza=Pizza_Orders.pop(0)
    print("Your pizza pie is finished!")
    Finished_Pizzas.append(Current_Pizza)

for Pizza in Finished_Pizzas:
    print(f"The Pizza {Pizza} was made.")