students =[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])


minimum = students[0][1]
for item in students:
    if minimum > item[1]:
        minimum = item[1]

def delete_min(m,students):
    for item in students:
        if m == item[1]:
            students.remove(item)
            delete_min(m,students)

delete_min(minimum,students)

minimum = students[0][1]
for item in students:
    if minimum > item[1]:
        minimum = item[1]
names = []
for item in students:
    if minimum == item[1]:
        names.append(item[0])
names.sort()
for i in names:
    print(i)
