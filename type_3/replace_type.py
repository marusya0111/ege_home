#2422 Текстовый файл состоит из символов, обозначающих десятичные цифры
# и заглавные буквы латинского алфавита. Определите в прилагаемом
# файле максимальное количество идущих подряд символов,
# которые могут представлять запись чётного числа в двенадцатеричной
# системе счисления. В этой записи отсутствуют незначащие (ведущие) нули.

# from string import digits, ascii_uppercase
# with open("../files/2422.txt") as file:
#     data = file.read()
#     alph = digits + ascii_uppercase
#     alph_12 = "0123456789AB"
#     good = "02468A"
#     bad = "13579B"
#     max_len = 0
#     for i in bad:
#         data = data.replace(i," ")
#     data = data.split()
#     for i in data:
#         data = [i.lstrip("0") for i in data]
#         if data[-1] in good:
#             max_len = len(max(data, key=len))
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

for i in bad:
    data = data.replace(i," ")

for element in data.split():
    while element and element[0] == "0":
        element = element[1:]
    while element and element[-1] not in even:
        element = element[:-1]
    max_len = max(len(element),max_len)

print(max_len)
#25
