import json

def options():
    print("1. View your to do list \n2. Add \n3. Remove \n4. Exit")
    while True:
        option = int(input("Press a number: "))
        if option not in (range(1, 5)):
            print("Error enter in a number 1-4")
            continue
        else:
            return option

def view_list():
    try:
        with open("todo_data.json", "r") as f:
            view_tasks = json.load(f)
            if not view_tasks:
                print("Your to-do list is empty.")
                return True
            else:
                print(json.dumps(view_tasks, indent=4))
                return False
    except FileNotFoundError:
        print("No to-do list found.")

def add_item():
    item = str(input("What do you want to add to your to do list?\n"))
    return item

def remove_item():
    num = int(input("Enter the number of the item you want to remove: "))
    return num

def main():
    try:
        with open("todo_data.json", "r") as f:
            to_do_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        to_do_list = {}
    
    #fixing to_do_list so the id key is changed from str to int
    fixed_list = {}
    for key in to_do_list:
        fixed_list[int(key)] = to_do_list[key]   
    to_do_list = fixed_list
    
    choice = options()
    
    if choice == 1:
        view_list()
        
    if choice == 2:
        item = add_item()
        
        # Determine the next available ID
        if len(to_do_list) == 0:
            next_id = 1
        else:
            next_id = max(to_do_list.keys()) + 1

        # Add the new item
        to_do_list[next_id] = {"description": item}
            
    if choice == 3:
        #checking if list is empty
        if view_list() == False:
            id = remove_item()
            if id == max(to_do_list.keys()):
                to_do_list.pop(id)
            elif id == min(to_do_list.keys()):
                to_do_list.pop(id)
                new_list = {key - 1: v for key, v in to_do_list.items()}
                to_do_list = new_list
            else:
                to_do_list.pop(id)
                new_list = {}
                for key in to_do_list:
                    if key > id:
                        new_list[key - 1] = to_do_list[key]
                    else:
                        new_list[key] = to_do_list[key]
                to_do_list = new_list
            
    with open("todo_data.json", "w") as f:
            json.dump(to_do_list, f, indent=4)
    
    
    
#options() 
main()