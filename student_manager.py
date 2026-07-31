from student import Student

class StudentManager:
    
    def __init__(self):
        self.students = []

    def add_student(self):

        name = input('Enter Your Name: ').upper()

        while True:
            try:
                roll = int(input('Enter Your Roll No: '))
                if self.search_student(roll):
                    print("Roll number already exists! Please enter a different roll number.")
                    continue
                break

            except ValueError:
                print('Invalid Roll No')

        while True:
            try:
                age = int(input('Enter Your Age: '))
                break
            except ValueError:
                print('Invalid Age')

        department = input('Enter Your Department Name: ').upper()
        
        while True:
            try :
                contact = int(input('Enter Your Contact: '))
                break
            except ValueError:
                print('Invalid Contact')

        address = input('Enter Your Address: ').upper()


        subjects = [
            'Python',
            'Math',
            'Ai'
                ]
        subject_marks ={}

        for subject in subjects:
            while True:
                try: 
                    mark = int(input(f'Enter your {subject} Marks: '))
                    if mark < 0 or mark > 100:
                        print('Marks Range Between 0 to 100')
                    else:
                        subject_marks[subject]=mark
                        break
                except ValueError:
                    print('Invalid Marks')

        student = Student(name,
                          roll,
                          age,
                          department,
                          contact,
                          address,
                          subject_marks)
        self.students.append(student)
        print("Student Added Sucessfully!")



    
    def show_all_students(self):
        if not self.students:
            print('No Student Found!')
            return
        for student in self.students:
            student.show_details()



    def search_student(self,roll) :
        for student in self.students:
            if student.roll == roll:
                return student
            

        return None         
    
    def delete_student(self,roll):

        student = self.search_student(roll)

        if student is None:
            print('Student Not Found!')
            return
        
        student.show_details()
        

        while True:
            print('1. Delete Student')
            print('2. Cancel')

            while True:
                try:
                    user = int(input('Select An Option:'))
                    break
                except ValueError:
                    print('Select Valid Option!')

            if user<1 or user>2:
                print('Invalid Choice')
                continue

            elif user == 1:
                self.students.remove(student)
                print('Student Deleted Sucessfully!')
                return

            elif user == 2:
                print('Cancelled!')
                return
            

    def update_student(self, roll):

        student = self.search_student(roll)

        if student is None:
            print('Student Not Found!')
            return
        
        student.show_details()
        


    def update_student(self,roll) :
        student = self.search_student(roll)
        if student is None:
            print('Student Not Found')
            return

        student.show_details()
        while True:
            print('1. Update Name')
            print('2. Update Age')
            print('3. Update Department')
            print('4. Update Contact')
            print('5. Update Address')
            print('6. Update Subject Marks')
            print('7. Update All')
            print('8. Cancel')

            while True:
                try:
                    user = int(input('Select An Option: '))
                    break
                except ValueError:
                    print('Invalid Option')

            if user<1 or user>8:
                print('Invalid Option')
                continue

            elif user == 1:
                student.name = input('Update Name: ').upper()

            elif user == 2:
                while True:
                    try:
                        age = int(input('Update Age: '))

                        if age <=0 :
                            print('Age Must Be Positive!')
                            continue
                        student.age = age
                        break
                        
                    except ValueError:
                        print('Invalid Age')

            elif user == 3:
                student.department = input('Update Department: ').upper()

            elif user == 4:
                while True:
                    try:
                        student.contact = int(input('Update Contact: '))
                        break
                    except ValueError:
                        print('Invalid COntact')

            elif user == 5:

                student.address = input('Update Address: ').upper()

            elif user==6:
                subjects = list(student.subject_marks.keys())

                for index, subject in enumerate(subjects, start=1):
                    print(f'{index}. {subject}')

                while True:
                    try:
                        choice = int(input('Select An Option: '))
                        
                    except ValueError:
                        print('Invalid choice!')
                        continue

                    if choice <1 or choice >len(subjects):
                        print('Invalid choice')
                        continue
                    break

                selected_subject = subjects[choice - 1]
                while True:
                    try:
                        new_mark = int(input(f'Enter New Marks For {selected_subject}: '))
                        if new_mark < 0 or new_mark > 100 :
                            print('Invalid! Marks Must Be Btween 0 to 100 ')
                            continue
                        student.subject_marks[selected_subject]= new_mark
                        break
                    except ValueError:
                        print('Invalid Marks!')



            elif user == 7:
                student.name = input('Update Name: ').upper()


                while True:
                    try:
                        age = int(input('Update Age: '))
                        if age <=0:
                            print('Age Must Be Positive!')
                            continue
                        student.age=age
                        break
                    except ValueError:
                        print('Invalid Age')
                
                student.department = input('Update Department: ').upper()


                while True:
                    try:
                        student.contact = int(input('Update Contact: '))
                        break
                    except ValueError:
                        print('Invalid COntact')


                student.address = input('Update Address: ').upper()
                
                subjects = list(student.subject_marks.keys())
                for subject in subjects:
                    while True:
                        try:
                            new_mark = int(input(f'Update New Marks For {subject}: '))
                            if new_mark < 0 or new_mark > 100 :
                                print('Invalid! Marks Must Be Btween 0 to 100 ')
                                continue
                            student.subject_marks[subject]= new_mark
                            break
                        except ValueError:
                            print('Invalid Marks!')
                    

                

            elif user == 8:
                print('Update cancelled!')
                return


            print('Updated sucessfully!')
            print()
            return

    def save_students(self):
        with open('isbm.txt','w') as file:
            for student in self.students:
                line =(f'{student.name},'
                       f'{student.roll},'
                       f'{student.age},'
                       f'{student.department},'
                       f'{student.contact},'
                       f'{student.address}')
                for mark in student.subject_marks.values():
                    line += f",{mark}"

                file.write(line +'\n')
                print('Student Saved sucessfully!')

    def load_student(self):
        try :
            with open('isbm.txt','r') as file:
                self.students.clear()
                for line in file:
                    parts = line.strip().split(',')

                    subject_marks ={
                        'python':int(parts[6]),
                        'Maths':int(parts[7]),
                        'Ai':int(parts[8])
                    }

                    student = Student(parts[0],int(parts[1]),int(parts[2]),
                                      parts[3],int(parts[4]),parts[5],subject_marks)
                    self.students.append(student)
                if not self.students:
                    print('Student not found!')
                else:
                    
                    print('Student Loaded Sucessfully!')
                    student.show_details()

        except FileNotFoundError:
            print('No saved records found. Please add students and save them first.')