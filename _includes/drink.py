from main import buildMenu
from main import banner
from main import drink_list

def drink():
    title = "Types of Drinks" + banner
    buildMenu(title, drink_list)

if __name__ == "__main__":
    drink()