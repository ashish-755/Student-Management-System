from student import Student
from student_manager import StudentManager

manager = StudentManager()
manager.load_student()

while True:
    print('='*10,'STUDENT MANAGEMENT SYSTEM','='*10,'\n')
    print('1. Add Student')
    print('2. Show All Student')
    print('3. Search Student')
    print('4. Update Student')
    print('5. Delete Student')
    print('6. Save Student')
    print('7. Load Student')
    print('8. Exit')

    while True:
        try:
            user = int(input('Select an Option: '))
            break
        except ValueError:
            print('invalid option')
    if user <1 or user>8 :
        print('Invalid Option')
        continue

    elif user == 1:
       manager.add_student()
        
        
    elif user == 2:
        manager.show_all_students()
    elif user== 3:
        roll  = int(input('Enter Your Roll: '))
        student=manager.search_student(roll)
        if student is not None:
            print('Student Found!')
            student.show_details()

        else:
            print('No Studet Found')
       
    elif user == 4:
        while True:
            try:
                roll  = int(input('Enter Your Roll: '))
                manager.update_student(roll)
                break
            except ValueError:
                print('Invalid Roll No')



    elif user==5:
        while True:
            try:
                roll  = int(input('Enter Your Roll: '))
                manager.delete_student(roll)
                break
            except ValueError:
                print('Invalid Roll No')
        
        

    elif user== 6:
        manager.save_students()

    elif user==7:
        manager.load_student()

    elif user == 8:
        print("Goodbye!")
        break