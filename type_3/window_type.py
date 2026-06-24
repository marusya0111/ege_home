#2422 Текстовый файл состоит из символов, обозначающих десятичные цифры
# и заглавные буквы латинского алфавита. Определите в прилагаемом
# файле максимальное количество идущих подряд символов,
# которые могут представлять запись чётного числа в двенадцатеричной
# системе счисления. В этой записи отсутствуют незначащие (ведущие) нули.

# from string import digits, ascii_uppercase
# data = "20Y14L50Z06002"
# alph_12 = "0123456789AB"
# left = right = 0
# max_len = 0
# while right < len(data)-1:
#     pair_12 = data[right] + data[right+1]
#     if pair_12 in alph_12:
#         lenght = (right - left)//2 +1
#         max_len = max(max_len,lenght)
#         right +=2
#     else:
#         right +=1
#         left = right
# print(max_len)



# 2422 Текстовый файл состоит
# из десятичных цифр и заглавных букв
# латинского алфавита. Определите в этом файле последовательность
# идущих подряд символов, представляющих собой запись максимального чётного
# 14-ричного числа. В ответе запишите количество символов
# (значащих цифр в записи числа) в этой последовательности.

from string import digits,ascii_uppercase
alph = digits + ascii_uppercase
even = alph[:14:2]
good= alph[:14]
bad = alph[14:]
cnt = max_len = 0

with open("../files/2422.txt") as file:
    data = file.readline()

right = left = 0
for right in range(len(data)):
    if data[right] in bad:
        left = right +1
        continue
    while data[left] == "0":
        left+=1
    if data[right] in even:
        max_len = max(max_len,right-left +1)
print(max_len)
