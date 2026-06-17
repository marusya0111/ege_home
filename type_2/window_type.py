#задание 2416

# data = "AABECAEABECADA"
# chars = "AE"
# max_len = 0
# left = right = 0
# while right < len(data)- 1:
#     if data[right] in chars and data[right+1] not in chars:
#         right+=2
#         current_len= (right- left) // 2
#         max_len = max(max_len,current_len)
#     else:
#         right+=1
#         left = right
# print(max_len)
#3


#2ZADACHA/ ?как действовать через метод окна, если у нас не 2 символа а три?
# Текстовый файл состоит из символов, обозначающих буквы латинского алфавита и десятичные цифры.
# Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых никакие три нечётные цифры не стоят рядом.

with open("../files/13866.txt") as file:
    data = file.read()
chars = "13579"
max_len = 0
left = right = 0
while right < len(data)- 1:
    if data[right] in chars and data[right+1] not in chars:
        right+=3
        current_len= (right- left) // 2
        max_len = max(max_len,current_len)
    else:
        right+=1
        left = right
print(max_len)
#?
