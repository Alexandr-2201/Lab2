def reverse_file(input_file, output_file):
    stack = []

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            stack.append(line.strip())

    with open(output_file, 'w') as out_file:
        while stack:
            line = stack.pop() # Извлечение последней строки из стека и присвоение её переменной line
            print(line) # Вывод строки на экран
            out_file.write(f"{line}\n") # Запись этой строки в файл вывода

# Укажите имя вашего исходного файла и файла для записи результата
input_file = 'Прямой порядок строк 8.txt'
output_file = 'Результат Обратный порядок строк 8.txt'
reverse_file(input_file, output_file)