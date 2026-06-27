# 2422 Текстовый файл состоит
# из десятичных цифр и заглавных букв
# латинского алфавита. Определите в этом файле последовательность
# идущих подряд символов, представляющих собой запись максимального чётного
# 14-ричного числа. В ответе запишите количество символов
# (значащих цифр в записи числа) в этой последовательности.

# from string import digits,ascii_uppercase
# alph = digits + ascii_uppercase
# data = "AA1243578924444"
# even = alph[:14:2]
# good= alph[:14]
# bad = alph[14:]
#
# i = 0
# breaks = []
# while i in range (len(data)):
#     if data[i] in bad:
#         breaks.append(i)
#
# breaks.append(len(data))
#
# distance = 0
# max_len = 0
# for i in range(1,len(breaks)):
#     part = data[breaks[i-1]+1 : breaks[i]]
#     while part and part[0] =="0":
#         part= part[1:]
#         while part and part[-1] not in even:
#             part = part[:-1]
#         distance = max(distance,len(part))
# print(distance)

#22356 Текстовый файл состоит из десятичных цифр
# и заглавных букв латинского алфавита.
# Onределите в этом файле последовательность идущих подряд символов,
# представляющих собой запись максимального нечётного 12-ричного числа.
# В ответе запишите индекс (номер)
# первого символа (первой значащей цифры), с которого начинается запись
# этого числа в прилагаемом файле. Нумерация символов в текстовом файле начинается с нуля.

from string import digits,ascii_uppercase
alph = digits+ascii_uppercase
good = alph[:12]#0123456789ABCDE
bad = alph[12:]
even = good[1::2]

substring = 0
cnt = max_len = 0
i = 0
breaks = []
part = 0
data = "LOCIZQT00795CCAELL"
for i in range(len(data)):
    if data[i] in bad:
        breaks.append(i)
candidats = []
breaks.append(len(data))
max_len = 0
for i in range(1,len(breaks)):
    left = breaks[i-1] + 1
    right = breaks[i]
    substring = data[left:right]
    if substring:
            substring.append((substring,left))

    while part and part[0] == "0":
        part = part[1:]

    for j in range(len(part) - 1, -1, -1):
        if part[j] in even:
            number = part[:j + 1]
            end_index = right - (len(part) - j)
            start_index = end_index - (j + 1)

            candidats.append((number, start_index))

ans = max(candidats, key = lambda x : int(x[0],12))
print(ans)

