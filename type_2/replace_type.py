#задание 2416
# data = "AABECAEABECADA"
# pairs = ["AB",'AC','AD','EB','EC','ED']
# for i in pairs:
#     data = data.replace(i,"*")
# for i in "ABCDE":
#     data = data.replace(i," ")
# data = data.split()
# max_len = len(max(data, key=len))
# print(max_len)
#3

#2ZADACHA
# Текстовый файл состоит из символов, обозначающих буквы латинского алфавита и десятичные цифры.
#
# Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых никакие три нечётные цифры не стоят рядом.

with open("../files/13866.txt") as file:
    data = file.read()
gr = "2468QWERTYUIOPASDFGHJKLZXCVBNM"
for i in gr:
    data = data.replace(i,"*")
for i in "13579":
    data = data.replace(i," ")
data = data.split()

max_len = len(max(data, key=len))
print(max_len)
#79?
