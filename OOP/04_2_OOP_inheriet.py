"""
Принципи ООП:
    інкапсуляція
    наслідування !!!!!!! inheriet
    поліморфізм
"""

class Person:
    def __init__(self, first_name, second_name, age) -> None:
        self.__first_name=first_name #атрибути або поля  або властивості класу ТУТ ПРИВАТНІ
        self.__second_name=second_name #атрибути або поля  або властивості класу ТУТ ПРИВАТНІ
        self.__age=age
        self.test="23SERIYA"

    def __str__(self):
        return f"Info person: {self.__first_name} {self.__second_name}, {self.__age} years old."
    
    # getters
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def second_name(self):
        return self.__second_name
    
    @property
    def age(self):
        return self.__first_name
    
    # setters
    # .....

    def info_class(self):
        print("This method from class Person!!!!")
    

#worker
class Employer():
    def __init__(self, work_place,salary):
        self.__work_place=work_place
        self.__salary=salary

    def __str__(self):
        return f"Employer working in {self.__work_place} and has salary {self.__salary} $"
    
    @property
    def work_place(self):
        return self.__work_place
    

    @property
    def salary(self):
        return self.__salary

    def print_info_employer(self):
        return self.__str__()
    



class Student(Person):
    """
    Опис класу студент
    """
    def __init__(self, first_name, second_name, age, univer="RSHU", marks=[]) -> None:
        super().__init__(first_name, second_name, age)
        self.__univer=univer
        self.__marks=marks

    def __str__(self):
        return super().__str__()+f"\nShe(he) learning in university {self.__univer}"
    
    def progress_learn(self):
        text=f"{super().second_name} {super().first_name}:\n"
        for mark in self.__marks:
            text+=str(mark)+"; "

        text+="\n"
        print(text)

    # getters
    @property
    def univer(self):
        return self.__univer
    
    @univer.setter
    def univer(self,univer):
        self.__univer=univer

    @property
    def marks(self):
        return self.__marks
    
    @univer.setter
    def marks(self,marks):
        self.__marks=marks

    def info_class(self):
        print("This method from class Student!!!!")

    def print_info_student(self):
        return self.__str__()
    



class WorkerStudent(Student,Employer):
    def __init__(self, first_name, second_name, age, work_place,salary, univer="RSHU", marks=[]) -> None:
        Student.__init__(self, first_name, second_name, age, univer, marks=[])
        Employer.__init__(self,work_place,salary)

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.work_place} {self.salary} EUR"
    




# ==========================
if __name__=="__main__":
    person=Person("Siry","Intelect",2)
    print(person)
    person.info_class()
    print("*"*30)
    student=Student("Yriy","Romanjuk",18)
    print(student)
    student.marks=[2,3,4,5]
    student.progress_learn()

    print("*"*30)
    print(student.first_name, student.test)
    student.info_class()
    print("*"*30)
    student_worker=WorkerStudent("Olga","Borovotec",22,"IT STEP",2000)
    print(student_worker)
    


