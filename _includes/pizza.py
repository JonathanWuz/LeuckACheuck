from main import buildMenu
from main import banner
from main import pizza_list

def pizza():
    title = "Types of Pizzas" + banner
    buildMenu(title, pizza_list)
  
if __name__ == "__main__":
    pizza()