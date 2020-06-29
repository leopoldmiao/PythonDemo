#coding=utf-8


def get_users_grades(sg):
    #sg = {}
    while True:
        stu = raw_input("Please give me the name of the student (q to quit):")
        if stu == "q":
            break
        gra = raw_input("Please give me their grade:")
        sg[stu] = gra
    #return sg


def print_users_grades(sg):
    students = sg.keys()
    n = 10
    print "Okay, Printing grades!"
    print "Student" + " "*n + "Grade"
    for s in students:
        if len(s)<len("Student"):
            print s + " "*(n+(len("Student")-len(s))) + sg[s]
        else:
            print s + " "*(n-(len(s)-len("Student"))) + sg[s]

def main():
    students_grades = {}
    get_users_grades(students_grades)
    #students_grades = get_users_grades(students_grades)
    #print students_grades
    print_users_grades(students_grades)

if __name__ == "__main__":
    main()