"""
Принципи ООП:
    інкапсуляція!!!!!!!!!
    наслідування
    поліморфізм
"""

class Student:
    """
    Опис класу студент
    """
    count=0
    def __init__(self,first_name="NoName",age=17):
        self.__first_name=first_name #атрибути або поля  або властивості класу ТУТ ПРИВАТНІ
        self.__age=age
        Student.count+=1
        # self.count=25
        print(f"Було створено екземпдяр класу Student #{Student.count}")

    def __str__(self) :
        return f"Student: {self.__first_name}, {self.__age} years."
    
    #методи для роботи з кожним екземпляр класу
    def print_info(self):
        print("This is class Student")

    #getters and setters
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self, first_name:str):
        if first_name.isalpha():
            self.__first_name=first_name

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>=14:
            self.__age=age


st1=Student("Kate", 19)
print(st1)
st2=Student("Nike", 16)
print(st2)

st1.age=-5 # зовні додане атрибут лише для екземпляра
print(st1)
print(st1.age)
# print(st2.age) #error

# st1._age=-2
# print(st1._age)

#ПРИХОВАНО ВЛАСТИВОСТІ, ДОСТУП ДО ЗМІНИ ДАНИХ НА ПРЯМУ ЗАКРИТУ
# print(st1.__first_name) #ERROR 'Student' object has no attribute '__first_name'.
# st1.__first_name="Nicka" # not changed attr but added new attribute (property)
# print(st1.__age)        #ERROR 'Student' object has no attribute '__age'.
# st1.__age=33            # not changed attr but added new attribute (property)
# print(st1)

print("Student name:",st1.get_first_name(),",", st1.get_age(),"years old")
print(st1)
st1.set_first_name("Катерина")
print(st1)
st1.set_first_name("Катерина007")
print(st1)
st1.set_age(10)
print(st1)
st1.set_age(17)
print(st1.get_age())