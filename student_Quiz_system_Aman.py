#========================
#Task 1 : Registration
#========================

#declare variable 
students = []

#declare register_student function
def registerStudent():
    """تسجيل طالب جديد وحفظ بياناته في القائمة العامة """

    name = input("please , enter student's name :").strip()
    age = input("enter student's age :").strip()
    subjects = input("enter favorite subjects for student with comma separated : ").strip()
    
    #first conver subjects to list 
    subjects_list = [s.strip() for s in subjects.split(",")]
    subjects_tuple = tuple(subjects_list)
    #student_data.append(subjects_tuple)
    
    #second store all student data in dictionary
    student_data = {
        "name": name ,
        "age": age ,
        "subjects": subjects_tuple ,
        "score": 0     
    }
    students.append(student_data)
    
    #display success message
    print(f"\n student {name} register successfully \n")   

registerStudent()
print(students)

#========================
#Task 2 : Quiz Function
#========================
#declare quiz_quesions function
def quizQuesions(student):
    """تقوم ببدء اختبار بسيط، وحساب النتيجة، وحفظها في قاموس الطالب"""
    
    quiz_quesions = [
        {
            "question": "?ماذا تعرف علن لغة البرمجة",
            "answer" :"answer1"
            
        },
        {
            
            "question": "?ما هى اللغة التي ترغب بدراستها",
            "answer" : "answer2"
        },
        {
            
            "question": "?ما خو اختصار لغة البرمجة بايثون",
            "answer" : "py"
        }
    ]
    #start ask student  quesions 
    current_score =0
    question_num = 1
    print(f"\n start question for {student['name']} student \n")
    
    for q in quiz_quesions:
        student_answer = input(f"\n quesion {question_num} is : {q['question']} \n your answer is : ")
        student_answer = student_answer.strip().lower()
        correct_answer = q['answer'].strip().lower()
        
        if student_answer == correct_answer:
            print("your answer is correct")
            current_score +=1
        else:
            print(f"your answer is incorrect the correct answer is {q['answer']} \n")
            
        question_num +=1
            
    # save studen's score with submitted score
    student["score"] = current_score 
    
        
    print(f"\n end of quiz the total score for {student["name"]} student is {current_score} from {len(quiz_quesions)} question \n ")
        
    return student

quizQuesions(students[0])
        
#========================
#Task 3 : Report Function
#========================

#declare show_report function
def showRport():
    print("\n" + "="*40)
    print("Report of students's data")
    print("="*40)
    
    # 1. التحقق من وجود طلاب
    if not students:
        print("there is not students registered yet")
        return  # to stop function execution if condition is true

    # display all students in student dictionary
    for student in students:
        
        # display elements of dictionary with security
        name = student.get('name', 'not found')
        score = student.get('score', 'not tested yet')
        subjects = student.get('subjects', ('no subjects are registered',))
        
        # display students's data
        print(f"student's name : {name}")
        print(f"score is : {score}")   
        print(f"subjects are : {', '.join(subjects)}")    #print(f"subjects are : {subjects}") join convert tuple to string
        
        print("-" * 30) # خط فاصل بين الطلاب
        
    print("="*40)
showRport()
    


#========================
#Task 4 : Main Menu
#========================

# declare main menu for user choice
def mainMenu():
    """main menu for system"""
    while True:
        print("="*30)
        print("main menu")
        print("="*30)
        print("1- to register students \n")
        print("2- to start quiz \n")
        print("3- to show students's report \n")
        print("4. to exit \n")
        print("-"*30)
        
        user_choice = input("enter choice from 1 to 4 : ")
        
        if user_choice == '1':
            registerStudent()
        elif user_choice == '2':
            if not students:
                print("there is not students to start quiz")
                continue
            else:
                entered_student = input("enter student to start quiz: ").strip()
                found_student = None
                for student in students:
                    if student.get('name','').lower() == entered_student.lower():
                        found_student = student
                        break
                if found_student:
                    quizQuesions(found_student)
                else:
                    print(f"student {entered_student} not found")
                    
        elif user_choice == '3':
            showRport()
        elif user_choice == '4':
            print("thanks to use system and data saved \n")
            break
        else:
            print("you choice is wrong please choice from 1 to 4: ")
            

mainMenu()
                        
                
        
                
    




