student_list = []
student_record = {}

def add_student():
    while True:
        print("ADD STUDENT")
        student_id = input("Enter Student Number: ")
        while not (len(student_id) == 12 and student_id.isdigit()):
            print("INVALID ID NUMBER")
            student_id = input("Enter Student Number: ")

        student_name = input("Enter Student Name: ").upper()
        student_list.append((student_id, student_name))
        view_student_list()

        print("[1] ADD ANOTHER STUDENT")
        print("[2] EXIT")
        user_choice = input("-->: ")
        if user_choice == '1':
            continue   
        elif user_choice == '2':
            return    
        else:
            print("INVALID USER INPUT")

def add_student_grade():
    print("ADD STUDENT GRADE")
    view_student_list()
    while True:
        student_search = input("Enter ID: ")
        student_id = None
        for s_id, s_name in student_list:  
            if student_search == s_id:
                student_id = s_id
                break
        if student_id is None:
            print("STUDENT NOT FOUND")
            continue

        while True:
            try:
                print("MATH")
                math_grades = int(input("-->"))
                print("ENGLISH")
                english_grades = int(input("-->"))
                print("FILIPINO")
                filipino_grades = int(input("-->"))
                print("HISTORY")
                history_grades = int(input("-->"))
                print("PE")
                pe_grades = int(input("-->"))

                student_record[student_id] = {
                    "Math": math_grades,
                    "English": english_grades,
                    "Filipino": filipino_grades,
                    "History": history_grades,
                    "PE": pe_grades
                }

                print("\nStudent Record:")
                for s_id, s_name in student_list:
                    print(f"{s_id}: {s_name}")
                    if s_id in student_record:
                        for subject, grade in student_record[s_id].items():
                            print(f"{subject}: {grade}")
                    else:
                        print("No grades yet")
                break
            except ValueError:
                print("INVALID USER INPUT")

        print("[1] ADD ANOTHER GRADE")
        print("[2] EXIT")
        user_choice = input("-->: ")
        if user_choice == '1':
            continue   
        elif user_choice == '2':
            return     
        else:
            print("INVALID USER INPUT")

def get_student_average():
    print("GET STUDENT AVERAGE")

def view_student_list():
    print("\nStudent Record:")
    for student_id, student_name in student_list:
        print(f"{student_id}: {student_name}")
        if student_id in student_record:
            for subject, grade in student_record[student_id].items():
                print(f"{subject}: {grade}")
        else:
            print("No grades yet")

        
def remove_student():
    print("REMOVE STUDENT")
    view_student_list()
    try:

        student_id = input("Enter Student ID")
        if student_id in student_record:
            del student_record[student_id] 
            student_list.remove(student_id)
        
        view_student_list()
    except ValueError:
        print("INVALID USER INPUT")

def main():
    while True:
        print("\n--- MAIN MENU ---")
        print("[1] ADD STUDENT")
        print("[2] ADD STUDENT GRADE")
        print("[3] GET STUDENT AVERAGE")
        print("[4] STUDENT LIST")
        print("[5] REMOVE STUDENT")
        print("[6] EXIT")
        
        user_choice = input("-->: ")
        if user_choice == '1':
            add_student()
        elif user_choice == '2':
            add_student_grade()
        elif user_choice == '3':
            get_student_average()
        elif user_choice == '4':
            view_student_list()
        elif user_choice == '5':
            remove_student()
        elif user_choice == '6':
            print("EXITED")
            break
        else:
            print("INVALID USER INPUT")

main()
