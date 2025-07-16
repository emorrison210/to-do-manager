import json
from helpers import *

def main():
    
    menu()
    
    while True:
        to_do_list = load_list()
    
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
            if is_empty(to_do_list):
                print("List is Empty")
            else:
                view_list()
                num = int(input("What do you want to delete? "))
                to_do_list.pop(num)
        
        if choice == 4:
            break
            
                
        with open("todo_data.json", "w") as f:
                json.dump(to_do_list, f, indent=4)
    
    
    
#options() 
main()