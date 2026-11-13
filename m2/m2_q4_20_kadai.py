num = 5
list_a = []
while num < 7:
    for i in range(num, 25, 2):
        i -= 6
        list_a.append(i)
    num += 1
print(sum(list_a))