import random
from students import group_list

interations = random.randint(1, 21)

print(f"Було обрано {interations} студентів:")

for step in range (1, interations+1):
    random_student = random.choice(group_list)
    print(step, random_student)

number_of_students = random.randint(1, 21)
random_students = random.choices(group_list, k=number_of_students)
print(f"Було обрано {number_of_students} студентів:", random_students)