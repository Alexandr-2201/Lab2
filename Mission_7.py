from collections import deque

def print_numbers_by_sign(file_name, out_file):
    negative_num = deque()
    positive_num = deque()

    with open(file_name, 'r') as file:
        for line in file:
            numbers = map(int, line.split())
            for num in numbers:
                if num < 0:
                    negative_num.append(num)
                else:
                    positive_num.append(num)

    with open(output_file, 'w') as out_file:
        print("Отрицательные числа:")
        out_file.write("Отрицательные числа:\n")
        while negative_num:
            neg_num = negative_num.popleft()
            out_file.write(f"{neg_num}\n")
            print(neg_num)

        out_file.write("\nПоложительные числа:\n")
        print("Положительные числа:")
        while positive_num:
            pos_num = positive_num.popleft()
            out_file.write(f"{pos_num}\n")
            print(pos_num)

file_name = 'Файл с числами 7.txt'  # Имя файла с числами
output_file = 'Результат 7.txt'  # Имя файла для записи результатов
print_numbers_by_sign(file_name, output_file)