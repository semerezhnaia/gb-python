num = 0
list1 = []
for num in range(1, 1000, 2):
    num = num**3
    list1.append(num)
print(list1)

list2 = []
sum_list = 0
for i in list1:
    while i != 0:
        sum_list += i % 10
        i = i // 10
        if sum_list % 7 == 0:
            list2.append(i)
    sum_list = 0
print(sum(list2))

sum_list_2 = 0
sum_2 = 0
for i in list2:
    i += 17
    while i != 0:
        sum_2 += i % 10
        i = i // 10
        if sum_2 % 7 == 0:
            sum_list_2 += num + 17
print(sum_list_2)