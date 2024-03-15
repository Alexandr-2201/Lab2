from collections import deque

# Чтение данных из файла
with open('books1.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Инициализация двух деков
deq1 = deque()
deq2 = deque()

# Перемещение строк в 1-й дек
for line in lines:
    deq1.append(line.strip())

# Перемещение строк из 1-го дека во второй в алфавитном порядке
while deq1: # Выполняется до тех пор, пока deq1 не станет пустым
    smallest = min(deq1)
    deq1.remove(smallest)
    deq2.append(smallest)
    print(smallest) # Вывод отсортированного списка

# Запись отсортированных строк в файл
with open('sorted_books1.txt', 'w') as file:
    for book in deq2:
        file.write(book + '\n')

print("Отсортированные строки записаны в файл 'sorted_books.txt'.")