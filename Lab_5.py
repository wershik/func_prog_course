# 5я лаба
#1е задание
students = []
while True:
    student_info = input("Введите информацию о студенте (Имя Фамилия, Группа, Предмет): ")
    if student_info == "":
        break
    students.append(student_info)

students = [student.split(", ") for student in students]

sorted_students = sorted(students, key=lambda x: (x[0], x[1]))

for student in sorted_students:
    print(", ".join(student))

#2е задание
#Список
subjects = ['Math', 'English', 'Prog']

#Словарь
grades = {
    'Serbol': [90, 85, 95],
    'Dauren': [95, 92, 88],
    'Korkem': [80, 85, 90]
}


def get_grades(name):
    return grades.get(name, 'No grades found')

name = input('Enter student name: ')

print(get_grades(name))



#3е задание
numbers = []
while True:
    num = int(input("Введите целое число (0 для выхода): "))
    if num == 0:
        break
    numbers.append(num)

numbers.sort()
print("Отсортированный список чисел:")
for num in numbers:
    print(num)

#4е задание
numbers.sort(reverse=True)
print("Обратно отсортированный список чисел:")
for num in numbers:
    print(num)


#5е задание
import random

my_ticket = []


while len(my_ticket) < 6:
    num = random.randint(1, 49)
    if num not in my_ticket:
        my_ticket.append(num)

my_ticket.sort()
print("Мои номера лотерейного билета:", my_ticket)


# #6е задание
def is_sorted(lst):
    if lst == sorted(lst):
        return True
    elif lst == sorted(lst, reverse=True):
        return True
    else:
        return False

listic = []
while True:
    num = int(input("Введите число (0 для завершения ввода): "))
    if num == 0:
        break
    listic.append(num)


if is_sorted(listic):
    print("Список отсортирован")
else:
    print("Список не отсортирован")