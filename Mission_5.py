from collections import deque

def check_brackets_balance(file_name):
    stack = deque()

    with open(file_name, 'r') as file:
        for line in file:
            for char in line:
                if char == '[':
                    stack.append('[')
                elif char == ']':
                    if not stack:
                        return False  # Найдена лишняя закрывающая скобка
                    stack.pop()

    return len(stack) == 0  # Проверяем, что дек пустой


file_name = 'program45.txt'  # Имя вашего файла с программой
if check_brackets_balance(file_name):
    print("Квадратные скобки сбалансированы.")
else:
    print("Квадратные скобки не сбалансированы!!!!!")