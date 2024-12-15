class person:
    def __init__(self, name, yob,):
        self.__name = name
        self.__yob = yob
    def display(self):
        print(f'Name: {self.__name} - Yob: {self.__yob}')

class student(person):
    def __init__(self, name, yob, grade ):
        super().__init__(name, yob)
        self.__name = name
        self.__yob = yob

        self.__grade = grade
    
    def display(self):
        print(f'Grade: {self.__grade}',end=" ")
        super().display()
class teacher(person):
    def __init__(self, name, yob,subject):
        super().__init__(name, yob)
        self.__name = name
        self.__yob = yob

        self.__subject = subject

    def display(self):
        print(f'Subject: {self.__subject}',end=" ")
        super().display()
class doctor(person):
    def __init__(self, name, yob,specialist):
        super().__init__(name, yob)
        self.__name = name
        self.__yob = yob

        self.__specialist = specialist

    def display(self):
        print(f'Specialist: {self.__specialist}', end=" ")
        super().display()

doctor1 = doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
student1 = student(name="studentA", yob=2010, grade="7")
teacher1 = teacher(name="teacherA", yob=1969, subject="Math")

class ward:
    
    def __init__(self, ward_name):
        self.__ward_name = ward_name
        self.a = []
    def addPerson(self, person):
        self.a.append(person)
    def display(self):
        print(self.__ward_name)
        for n in self.a:
            n.display()
        

teacher2 = teacher(name="teacherB", yob=1995, subject="History")
doctor2 = doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = ward(ward_name="Ward1")
ward1.addPerson(student1)
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1)
ward1 . addPerson(doctor2)
ward1.display()

