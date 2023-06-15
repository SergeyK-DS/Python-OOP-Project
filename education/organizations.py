print('Organizations module successfully imported')
import sys 
sys.path.append("education")
from users import *
list_School = ["class School", "__init__", "set_name", "set_address", "set_phone", "set_email", "set_num_stud", "set_num_teachers", "add_student", "add_teacher", "get_info", "get_report"]
if __name__ == "__main__":    
    print(list_School)
import csv
class School:
    def __init__(self, name, address, phone, email, num_stud, num_teachers):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__num_stud = num_stud
        self.__num_teachers = num_teachers
        self.list_students = []
        self.list_teachers = []
    def set_name(self, name):
        self.__name = name
        pass
    def set_address(self, address):
        self.__address = address
        pass
    def set_phone(self, phone):
        self.__phone = phone
        pass
    def set_email(self, email):
        self.__email = email
        pass
    def set_num_stud(self, num_stud):
        self.__num_stud = num_stud
        pass
    def set_num_teachers(self, num_teachers):
        self.__num_teachers = num_teachers
        pass
    def add_student(self, student):
        self.list_students.append(student)
        pass
    def add_teacher(self, teacher):
        self.list_teachers.append(teacher)
        pass
    def get_info(self):
        school_information = dict(name=self.__name, address=self.__address, phone=self.__phone, email=self.__email, num_stud=self.__num_stud, num_teachers=self.__num_teachers)
        return school_information
        pass
    def get_report(self):
        with open(f"{self.__name}.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name_school', 'address', 'phone', 'email', 'num_students', 'num_teachers'])
            school_info = self.get_info()
            writer.writerow([school_info["name"], school_info["address"], school_info["phone"], school_info["email"], school_info["num_stud"], school_info["num_teachers"]])
      
            writer.writerow(['name_student', 'familyname', 'age', 'gender', 'nationality', 'school', 'subject'])
            for student in self.list_students:
                student_info = student.get_info_student()
                writer.writerow([student_info["name"], student_info["familyname"], student_info["age"], student_info["gender"], student_info["nationality"], student_info["school"], student_info["subject"]])
            
            writer.writerow(['name_teacher', 'familyname', 'age', 'gender', 'nationality', 'school', 'subject'])
            for teacher in self.list_teachers:
                teacher_info = teacher.get_info_teacher()
                writer.writerow([teacher_info["name"], teacher_info["familyname"], teacher_info["age"], teacher_info["gender"], teacher_info["nationality"], teacher_info["school"], teacher_info["subject"]])
        pass
        
        

