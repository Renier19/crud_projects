import json

student_list = []
student_record = {}



def do_it_again():
    while True:
        print("=======ASK AGAIN =======")
        print("[1] DO IT AGAIN")
        print("[2] EXIT")
        user_choice = input("-->: ")
        if user_choice == '1':
            break
         
        elif user_choice == '2':
            main()

        else:
            print("INVALID USER INPUT")


            
def add_students():
    while True:
        print("=======ADD STUDENT=======")
        student_id = input("ENTER STUDENT ID: ")
        while not (len(student_id) == 5 and student_id.isdigit()):
            print("INVALID USER INPUT(SHOULD BE 5 DIGITS)")
            student_id = input("ENTER SUTDENT ID: ")
        student_name = input("PLEASE INPUT STUDENT NAME: ").upper()
        while not(student_name.isalpha()):
            print("INVALID USER INPUT(SHOULD NOT CONTAIN SPECIAL CHARACTERS")
            student_name = input("PLEASE INPUT STUDENT NAME: ").upper()
        student_list.append((student_id, student_name))
        view_list()
        do_it_again()
           
def add_grades():
    print("=======ADD GRADES=======")
    view_list()
    while True:
        student_id_search = input("ENTER STUDENT ID: ")
        found = False    

        for student_id, student_name in student_list:    
            if student_id == student_id_search:
                print(f"STUDENT FOUND: {student_name}")
                found = True
               
                if student_id_search not in student_record:
                    student_record[student_id_search] = {}
               
                for subject in ["MATH", "SCIENCE", "ENGLISH", "FILIPINO", "PE"]:
                    while True:
                        try:
                            grade = int(input(f"Enter grade for {subject}: "))
                            if 0 <= grade <= 100:
                                student_record[student_id_search][subject] = grade
                                break
                            else:
                                print("Grade must be between 0 and 100")
                        except ValueError:
                            print("INVALID USER INPUT (please enter numbers only)")

                view_list()
                do_it_again()
                break  
        if not found:
            print("STUDENT NOT FOUND")
        
def get_average():
    print("=======GET AVERAGE======")
    for student_id,student_name in student_list:
        print(f"{student_id} : {student_name}")
        if student_id in student_record:
            grades = student_record[student_id].values()
            total = sum(grades)
            average = total / len(grades)
            print(f"AVERAGE: {average}")
        else:
            print("NO GRADES YET")       

def view_list():
        print("=======VIEW LIST======")
        for student_id, student_name in student_list:
            print(f"{student_id} : {student_name}")
            if student_id in student_record:
                for subject, student_grade in student_record[student_id].items():
                    print(f"{subject} : {student_grade}")    
            else:
                print("NO GRADES YET")

            

def remove_student():
    print("=======REMOVE STUDENT======")
    view_list()
    remove_id_student = input("ENTER STUDENT ID TO REMOVE STUDENT: ")
    for student in student_list:
        if student[0] == remove_id_student:
            student_list.remove(student)
            view_list()
            do_it_again()
            break
            

def main():
    while True:
        print("=======STUDENT MANAGEMENT SYSTEM=====")
        print("[1] ADD STUDENT")
        print("[2] ADD GRADES")
        print("[3] GET AVERAGE")
        print("[4] VIEW LIST")
        print("[5] REMOVE STUDENT")
        print("[6] EXIT")
        user_choice = input("-->: ")
        
        if user_choice == '1':
            add_students()
        
        elif user_choice == '2':
            add_grades()
        
        elif user_choice == '3':
            get_average()

        elif user_choice == '4':
            view_list()

        elif user_choice == '5':
            remove_student()
            
        elif user_choice == '6':
            print("EXITED")
            break
        else:
            print("INVALID USER INPUT")


main()




