def move_disk(source, target):
    disk = source.pop()
    target.append(disk)
    print(f"Переместить диск {disk} с {source} на {target}")

def hanoi_with_stacks(n, source, target, auxiliary):
    if n == 1:
        move_disk(source, target)
        return
    hanoi_with_stacks(n-1, source, auxiliary, target)
    move_disk(source, target)
    hanoi_with_stacks(n-1, auxiliary, target, source)

# Чтение информации о дисках из исходного файла
with open('disks.txt', 'r') as file:
    disks = [int(line.strip()) for line in file]

# Создание трех стеков для стержней А, В, С
stack_a = disks[::-1]  # Изначально все диски на стержне А
stack_b = []
stack_c = []

# Вызов функции для перемещения дисков
hanoi_with_stacks(len(disks), stack_a, stack_c, stack_b)