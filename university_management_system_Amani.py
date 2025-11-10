
# import all namespaces needed
from abc import ABC , abstractmethod

# define Abstract person class
class Person(ABC):
    def __init__(self, name , age  , email):
        self.person_name = name 
        self.person_age = age
        self.person_email= email
     
    @abstractmethod   
    def display_info(self):
        print(f"the name of : {self.person_name} \n")
        print(f"the age of : {self.person_age} \n")
        print(f"the email is : {self.person_email} \n")
        
# defin Student class 
class Student(Person):
    def __init__(self, name, age, email ,student_id , major , gpa):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
    
    # declare getter and setter of gpa private variable 
    @property
    def gpa(self):
        """this property to return gpa variable value (getter)"""
        return self.__gpa
    
    @gpa.setter
    def gpa(self , new_gpa):
        """to check the validate of entered gpa"""
        if new_gpa <= 0 :
            raise ValueError("the value of gpa not acceptable")
        self.__gpa = new_gpa
            

   # overide display info        
    def display_info(self):
         super().display_info()
         print(f"ident of student is: {self.student_id} \n")
         print(f"the major of students is: {self.major}")
         print(f"the gpa of students is: {self.__gpa}")
         
# define Professor  class
class Professor(Person):
    def __init__(self, name, age, email , department , salary):
        super().__init__(name, age, email)
        self.department_name = department
        self.salary = salary  # here call of salary setter not variable __salary
        
    @property
    def salary(self):
        """this property for salary variable"""
        return self.__salary
    
    @salary.setter
    def salary(self , new_salary):
        if new_salary <= 0 :
             raise ValueError("salary must be more than 0")
        self.__salary = new_salary
        
    def display_info(self):
         super().display_info()
         print(f"department of student is: {self.department_name} \n")
         print(f"the salary of students is: {self.__salary} \n")
        
         
        
# define University class
class University():
    def __init__(self , name):
        self.name = name
        self.students = []
        self.professors = []
        
    
    # define add_student function
    def add_student(self , student):
        """to add student object of student"""
        if student:
            self.students.append(student)
        else:
            print("there is not student to add  ")   
        
        
    def add_professor(self , professor):
        """to add professor obect of professor"""
        if professor:
            self.professors.append(professor)
        else:
            print("there is not professor to add")
    
    
    def ahow_all_people(self):
        """to display all info of all object"""
        
        # first dispaly name of university
        print(f" \n the name of university is: {self.name} \n")
        
        #display all students data
        print("== الطلاب ==")
        for s in self.students:
            s.display_info()
            print("-"*30)
        
        # display all professor  data
        print("== الاساتذة ==")
        for p in self.professors:
            p.display_info()
            print("-"*30)
            

# use of class student and professor
s1 = Student("amani", 22 , "amani@gmail" , "s12" , "CS" , 77)
p1 = Professor("ali" , 25 , "ali@gmail" , "CS" , 0) 

uni1 = University("sana university")

uni1.add_student(s1)
uni1.add_professor(p1)
uni1.ahow_all_people()

        
    
        
    
        
        
    
