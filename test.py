# Вводим данные о студенте
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
is_student = input("Вы студент? (Да/Нет): ").lower() == "да"

# Выводим информацию о студенте с помощью условных операторов
print("Имя студента:", name)
if age < 18:
    print("Студент несовершеннолетний.")
else:
    print("Студент совершеннолетний.")
if is_student:
    print("Студент учится в вузе.")
else:
    print("Студент не учится в вузе.")