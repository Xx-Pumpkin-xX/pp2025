student = []
course = []
mark = {}

def set_number_of_student():
    count = int(input("Enter the number of student in the class: "))
    return count
def set_student_info():
    count = set_number_of_student()
    for i in range (count):
        s_name = input(f"Name of student {i+1}: ")
        s_id = input(f"Id of student {i+1}: ")
        DoB = input(f"DoB of student {i+1}: ")
        student.append({"name" : s_name, "id" : s_id, "DoB" : DoB})
def set_number_of_course():
    count = int(input("Enter the number of course: "))
    return count
def set_course_info():
    count = set_number_of_course()
    for i in range (count):
        c_name = input(f"Name of course {i+1}: ")
        c_id = input(f"ID of course {i+1}: ")
        course.append({"name" : c_name, "id" : c_id})
        mark[c_id] = {}
def set_mark():
    if not course:
        print("No course avaiable")
        return
    for c in course:
        print(f"Available courses: {c['name']} (ID: {c['id']})")
    selected_id = input("Enter course ID to get mark: ")
    if selected_id in mark:
        for s in student:
            score = float(input(f"Enter mark for {s['name']} (ID {s['id']}): "))
            mark[selected_id][s['id']] = score
    else:
        print("Invalid Course ID")
def get_student():
    print("")
    print("-----Student list-----")
    for s in student:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['DoB']}")
def get_mark():
    print("")
    print("-----Showing Mark-----")
    for c in course:
        print(f"Available courses: {c['name']} (ID: {c['id']})")
    c_id = input("Enter the Course ID: ")
    if c_id in mark:
        print(f"Mark for {c['name']}: ")
        for s in student:
            score = mark[c_id].get(s['id'], "N/A")
            print(f"{s['name']}: {score}")
    else:
        print("Course not found")
def main():
    while True:
        print("\n1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. List Students")
        print("5. Show Marks")
        print("0. Exit")
        
        user = input()
        
        if user == '1':
            print("-----Setting student info: -----")
            set_student_info()
        elif user == '2':
            print("-----Setting course info: ------")
            set_course_info()
        elif user == '3':
            print("-----Setting mark for student: -----")
            set_mark()
        elif user == '4':
            print("-----Listing all student: -----")
            get_student()
        elif user == '5':
            print("-----Showing all student info: -----")
            get_mark()
        elif user == '0':
            break
main()