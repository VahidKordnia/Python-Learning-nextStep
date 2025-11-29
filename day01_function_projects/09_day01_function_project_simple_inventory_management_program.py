
# Session04-Function-simple inventory management program-project

# in this project, we want to write a program that can report, add, remove, and edit products in a shop or warehouse.



# Supporting Code:

inventory = {}

def add():

    product_name = input("Enter product's name: ")

    while True:
        try:
            product_price = int(input("Enter product's price: "))
            break
        except ValueError:
            print("invalid input!\n")
            continue

    while True:
        try:
            product_stock = int(input("Enter product's stock: "))
            break
        except ValueError:
            print("invalid input!\n")
            continue   

    ID = len(inventory) + 1

    inventory[ID] = [product_name, product_price, product_stock]  


def search():
    
    while True:
        try:
            choice = int(input("find by:\n1. ID\n2. name\n3. Back\n"))
        except ValueError:
            print("invalid input!\n")
            continue

        options = (1, 2, 3)    
        if choice not in options:
            print("invalid input!\n")
            continue
        else:
            break

    if choice == 1:
        while True:
            try:
                ID = int(input("Enter the product's ID: "))
            except ValueError:
                print("invalid input!\n")
                continue
            if ID not in inventory.keys():
                print("There is no product with this ID!\n")
                continue
            else:
                break
        return ID    

    elif choice == 2:
        while True:
            name = input("Enter product's name: ")
            for k, v in inventory.items():
                if name in v:
                    ID = k
                    return ID
            print("There is no product with this name!\n")
            continue
                    
    else:
        return 0               


def edit():

    while True:
        try:
            choice = int(input("1. edit name\n2. edit price\n3. edit stock\n4. back\n"))
        except ValueError:
            print("invalid input!\n")
            continue

        options = (1, 2, 3, 4)    
        if choice not in options:
            print("invalid input!\n")
            continue
        else:
            break

    if choice == 1:
        new_name = input("Enter the new name: ")
        inventory[ID][0] = new_name
        
    elif choice == 2:
        while True:
            try:
                new_price = int(input("Enter the new price: "))
                break
            except ValueError:
                print("invalid input\n")
                continue
            
        inventory[ID][1] = new_price

    elif choice == 3:
        while True:
            try:
                new_stock = int(input("Enter the new stock: "))
                break
            except ValueError:
                print("invalid input\n")
                continue
            
        inventory[ID][2] = new_stock
    else:
        return 0



# Core code:

while True:

    while True:
        try:
            choice = int(input("1. report\n2. add\n3. remove\n4. edit\n5. exit\n"))
        except ValueError:
            print("invalid input!\n")
            continue
        options = (1, 2, 3, 4, 5)
        if choice in options:
            break
        else:
            print("invalid input!\n")
            continue

    if choice == 1:
        if inventory == {}:
            print("There is nothing to report!\n")
        else:
            print('"product ID- Product name, product price, product stock:"\n')
            for k, v in inventory.items():
              print(f"{k}- {v[0]}, {v[1]}, {v[2]}")
              print("----------------------------")  

    elif choice == 2:
        add()
        print("----- The product was added successfully. -----\n")

    elif choice == 3:
        ID = search()
        if ID != 0:
            inventory.pop(ID)
            print("----- The product was removed successfully. -----\n")
        else:
            continue

    elif choice == 4:
        ID = search()
        if ID != 0:
            a = edit()
            if a != 0:
                print("edited successfully!\n")
            else:
                continue
        else:
            continue

    else:
        break        
