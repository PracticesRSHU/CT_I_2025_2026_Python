class Student:
    """
    Опис класу студент
    """
    count=0
    def __init__(self,first_name="NoName",age=17):
        self.first_name=first_name #атрибути або поля  або властивості класу
        self.age=age
        Student.count+=1
        self.count=25
        print(f"Було створено екземпдяр класу Student #{Student.count}")

    def __str__(self) :
        return f"Student: {self.first_name}, {self.age} years."
    
    #методи для роботи з кожним екземпляр класу
    def print_info(self):
        print("This is class Student")


st1=Student()
st1.first_name="Тимофій"
print(st1.first_name)
print(st1.age)
print(st1)
st1.print_info()
st2=Student()
st2.first_name="Юрій"
print(st2.first_name)
print(st2.age)
print(st2)
st3=Student("Володимир",18)
print(st3.first_name)
print(st3.age)
print(st3)
st3.count=55
print("All created students:",Student.count)
print("st1",st1.count)
print("st2",st2.count)
print("st3",st3.count)
Student.count=77
print("All created students:",Student.count)
