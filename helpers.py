import json

def load_list():
    try:
        with open("todo_data.json", "r") as f:
            to_do_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        to_do_list = {}
    fixed_list = {}
    for key in to_do_list:
        fixed_list[int(key)] = to_do_list[key]   
    to_do_list = fixed_list
    return to_do_list

def options():
    while True:
        option = int(input("\nPress a number: "))
        if option not in (range(1, 5)):
            print("Error enter in a number 1-4")
            continue
        else:
            return option

def view_list():
    to_do_list = load_list()
    if not to_do_list:
        print("List is Empty")
        return
    for key, value in to_do_list.items():
        print(f"\n{key}: {value['description']}")

def add_item():
    item = str(input("What do you want to add to your to do list?\n"))
    return item

def remove_item():
    num = int(input("Enter the number of the item you want to remove: "))
    return num

def is_empty(list):
    if list:
        return False
    if not list:
        return True
    
def menu():
    print("------------------------")
    print("1. View your to do list \n2. Add \n3. Remove \n4. Exit")
    print("------------------------")