import json

student_list = []
student_record = {}



def do_it_again():
    while True:
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
        student_id = None
        for student_id, student_name in student_list:
            if student_id == student_id_search:
                print("STUDENT FOUND")
                try:
                    math_grade = int(input("MATH: "))
                    english_grade = int(input("ENGLISH: "))
                    science_grade = int(input("SCIENCE: "))
                    history_grade = int(input("HISTORY: "))
                    pe_grade = int(input("PE: "))
                except ValueError:
                    print("INVALID USER INPUT")
                
                student_record[student_id] = {"MATH" : math_grade,
                                            "ENGLISH" : english_grade,
                                            "SCINCE" : science_grade,
                                            "HISTORY" : history_grade,
                                            "PE" : history_grade 
                                            } 
            
            else:
                print("STUDENT NOT FOUND")

def get_average():
    print("=======GET AVERAGE======")

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




