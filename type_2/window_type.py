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
        current_len= (right- left) // 3
        max_len = max(max_len,current_len)
    else:
        right+=1
        left = right
print(max_len)
#?

# екстовый файл состоит из символов N, O и P.
# Определите максимальное количество идущих подряд последовательностей символов NPO или PNO в прилагаемом файле.
# Искомая последовательность должна состоять только из троек NPO, или только из троек PNO, или только из троек NPO и PNO в произвольном порядке их следования
pairs = ["NOP","PNO"]
left = right = 0
max_len = 0
while right < len(data)-1:
    pair = data[right] + data[right+1]
    if pair in pairs:
        lenght = (right - left)//2 +1
        max_len = max(max_len,lenght)
        right +=3
    else:
        right +=1
        left = right
print(max_len)



