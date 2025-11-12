x=[3,4,5,6,7]
print(x[4])
## print(x[5]) #IndexError: list index out of range
# try: #блок, де може виникнути помилка
#     number = int(input("Введіть число: "))
#     print("Введене число:", number)
#     print(f"{number}**2={number**2}")
# except: #перехоплення та обробка всіх винятків
#     print("Перетворення пройшло невдало")
# print("Продовження програми")


# try: #блок, де може виникнути помилка
#     number = int(input("Введіть число: "))
#     print("Введене число:", number)
#     print(f"{number}**2={number**2}")
# except ValueError as ex: #перехоплення та обробка всіх винятків
#     print("Перетворення пройшло невдало",ex)
# print("Продовження програми")

try: #блок, де може виникнути помилка
    number1 = int(input("Введіть число: "))
    number2=int(input("Введіть число: "))
    print("Введене число:", number1)
    print("Введене число:", number2)
    print(number1/number2)
except TypeError as e: #перехоплення та обробка всіх винятків
    print("невідповідність =>",e)
except ValueError as e:
    print("Перетворення прошло невдало",e)
except ZeroDivisionError:
    print(ZeroDivisionError.__doc__)
except Exception as e:
    print("Вийняток => ",e)
else:
    print("Блок коду виконався без помилок")
finally:
    print("Я виконуюсь завжди. Тут можете звільнити ресурси (закрити файл, закрити зєднання з БД )")

print("Продовження програми")

# try :   фрагмент коду, в якому може бути виянто к!!!
# except тип_виключення(помилка):: коли є виняток !!!
# else:  нема винятку
# finaly:    завжди виконується


# list1=[3,45]
# try: #блок, де може виникнути помилка
#     number1 = int(input("Введіть число: "))
#     number2 = int(input("Введіть число: "))
#     if number2==0:
#         raise Exception(f"{number1}/{number2} - ділення на нуль ")
#     print("Введене число:", number1/number2)
#     print(list1[2])
# except TypeError as e: #перехоплення та обробка всіх винятків
#     print("Перетворення прошло невдало",e)
# except ValueError as e:
#     print(e)
#     print("input int number")
# except ZeroDivisionError as e:
#     print(e.__doc__)
# except Exception as e:
#     print("name Exception: ",e)
# else:
#     print("Блок коду виконався без помилок")
# finally:
#     print("Я виконуюсь завжди. Тут можете звільнити ресурси (закрити файл, закрити зєднання з БД )")



try:
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))
    if number2 == 0:
        raise Exception("Друге число не повинне бути рівним 0")
    
except ValueError:
    print("Введено нероректні дані")
except Exception as e:
    print(e)
else:
    print("Результат ділення двох чисел:", number1 / number2)
print("Заврешення програми")