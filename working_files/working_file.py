fileread=open("01_test.py","rt")
text=fileread.read()
print(text)
fileread.close()
# ============================
# Напишіть програму, яка зчитує  числа з файлу numbers.txt і обчислює їх суму,
# виводить цю суму на екран і, водночас,
#  записує цю суму у інший файл під назвою sum_numbers.txt
# Відносне посилання: working_files\numbers.txt

fileread1=open("working_files\\numbers.txt")
numbers_str=fileread1.readline()
print(numbers_str)
print(type(numbers_str))
numbers_list_str=numbers_str.split()
print(numbers_list_str)
numbers_list=[int(x) for x in numbers_list_str]
print(f"suma чисел {numbers_list} => {sum(numbers_list)}")
fileread1.close()
# Абсолютний шлях: E:\Tetiana\RSHU\CT_I_2025_2026_Python\working_files
filewrite=open("working_files\sum_numbers.txt","wt")
filewrite.write(f"suma numbers {numbers_list} => {sum(numbers_list)}")
filewrite.close()