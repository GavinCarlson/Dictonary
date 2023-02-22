#Dictonary thing

Names = {'Steve': 99, 'Larry': 78, 'Gavin': 0, 'joe': 45, 'iguana': 88}
print(Names)
Names['Sam'] = 78
Names['Marrie'] = 92
Names['Ria'] = 88
print(len(Names))

num_students = len(Names)


total_score = sum(Names.values())
mean = total_score / num_students
print(mean)

num_avg_student = 0
for score in Names.values():
    if score > mean:
        num_avg_student += 1
print(num_avg_student)

Names['Sam'] = 95

print(Names['Sam'])