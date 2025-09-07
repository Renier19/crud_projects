contacts = {}

def add_contact():
    print("ADD CONTACT")
    contact_number = input("Please enter Contact number: ")

    while not (len(contact_number)==11 and  contact_number.isdigit()):
        print("Youre number is invalid!!")
        contact_number = input("Please enter Contact number: ")


    contact_name = input("Please enter contact name: ")
    contacts [contact_name] = contact_number
    print("UPDATED CONTACTS")

    for key,value in contacts.items():
        print(f"[{key}:{value}]") 
    return main()
    
def search_contact():
    print("SEARCH CONTACT")
    contact_search = input("Please Enter Name to search: ")

    if contact_search in contacts:
        number = contacts[contact_search]
        print("CONTACT FOUND")
        print(f"{contact_search}: {number}")

    else:
        print(f"{contact_search} does not exist in your contacts")
    return main()
     
def delete_contact():
    print("DELETE CONTACT")
    contact_search = input("Please enter name to delete: ")

    if contact_search in contacts:
        contacts.pop(contact_search)
        print("CONTACT DELETED")
        print("UPDATED CONTACTS")
        for key,value in contacts.items():
            print(f"[{key}:{value}]") 

    else:
        print(f"{contact_search} does not exist in your contacts")
    return main()

def display_contact():
    print("ALL CONTACTS")

    for key,value in contacts.items():
        print(f"[{key}:{value}]")
    return main()

def main():

    while True:
        print("CONTACTS")
        print("[1] Add Contact")
        print("[2] Search Contact")
        print("[3] Delete Contact")
        print("[4] Display All Contacts")
        print("[5] Exit")
        choice = input("Please Select: ")

        if choice == '1':
            add_contact()
            break

        elif choice == '2':
            search_contact()
            break
            
        elif choice == '3':
            delete_contact()
            break

        elif choice == '4':
            display_contact()
            break

        elif choice == '5':
            print("EXITED")
            break  
        else:
            print(f"{choice} is not in the choices")
            
main()
    


