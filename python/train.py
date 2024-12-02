# number = 15
# if number > 10:
#     print("Число больше 10")
# else:
#     print("Число меньше или равно 10")


# num = int(input('Num: '))
# if num % 2 == 0:
#     print('Четный')
# else:
#     print('No')


# text = " "
# if text == " ":
#     print('pusto')
# else:
#     print('No')

# day = input('Day: ')
# if day == 'Понедельник':
#     print('Начало недели')
# else:
#     print('Будни дни')

# user = int(input('Num: '))
# if user > 0:
#     print('Положительное число')
# else:
#     print('Отрицательоне число')


# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print('Error')

# try:
#    num = int('abc')
# except ValueError:
#    print('Error')



# try: 
#     num = int(input())
#     num2 = int(input())
    
#     num + num2
# except Exception as ex:
#     print('Error: Вводить можно только число')


# lists = [1,2,3]
# try:
#     element = lists[5]
# except Exception as ex:
#     print('Error: Что то', ex)

# try:
#     s = 'text' / 2
# except Exception as ex:
#     print('Error: zz', ex)
 


# num = int(input('Num: '))
# if 10 <= num <= 50:
#     print(f'Num: {num}')
# else:
#     print(f'Num: Not {num}')


# text = input('Str: ')
# if text.startswith('A'):
#     print('Строка начинается с буквы А')
# elif text.startswith('В'):
#     print('Строка начинается с буквы В')
# else:
#     print('Not')


# num = int(input('Num: '))
# if num % 3 == 0 and num % 5 == 0:
#     print('Yes')
# elif num % 3 == 0:
#     print('Только на 3')
# elif num % 5 == 0:
#     print('Только на 5')
# else:
#     print('Error')


# text = input('')
# text2 = input('')
# if len(text) > len(text2):
#     print(f'{text} больше')
# elif len(text) < len(text2):
#     print(f'{text2} больше')
# else:
#     print(f'{text}:{text2} равно')


# try:
#     num1 = int(input('Num: '))
#     s = 100 / num1
#     print(s)
# except Exception as ex:
#     print('Error: ', ex)

# try:
#     num = int('asd')
# except Exception as ex:
#     print('Error:', ex)


# try:
#     num1 = 7
#     num2 = 0

#     result =  num1 / num2
# except Exception as ex:
#     print('Error', ex)


# try:
#     filename = input()
#     with open(filename, 'r') as file:
#         print(file.read())
# except Exception as ex:
#     print('Error: ', ex)


# try: 
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 / num2
#     print(result)
# except Exception as ex:
#     print('Error: ', ex)

# try:
#     num =  list(map(int, input('').split()))
#     result = sum(num) / len(num)
#     print(result)
# except Exception as ex:
#     print('Error: ', ex)

# try: 
#     text = input('')
#     result = int(text)
#     print(result)
# except Exception as ex:
#     print('Error:', ex)



# found = None
# for i in 'hello':
#     if i == 'l':
#         found = True
#         break
# else:
#     found = False

# print(found)

