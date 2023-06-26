### Project Description
This project involves creating at least 2-3 schools, each with a minimum of 10 students (with different information), as well as at least 2 teachers of different subjects and their personal information. **The personal information of these students, teachers, and schools should not be true.**
   - The files School_N9.csv, School_N10.csv, School_N19.csv are the final results of the project.
### Project Contents:

### The **education** package, which includes the following modules:
  - users;
  - organizations.

### Running the Package
When running the package directly, all the modules specified in the package will be displayed.

### Description of the Modules is provided below:
The **users** module should contain the following classes: **Human, Student (Human), Teacher (Human).**

### 1. The **Human** class should contain the following information: name, family name, age, gender, nationality, and methods for setting this information.
  - h1 = Human(name="John", familyname="Wick", age=35, gender="male", nationality="USA")
List of methods:
    - set_name()
    - set_family()
    - set_age()
    - set_gender()
    - set_nationality()
    - get_info() # returns a dictionary with personal information about the object

### 2. The **Student** class - a child class of the Human class. It should contain the following information about each student: name, family name, age, gender, nationality, name of the school or university, a list of subjects, and corresponding methods to set this information.
List of methods in addition to the methods from the parent Human class:
  - set_school()
  - add_subject() # add a subject to the list of subjects

### 3. The **Teacher** class - a child class of the Human class. It should contain the following information about each teacher: name, family name, age, gender, nationality, name of the school or university, subject taught, and corresponding methods to set this information.
List of methods in addition to the methods from the parent Human class:
  - set_school()
  - add_subject() # add a subject taught by the teacher

**When running the users module directly, the list of classes and the lists of methods of the respective classes mentioned in the module should be displayed.
When you import the module, it should indicate that the module was successfully imported.**

### The **organizations** module should contain the **School** class.

The **School** class should contain the following information: the name or number of the school, the school's address, the school's phone number, the school's email address, the number of students, the number of teachers, and methods for setting this information.
- s1 = School(name="NIS", address="Astana, Kazakhstan", phone="999999", num_stud=1000, num_teachers=50)
List of methods:
  - set_name()
  - set_address()
  - set_phone()
  - set_email()
  - set_num_stud()
  - set_num_teachers()
  - add_student()
  - add_teacher()
  - get_info() # returns a dictionary with information about the school without personal information of students/teachers
  - get_report() # creates a report (CSV file) with information about the school and each student, as well as the teacher in that school.
---
**You need to create the correct CSV file format (which will be the most understandable).**
**When running the organizations module directly, the list of classes and the lists of methods of the respective classes mentioned in the module should be displayed.**
### When importing the module, it should indicate that the module was successfully imported.
