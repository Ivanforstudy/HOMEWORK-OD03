mas = [12, 4, 9, 1, 7, 6]
n = len(mas)
for run in range(n - 1):
    for i in range(n - 1):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)