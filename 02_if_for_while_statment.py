# # # if value:
# # #     commands
# # # else:
# # #     commands

# # # if value1:
# # #     commands
# # # elif value2:
# # #     commands
# # # else:
# # #     commands

# # # # #> < >= <= != is  and or not
# # # # # predicate , logic value


if "Python": #true
    print("Commands for true")
else:
    print("Commands for false")


if not None: #  23, "str", 2>1 =>  true
    print("Commands for true")
else:
    print("Commands for false")


a=6
b=67
print(type(b))
print(b.bit_length()) #1000011
print(bin(b))
print(oct(b))
print(hex(b))
c=complex(3,4)
print(c)
d=int("789")
print(d,"=>",type(d),sep=";")
print(f'Використання f-рядка: {d:=^11d} => {type(d)}!!!')
a=4.567
b=-75656
str_result="Expretions: {}/{}={:12.2f}".format(a,b,a*b)
print(str_result)
str_result="Expretions: {1}*{0}={2:*^11.4f}!".format(a,b,a/b)
print(str_result)

# # if a>b:
# #     max=a
# # else:
# #     max=b
# # print("max=",max,sep="",end="; ")
# # print(max,"**2=",max**2, sep="")
# # text=f"{max}**2={max**2}"
# # print(text)
# # print(f'max={max}')
# # text2="max={:d}".format(max)
# # print(text2)

# # # # # operand1 if value else operand2
# # max=a if a>b else b #ternarniy
# # print(f'max={max}')

# # day_of_week=int(input("Input number day of week: "))
# # if day_of_week>=1 and day_of_week<=5:  #[1;5]
# #     print("working day")
# # elif day_of_week==6 or day_of_week==7:
# #     print("weekend")
# # else:
# #     print("Error")

# # # match
# # match day_of_week:
# #     # pattern1
# #     case 1|2|3|4|5:
# #         print("working day")
# #     # pattern2
# #     case 6|7:
# #         print("weekend")
# #     # default pattern
# #     case _: #alternativ varaiable
# #         print("Error")

# # step1="Вмокнув пензлика в банку з фарбою"
# # step2="Провів вгору і вниз пензликом"
# # step3="Пересунув банку з фарбою вправо"
# # step4="Зробив крок вправо"

# import random
# # shtaheta_break=random.randint(1,10)

# # elemenets=10 #штахети
# # count=1
# # while count<=elemenets:
# #     print("="*10,count,"="*10)
# #     if count==3 or count==7:
# #         print("Я змахлював... не пофарбував штахету №", count)
# #         count+=1
# #         continue
# #     if count==shtaheta_break:
# #         print("Я пішов на перерву...")
# #         break
# #     print(step1)
# #     print(step2)
# #     print(step3)
# #     count=count+1
# #     print(step4+" до штахети №", count)
# # else:
# #     print(f"Stop!!! А штахети №{count} нема!")

# # print(f"Було пофарбовано {count-1} штахет")




# # # # """
# # # # for змінна in послідовність:
# # # #     команди
# # # # """

# # # # """
# # # # for змінна in послідовність:
# # # #     команди
# # # # else:                     
# # # #     команди
# # # # """

# # # # # range(10) => [0,1,2,...,9]
# # print(list(range(1,11)))
# shtaheta_break=random.randint(1,11)

# elemenets=10 #штахети
# for count in range(1,elemenets+1):
#     print("="*10,count,"="*10)
#     if count==3 or count==7:
#         print("Я змахлював... не пофарбував штахету №", count)
#         continue
#     if count==shtaheta_break:
#         print("Я пішов на перерву...")
#         break
#     print(step1)
#     print(step2)
#     print(step3)
#     print(step4+" до штахети №", count)
# else:
#     print(f"Stop!!! А штахети №{count} нема!")

# # print(f"Було пофарбовано {count-1} штахет")


suma=0 #0+1+...+9
print(type(suma))
for i in range(10):
    suma+=i
    print(i,end="\t")

print("\n",suma)

# suma=0 #0+1+2+...+10
# print(type(suma))
# for i in range(11): #range(1,11,1)
#     suma+=i
#     print(i,end="\t")

# print("\n",suma)

# print(list(range(4,10,2))) #[4, 6, 8]

# # """
# # while умова(предикат):
# #     команди (ітерації)
# # else:
# #     команди (успішний цикл без break)
# # """
# #Знайти суму 1,2,3, ..., 10
# suma=0 
# i=1
# while i<11:
#     suma=suma+i
#     print(i,end="\t")
#     i+=1
# else:
#     print("\nGood finish!")

# print(f"\nsuma={suma}")

# #Знайти суму 1,2,3, ..., 10
# suma=0 
# i=1
# while True:
#     if i>10:
#         break
#     suma=suma+i
#     print(i,end="\t")
#     i+=1
# else:
#     print("Good finish!") # never working


# print(f"\nsuma={suma}")

# # """
# # 1. Вмочив пензлик у фарбу 
# # 2. Пофарбував штахету #i
# # 3. Крок вправо на одну штахету
# # ... допоки не закінчаться штахети в паркані
# # паркан складається з 20 штахет
# # """

# # for item in range(20):
# #     if item==10: 
# #         print("Break.....")
# #         break
# #     working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(item+1)
# #     print(working)
# # else:
# #     print("Work done!!!") #not break cicle

# # # Том Соєр вирішив фарбувати кожну другу штахету
# # for item in range(20): #0,1,2,3..,19
# #     if item%2==1: 
# #         print("Continue item #",item+1)
# #         continue
# #     if item==10: 
# #         print("Break.....")
# #         break
# #     working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(item+1)
# #     print(working)
# # else:
# #     print("Work done!!!") #not break cicle

# # for item in range(1,21): #1,2,3..,20
# #     if item%2==1: 
# #         print("Continue item #",item)
# #         continue
# #     if item==10: 
# #         print("Break.....")
# #         break
# #     working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(item)
# #     print(working)
# # else:
# #     print("Work done!!!") #not break cicle


# # # break continue
# # # while
# # print("Working with while...")
# # cout_shtaheta=20
# # all_shtahet=20
# # while cout_shtaheta<all_shtahet:
# #     cout_shtaheta+=1 
# #     # cout_shtaheta=cout_shtaheta+1
# #     working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(cout_shtaheta+1)
# #     print(working)
# # else:
# #     print("Work done!!!") #not break cicle