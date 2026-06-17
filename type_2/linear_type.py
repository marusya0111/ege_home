#задание 2416
# data = "AABECAEABECADA"
# chars = "AE"
# i = 0
# cnt = 0
# max_len = 0
# while i < len(data)- 1:
#     if data[i] in chars and data[i+1] not in chars:
#         i+=2
#         cnt+= 1
#         max_len = max(cnt, max_len)
#     else:
#         i+=1
#         cnt= 0
# print(max_len)
#3


#2ZADACHA
# Текстовый файл состоит из символов, обозначающих буквы латинского алфавита и десятичные цифры.
#
# Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых никакие три нечётные цифры не стоят рядом.

with open("../files/13866.txt") as file:
        data = file.read()
i = 0
max_len = 0
cur_len = 0
cifri = "13579"
while i < len(data)-1:
    if data[i] not in cifri and data[i+1] not in cifri and data[i+2] not in cifri:
        i+=3
        cur_len+=1
        max_len= max(cur_len,max_len)
    else:
        i+=1
        cur_len = 0
print(max_len)
#26


