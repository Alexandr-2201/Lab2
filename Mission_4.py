def check_brackets_balance(file_path):
    stack = []
    opening_brackets = "("  # Открывающие скобки
    closing_brackets = ")"  # Закрывающие скобки

    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char in opening_brackets:
                    stack.append(char)
                elif char in closing_brackets:
                    if not stack:  # Если стек пустой, а закрывающая скобка встретилась
                        return False
                    if opening_brackets.index(stack[-1]) == closing_brackets.index(char):
                        stack.pop()
                    else:
                        return False

    return len(stack) == 0

file_path = 'program4.txt'  # Путь к файлу с программой
if check_brackets_balance(file_path):
    print("Скобки сбалансированы")
else:
    print("Скобки не сбалансированы!!!!")