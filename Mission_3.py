def move_disk(source, target, source_name, target_name):
    disk = source.pop() # Удаление последнего элемента из стержня source и запись его в переменную disk
    target.append(disk) # Запись disk в конец стержня target
    output = f"Переместить диск {disk} с {source_name}: {source} на {target_name}: {target}"
    print(output)
    with open('output3.txt', 'a') as output_file:  # Открываем файл для добавления результатов
        output_file.write(f"{output}\n")  # Записываем содержимое строки в файл

def hanoi_with_stacks(n, source, target, auxiliary, source_name, target_name, auxiliary_name):
    if n == 1:
        move_disk(source, target, source_name, target_name)
        return
    hanoi_with_stacks(n-1, source, auxiliary, target, source_name, auxiliary_name, target_name)
    move_disk(source, target, source_name, target_name)
    hanoi_with_stacks(n-1, auxiliary, target, source, auxiliary_name, target_name, source_name)

# Чтение информации о дисках из исходного файла
with open('disks.txt', 'r') as file:
    disks = [int(line.strip()) for line in file]

# Очистить файл вывода
with open('output3.txt', 'w') as file:
    file.write('')

# Создание трех стеков для стержней А, В, С
stack_a = disks[::-1]  # Изначально все диски на стержне А
stack_b = [] # Промежуточный стержень B
stack_c = [] # Итоговый стержень C

# Вызов функции для перемещения дисков
hanoi_with_stacks(len(disks), stack_a, stack_c, stack_b, 'A', 'C', 'B')