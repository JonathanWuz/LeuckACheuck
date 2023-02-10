from main import buildMenu
from main import banner
from main import dessert_list

def dessert():
    title = "Types of Desserts" + banner
    buildMenu(title, dessert_list)

if __name__ == "__main__":
    dessert()