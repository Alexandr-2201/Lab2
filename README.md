Работу выполнил студент группы БСТ 2201 Попов Александр

Задание:
Разработать программу обработки данных, содержащихся в заранее подготовленном txt-файле, в соответствии с заданиями, применив указанную в задании структуру данных. Результат работы
программы вывести на экран и сохранить в отдельном txt-файле.

Задание №1
Отсортировать строки файла, содержащие названия книг, в алфавитном порядке с использованием двух деков.
Исходный файл:
-----------------------------
Бедные люди
Униженные и оскорблённые
Преступление и наказание
Игрок
Идиот
Бесы
Подросток
Братья Карамазовы
----------------------------

Результат:
----------------------------
Бедные люди
Бесы
Братья Карамазовы
Игрок
Идиот
Подросток
Преступление и наказание
Униженные и оскорблённые
----------------------------


Задание №2
Дек содержит последовательность символов для шифровки сообщений. Дан текстовый файл, содержащий зашифрованное сообщение. Пользуясь деком, расшифровать текст. Известно, что при
шифровке каждый символ сообщения заменялся следующим за ним в деке по часовой стрелке через один.

Исходный файл с зашифрованным сообщением:
----------
ifmmp tqz
----------

Результат с расшифрованным сообщением:
----------
hello spy
----------


Задание №3
Даны три стержня и n дисков различного размера. Диски можно надевать на стержни, образуя из них башни. Перенести n дисков со стержня А на стержень С, сохранив их первоначальный
порядок. При переносе дисков необходимо соблюдать следующие правила:
- на каждом шаге со стержня на стержень переносить только один диск;
- диск нельзя помещать на диск меньшего размера;
- для промежуточного хранения можно использовать стержень В. Реализовать алгоритм, используя три стека вместо стержней А, В, С. Информация о дисках хранится в исходном файле.

Исходный файл с размерами дисков:
----------
1
2
3
4
5
6
----------

Результат с ходом выполнения операций:
------------------------------------------------------------
Переместить диск 1 с A: [6, 5, 4, 3, 2] на B: [1]
Переместить диск 2 с A: [6, 5, 4, 3] на C: [2]
Переместить диск 1 с B: [] на C: [2, 1]
Переместить диск 3 с A: [6, 5, 4] на B: [3]
Переместить диск 1 с C: [2] на A: [6, 5, 4, 1]
Переместить диск 2 с C: [] на B: [3, 2]
Переместить диск 1 с A: [6, 5, 4] на B: [3, 2, 1]
Переместить диск 4 с A: [6, 5] на C: [4]
Переместить диск 1 с B: [3, 2] на C: [4, 1]
Переместить диск 2 с B: [3] на A: [6, 5, 2]
Переместить диск 1 с C: [4] на A: [6, 5, 2, 1]
Переместить диск 3 с B: [] на C: [4, 3]
Переместить диск 1 с A: [6, 5, 2] на B: [1]
Переместить диск 2 с A: [6, 5] на C: [4, 3, 2]
Переместить диск 1 с B: [] на C: [4, 3, 2, 1]
Переместить диск 5 с A: [6] на B: [5]
Переместить диск 1 с C: [4, 3, 2] на A: [6, 1]
Переместить диск 2 с C: [4, 3] на B: [5, 2]
Переместить диск 1 с A: [6] на B: [5, 2, 1]
Переместить диск 3 с C: [4] на A: [6, 3]
Переместить диск 1 с B: [5, 2] на C: [4, 1]
Переместить диск 2 с B: [5] на A: [6, 3, 2]
Переместить диск 1 с C: [4] на A: [6, 3, 2, 1]
Переместить диск 4 с C: [] на B: [5, 4]
Переместить диск 1 с A: [6, 3, 2] на B: [5, 4, 1]
Переместить диск 2 с A: [6, 3] на C: [2]
Переместить диск 1 с B: [5, 4] на C: [2, 1]
Переместить диск 3 с A: [6] на B: [5, 4, 3]
Переместить диск 1 с C: [2] на A: [6, 1]
Переместить диск 2 с C: [] на B: [5, 4, 3, 2]
Переместить диск 1 с A: [6] на B: [5, 4, 3, 2, 1]
Переместить диск 6 с A: [] на C: [6]
Переместить диск 1 с B: [5, 4, 3, 2] на C: [6, 1]
Переместить диск 2 с B: [5, 4, 3] на A: [2]
Переместить диск 1 с C: [6] на A: [2, 1]
Переместить диск 3 с B: [5, 4] на C: [6, 3]
Переместить диск 1 с A: [2] на B: [5, 4, 1]
Переместить диск 2 с A: [] на C: [6, 3, 2]
Переместить диск 1 с B: [5, 4] на C: [6, 3, 2, 1]
Переместить диск 4 с B: [5] на A: [4]
Переместить диск 1 с C: [6, 3, 2] на A: [4, 1]
Переместить диск 2 с C: [6, 3] на B: [5, 2]
Переместить диск 1 с A: [4] на B: [5, 2, 1]
Переместить диск 3 с C: [6] на A: [4, 3]
Переместить диск 1 с B: [5, 2] на C: [6, 1]
Переместить диск 2 с B: [5] на A: [4, 3, 2]
Переместить диск 1 с C: [6] на A: [4, 3, 2, 1]
Переместить диск 5 с B: [] на C: [6, 5]
Переместить диск 1 с A: [4, 3, 2] на B: [1]
Переместить диск 2 с A: [4, 3] на C: [6, 5, 2]
Переместить диск 1 с B: [] на C: [6, 5, 2, 1]
Переместить диск 3 с A: [4] на B: [3]
Переместить диск 1 с C: [6, 5, 2] на A: [4, 1]
Переместить диск 2 с C: [6, 5] на B: [3, 2]
Переместить диск 1 с A: [4] на B: [3, 2, 1]
Переместить диск 4 с A: [] на C: [6, 5, 4]
Переместить диск 1 с B: [3, 2] на C: [6, 5, 4, 1]
Переместить диск 2 с B: [3] на A: [2]
Переместить диск 1 с C: [6, 5, 4] на A: [2, 1]
Переместить диск 3 с B: [] на C: [6, 5, 4, 3]
Переместить диск 1 с A: [2] на B: [1]
Переместить диск 2 с A: [] на C: [6, 5, 4, 3, 2]
Переместить диск 1 с B: [] на C: [6, 5, 4, 3, 2, 1]
------------------------------------------------------------


Задание №4
Дан текстовый файл с программой на алгоритмическом языке. За один просмотр файла проверить баланс круглых скобок в тексте, используя стек.

Исходный файл:
--------------------------
Program()
 This is (the program)
 if ()
 else (( ))
Array [][]
--------------------------

Результат:
------------------------------
Круглые скобки сбалансированы.
------------------------------


Задание №5
Дан текстовый файл с программой на алгоритмическом языке. За один просмотр файла проверить баланс квадратных скобок в тексте, используя дек.

Исходный файл:
--------------------------
Program()
 This is (the program)
 if ()
 else (( ))
Array [][]
--------------------------

Результат:
----------------------------------
Квадратные скобки сбалансированы.
----------------------------------


Задание №6
Дан файл из символов. Используя стек, за один просмотр файла напечатать сначала все цифры, затем все буквы, и, наконец, все остальные символы, сохраняя исходный порядок в каждой группе
символов.

Исходный файл:
-----------------------------------------------
сим1[23 в]олы 456 (зде)с7 на-писа8ны9044444
-----------------------------------------------

Результат:
---------------------------
Цифры:
123456789044444
Буквы:
символыздеснаписаны
Остальные символы:
[ ]  () -
---------------------------


Задание №7
Дан файл из целых чисел. Используя дек, за один просмотр файла напечатать сначала все отрицательные числа, затем все положительные числа, сохраняя исходный порядок в каждой группе.

Исходный файл:
-----------------------------------------------------
5 4 -12 4 191 -23 -56 31 59 12 -53 -12 5 4 9 10
-----------------------------------------------------

Результат:
----------------------------
Отрицательные числа:
-12
-23
-56
-53
-12

Положительные числа:
5
4
4
191
31
59
12
5
4
9
10
----------------------------


Задание №8
Дан текстовый файл. Используя стек, сформировать новый текстовый файл, содержащий строки исходного файла, записанные в обратном порядке: первая строка становится последней, вторая –
предпоследней и т.д.

Исходный файл:
---------------------------------
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
---------------------------------

Результат:
---------------------------------
Налево — сказку говорит.
Идёт направо — песнь заводит,
Всё ходит по цепи кругом;
И днём и ночью кот учёный
Златая цепь на дубе том:
У лукоморья дуб зелёный;
---------------------------------


