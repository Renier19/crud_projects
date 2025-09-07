to_do_dict = {}
task_id = 1       




def to_do_add():
    global task_id
    while True:
        print("TO DO: ADD")
        user_add = input("Please add to the list: ")
        to_do_dict[task_id] = user_add   
        task_id += 1

        print("Your Tasks:")
        for key, value in to_do_dict.items():
            print(f"[{key}] {value}")
        print("==================================")
        print("[1] Add another task")
        print("[2] Exit to main menu")
        user_choice = input("->: ")

        if user_choice == '1':
            continue  

        elif user_choice == '2':
            main()
            break

        else:
            print("INVALID USER INPUT")


def to_do_view():
    print("TO DO: VIEW")
    for key, value in to_do_dict.items():
        print(f"[{key}] {value}") 


def to_do_update():
    print("TO DO: UPDATE")
    to_do_view()
    
    try:
        task_num = int(input("Enter task number to update: "))

        if task_num in to_do_dict:
            to_do_dict[task_num] = to_do_dict[task_num] + "(done)"
            print("Task updated successfully.")
            to_do_view()

        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input.")


def to_do_delete():
    print("TO DO: DELETE")
    to_do_view()
    
    try:
        task_num = int(input("Enter task number to delete: "))
        if task_num in to_do_dict:
            del to_do_dict[task_num]
            print("Task deleted successfully.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input.")


def main():
    while True:
        print("\nTO-DO LIST")
        print("[1] Add")
        print("[2] View")
        print("[3] Update")
        print("[4] Delete")
        print("[5] Exit")

        user_choice = input("->: ")

        if user_choice == '1':
            to_do_add()
        elif user_choice == '2':
            to_do_view()
        elif user_choice == '3':
            to_do_update()
        elif user_choice == '4':
            to_do_delete()
        elif user_choice == '5':
            print("EXITED")
            break
        else:
            print("INVALID USER INPUT")


main()
