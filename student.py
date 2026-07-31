class Student:
    def __init__(self,name,roll,age,department,contact,address,subject_marks):
        self.name = name
        self.roll = roll
        self.age = age
        self.department = department
        self.contact = contact
        self.address = address
        self.subject_marks = subject_marks

    def show_details(self):
        
        print('='*40,'\n','Students Details','\n','='*40)

        print(f'Name: {self.name}')
        print(f'Roll No: {self.roll}')
        print(f'Age: {self.age}')
        print(f'Department: {self.department}')
        print(f'Contact: {self.contact}')
        print(f'Address: {self.address}')
        print('\n','Subject Marks')

        for subject, marks in self.subject_marks.items():
            print(subject,':',marks)

