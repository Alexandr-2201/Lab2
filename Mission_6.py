def print_characters_by_type(file_name, output_file_name):
    characters = []
    order = []

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                characters.append(char)
                order.append(char)

    digits = []
    letters = []
    others = []

    for char in characters:
        if char.isdigit():
            digits.append(char)
        elif char.isalpha():
            letters.append(char)
        else:
            others.append(char)

    with open(output_file_name, 'w') as output_file:
        print("Цифры:")
        output_file.write("Цифры:\n")
        for char in order:
            if char in digits:
                print(char, end='')
                output_file.write(char)

        print("\nБуквы:")
        output_file.write("\nБуквы:\n")
        for char in order:
            if char in letters:
                print(char, end='')
                output_file.write(char)

        print("\nОстальные символы:")
        output_file.write("\nОстальные символы:\n")
        for char in order:
            if char in others:
                print(char, end='')
                output_file.write(char)

file_name = 'Файл с символами 6.txt'  # Имя вашего файла с символами
output_file_name = 'Результат работы 6.txt'  # Имя файла для записи результата
print_characters_by_type(file_name, output_file_name)