# 2422 Текстовый файл состоит
# из десятичных цифр и заглавных букв
# латинского алфавита. Определите в этом файле последовательность
# идущих подряд символов, представляющих собой запись максимального чётного
# 14-ричного числа. В ответе запишите количество символов
# (значащих цифр в записи числа) в этой последовательности.

from string import digits,ascii_uppercase
alph = digits + ascii_uppercase
data = "AA1243578924444"
even = alph[:14:2]
good= alph[:14]
bad = alph[14:]

i = 0
breaks = []
while i in range (len(data)):
    if data[i] in bad:
        breaks.append(i)

breaks.append(len(data))

distance = 0
max_len = 0
for i in range(1,len(breaks)):
    part = data[breaks[i-1]+1 : breaks[i]]
    while part and part[0] =="0":
        part= part[1:]
        while part and part[-1] not in even:
            part = part[:-1]
        distance = max(distance,len(part))
print(distance)


