main_menu = []

pizza_list = [
    ["Cheese","$1.50"],
    ["Pepperoni","$2.50"],
    ["Vegetarian","$2.50"]
]

drink_list = [
    ["Soda","$1.00"],
    ["Juice","$1.00"],
    ["Water","$0"]
]

dessert_list = [
    ["Icecream","$1.50"],
    ["Cookie","$1.00"],
    ["Cake","$3.00"]
]

menu_list = []

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    print()
    title = "Welcome to the Pizzeria!" + banner
    menu_list.append(["Pizza", "pizza.py"])
    menu_list.append(["Drinks", "drink.py"])
    menu_list.append(["Desserts", "dessert.py"])
    menu_list.append(["Checkout", None])
    buildMenu(title, menu_list)

def check_out(done_list):
    print("")
    print("")
    print("=========================================")
    print("   You selected the following item(s): ")
    total_cost = float(0)
    for item in done_list:
        print("          " + item[0], '->', item[1])
        total_cost = total_cost + float(item[1].replace("$",""))

    print("   Total cost is $" + str(total_cost))
    print("=========================================")


selected_list = []

def buildMenu(banner, options):
    print(banner)
  
    if("Welcome to the Pizzeria!" in banner):
      prompts = {0: ["Main Menu", None]}
    else:
      prompts = {0: ["Return to Main Menu", None]}

    for op in options:
        index = len(prompts)
        prompts[index] = op
      
    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")
  
    try:
        choice = int(choice)
        if choice == 0:
          if("Welcome to the Pizzeria!" in banner):
            buildMenu(banner, options)
          else:
            return
            
        if choice == 4:
            check_out(selected_list)
            exit()
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try: 
                exec(open(action).read())
            except FileNotFoundError:
                print(f"You selected {prompts.get(choice)[0]}, the price is {prompts.get(choice)[1]}")
                selected_list.append([prompts.get(choice)[0], prompts.get(choice)[1]])
                banner = f"\n{border}\nPlease Select An Option\n{border}"
                options = menu_list
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")

    buildMenu(banner, options) 

if __name__ == "__main__":
    menu()