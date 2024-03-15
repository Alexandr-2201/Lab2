def check_brackets_balance(file_path):
    stack = []

    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char == '(':
                    stack.append('(')
                elif char == ')':
                    if not stack:  # Если стек пустой, а закрывающая скобка встретилась
                        return False
                    stack.pop()

    return len(stack) == 0

file_path = 'program45.txt'  # Путь к файлу с программой
if check_brackets_balance(file_path):
    print("Круглые скобки сбалансированы.")
else:
    print("Круглые скобки не сбалансированы!!!!")