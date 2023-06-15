print('Users module successfully imported')
list_Human = ["class Human", "__init__,", "set_name,", "set_family,", "set_age,", "set_gender,", "set_nationality,", "get_info"]
list_Student = ["class Student", "__init__,", "set_school,", "add_subject", "get_info_student"]
list_Teacher = ["class Teacher", "__init__,", "set_school,", "add_subject", "get_info_teacher"]
if __name__ == "__main__":
    print(list_Human)
    print(list_Student)
    print(list_Teacher)
secret = 'It is a secret phrase'
class Human:
    def __init__(self, name, familyname, age, gender, nationality):
        self.__name = name
        self.__familyname = familyname
        self.__age = age
        self.__gender = gender
        self.__nationality = nationality
    def set_name(self, name):
        self.__name = name
        pass
    def get_name(self):
        return self.__name
        pass
    def set_family(self, familyname):
        self.__familyname = familyname
        pass
    def get_family(self):
        return self.__familyname
        pass
    def set_age(self, age):
        self.__age = age
        pass
    def get_age(self):
        return self.__age
        pass
    def set_gender(self, gender):
        self.__gender = gender
        pass
    def get_gender(self):
        return self.__gender
        pass
    def set_nationality(self, nationality):
        self.__nationality = nationality
        pass
    def get_nationality(self):
        return self.__nationality
        pass
    def get_info(self):
        personal_info = dict(name = self.get_name(), familyname = self.get_family(), age = self.get_age(), gender = self.get_gender(), nationality = self.get_nationality())
        return personal_info
        pass
class Student(Human):
    def __init__(self, name, familyname, age, gender, nationality, school, subject):
        super().__init__(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality)
        self.__school = school
        self.__subject = subject
        self.subject_list = [self.__subject]
    def set_school(self, school):
        self.__school = school
        pass
    def get_school(self):
        return self.__school
        pass
    def add_subject(self, subject_name):
        self.subject_list.append(subject_name)
        pass
    def get_info_student(self):
        personal_info = dict(name = self.get_name(), familyname = self.get_family(), age = self.get_age(), gender = self.get_gender(), nationality = self.get_nationality(), school = self.get_school(), subject = self.subject_list)
        return personal_info
class Teacher(Human):
    def __init__(self, name, familyname, age, gender, nationality, school, subject):
        super().__init__(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality)
        self.__school = school
        self.__subject = subject
        self.subject_list = [self.__subject]
    def set_school(self, school):
        self.__school = school
        pass
    def get_school(self):
        return self.__school
        pass
    def add_subject(self, subject_name):
        self.subject_list.append(subject_name)
        pass
    def get_info_teacher(self):
        personal_info = dict(name = self.get_name(), familyname = self.get_family(), age = self.get_age(), gender = self.get_gender(), nationality = self.get_nationality(), school = self.get_school(), subject = self.subject_list)
        return personal_info