#Лаба 6я
import random
# Создаём картежи для 1го пункта лабы

resume_1 = ("Sergey Vershinin", 21, "Computer Science", "Java", "C++", "PHP", "JS", "Python", "SQL")
resume_2 = ("Anna Vershinina", 47, "Analise", "Exel", "Hight Math")
resume_3 = ("Alex Ivanov", 24, "Sales", "Marketing", "Finance", "Communication")
resume_4 = ("Ivan Petrov", 45, "Dooker", "CI/CD processes", "Architect", "Team Leading")

resumes = {resume_1, resume_2}
resumes_test_for_set_1 = set(resume_1)
resumes_test_for_set_2 = set(resume_3)
comm_elements = resumes_test_for_set_1.intersection(resumes_test_for_set_2)
diff_elements = resumes_test_for_set_1.symmetric_difference(resumes_test_for_set_2)
resumes.add(resume_3)
resumes.discard(resume_3)
resumes.add(resume_3)
resumes.remove(resume_3)
resumes.clear()
resumes_1 = {resume_1, resume_2, resume_3}
resumes_2 = {resume_2, resume_3, resume_4}
print(resumes_1.issubset(resumes_2))
print(resumes_2.issubset(resumes_1))
resumes_summ = resumes_1.union(resumes_2)
###############
list_data = ["Sergey", 21, "Satpaev", "data science"]
tuple_data = tuple(list_data)
print(tuple_data)
merged_resume = resume_2 + resume_3
print(resume_3[1:3])
t_ages = []
for resume in resumes_1:
    t_ages.append(resume[1])

summ_ages = sum(t_ages)/len(t_ages)
#####################

##################
#задание 2.1

def random_tuple(begin, end, size_tuple):
    return tuple(random.randint(begin, end) for _ in range(size_tuple))

tuple_1 = random_tuple(0, 5, 10)
tuple_2 = random_tuple(-5, 0, 10)
print(tuple_1)
print(tuple_2)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)
count_of_zeros = tuple_3.count(0)
print("Сколько нулей:", count_of_zeros)

#задание 2.2
matrioshka = (21, (90.8, (1+7j, ('внутренний стринг', ()))))

print(matrioshka[1][1][1][0])

#задание 2.3

trari_for_week = [
    {"day": "Monday", "Transport": 80, "Food": 1020, "Life": 0},
    {"day": "Tuesday", "Transport": 80, "Food": 560, "Life": 0},
    {"day": "Wednesday", "Transport": 0, "Food": 2900, "Life": 0},
    {"day": "Thursday", "Transport": 80, "Food": 2090, "Life": 4321},
    {"day": "Friday", "Transport": 160, "Food": 789, "Life": 1211},
    {"day": "Saturday", "Transport": 0, "Food": 1092, "Life": 3434},
    {"day": "Sunday", "Transport": 80, "Food": 5909, "Life": 7878},
]


total_summ_days = [day["Transport"] + day["Food"] + day["Life"] for day in trari_for_week]
total_summ = sum(total_summ_days)

print("total summ for week:", total_summ_days)
print("total summ for week:", total_summ)

#задание 2.4

students = tuple(input("Введиите через пробел: ").split())

names_output = ""
va = "ва"

for name in students:
    if va in name:
        names_output += name + " "


print(f"Names containing {va}: {names_output}")

#задание 2.5
alphabet = {'а': 'a', 'ә': 'a\'', 'б': 'b', 'в': 'v', 'г': 'g', 'ғ': 'g\'', 'д': 'd',
            'е': 'e', 'ё': 'e', 'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'i', 'і': 'i\'', 'к': 'k',
            'қ': 'q', 'л': 'l', 'м': 'm', 'н': 'n', 'ң': 'n\'', 'о': 'o', 'ө': 'o\'',
            'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ұ': 'ū','ү': 'ü',
            'ф': 'f', 'х': 'h', 'һ': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sh\'',
            'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


input_text = input("Введите казахский текст: ")
output_text = ""

for char in input_text:
    is_up = False
    if char.isupper():
        is_up = True
    else:
        is_up = False
    if char.lower() in alphabet:
        if char.isupper():
            output_text += alphabet[char.lower()].upper()
        else:
            output_text += alphabet[char.lower()].lower()
    else:
        output_text += char

print("Переведенный текст: ", output_text)

print("dddd")