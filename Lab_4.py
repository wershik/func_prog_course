# уже не пусто

# 1е задание
text = "hello, world!"

print("Длина строки:", len(text))

print("Строка в верхнем регистре:", text.upper())

print("Строка в нижнем регистре:", text.lower())

print("Количество символов 'o':", text.count('o'))

print("Индекс первого вхождения 'o':", text.find('o'))

print("Замена 'World' на 'Python':", text.replace('World', 'Python'))

print("Разделение строки на слова:", text.split(','))

print("Состоит ли строка только из букв:", text.isalpha())

print("Состоит ли строка только из цифр:", text.isnumeric())
#+5
print("Слияние:", text.join(text))
print("2:", text.upper())
print("3:", text.islower())
print("4:", text.title())
print("5:", text.capitalize())


words = ['Hello', 'World']
print("Объединение слов в строку:", ' '.join(words))


# 2е задание
#сортировка

def my_sort(students):
    for i in student:
        for j in i:
            tmp = j
    return tmp

students = []

n = int(input("Введите количество учеников: "))

for i in range(n):
    name = input("Введите фамилию ученика: ")
    grade = int(input("Введите класс ученика: "))
    students.append((name, grade))

students.sort(key=lambda x: x[1])

print("Список учеников, отсортированный по возрастанию классов:")
for student in students:
    print(student[0], "%g класс" % student[1])


#3е задание - 1я подзадача
text = "HeLLo WoRLd"

count_upper = 0
count_lower = 0

for cymbol in text:
    if cymbol.isupper():
        count_upper += 1
    elif cymbol.islower():
        count_lower += 1


if count_lower >= count_upper:
    text = text.lower()

else:
    text = text.upper()

print(text)

#3е задание - 2я подзадача
while True:
    A = input("Введите первое число: ")
    B = input("Введите второе число: ")

    if A.isdigit() and B.isdigit():
        A = int(A)
        B = int(B)
        print("Сумма:", A + B)
        break
    else:
        print("Ошибка! Введите.")
    
