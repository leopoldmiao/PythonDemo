#coding=utf-8


class Student(object):
    name = ""
    school = ""
    grade = ""

    def __init__(self, name = "", school="", grade=""):

        self.name = self.get_correct_name(name)
        self.school = self.get_correct_school(school)
        self.grade = self.get_correct_grade(grade)


    def get_correct_name(self,name):
        correct_name = name
        if not correct_name:
            correct_name = raw_input("Please input the student's name:")
        return correct_name


    def get_correct_school(self,school):
        correct_school = school
        if not school:
            print "{}'s school is not valid!".format(self.name),
            correct_school = raw_input("Please input the student's school:")
        return correct_school


    def get_correct_grade(self,grade):
        correct_grade = grade
        while correct_grade.lower() not in ["k","1","2","3","4","5"]:
            print "{}'s grade is not valid!".format(self.name),
            correct_grade = raw_input("Please input the student's grade:[k,1-5] ")
        return correct_grade

    def print_student(self):
        print "Name: {}".format(self.name)
        print "School: {}".format(self.school)
        print "Grade: {}".format(self.grade)

def main():
    student1 = Student()
    student2 = Student("miaomiao", "haidianshiyan", "2")
    student3 = Student("wumao")
    #students = [student1,student2]
    students = [student1, student2, student3]
    print_students(students)

def print_students(students):
    print "All Students"
    print "*" * 30
    for s in students:
        s.print_student()
        print "*"*30

if __name__ == "__main__":
    main()