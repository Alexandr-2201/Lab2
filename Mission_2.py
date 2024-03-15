from collections import deque

# Создаем дек с последовательностью символов для шифровки
deq = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

# Читаем зашифрованное сообщение из файла
with open('Шифр2.txt', 'r') as file:
    encrypted_message = file.read()

# Расшифровываем сообщение
decrypted_message = ''
for char in encrypted_message:
    if char.isalpha():
        index = deq.index(char)
        decrypted_char = deq[(index - 1) % len(deq)]  # Расшифровываем символ
        decrypted_message += decrypted_char
    else:
        decrypted_message += char

# Выводим расшифрованное сообщение
print(decrypted_message)

# Запись расшифрованного сообщения в файл
with open('Шпион2.txt', 'w') as file:
    file.write(decrypted_message)