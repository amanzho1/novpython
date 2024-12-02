from os import system
system ('clear')



# Работа с файлами в Python включает в себя открытие, чтение, запись и закрытие файлов. 
# Вы можете использовать функцию open() для открытия файла, указать режим 
# (чтение, запись, добавление) и затем использовать методы, такие как read(), write(), 
# и другие для взаимодействия с содержимым файла. Не забывайте закрывать файл с 
# помощью close(), чтобы освободить ресурсы.


# file = open('имя_файла', 'режим')
# file.close()

# file = open('file.txt', 'w')
# # file.write('Hello, World!')
# file.write('Hello!')
# file.close()


# file2 = open('file1.txt', 'a')
# file2.write('Hello, World!')
# file2.close()

# file3 = open('file.txt', 'r')
# text = file3.read()
# print(text)
# file3.close()

# # Функция open() в Python используется для открытия файлов. 
# Ее синтаксис выглядит следующим образом:
# file = open('имя_файла', 'режим')

# Где:
# - 'имя_файла' - это строка, содержащая имя или путь к файлу.
# - 'режим' - это строка, указывающая режим открытия файла:
#   - 'r': чтение (по умолчанию).
#   - 'w': запись (существующий файл будет очищен, если файл не существует, 
#         он будет создан).
#   - 'a': добавление (добавление данных в конец файла).


# # ЧТЕНИЕ ФАЙЛА 
# file = open('example.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# # ЗАПИСЬ ФАЙЛА 
# file = open('example.txt', 'w')
# file.write('Новые данные для файла.')
# file.close()

# # Добавление данных в конец файла
# file = open('example.txt', 'a')
# file.write('\nДополнительные данные.')
# file.close()



example = open('examople.txt', 'r')
text = example.read()
print(text)
example.close()