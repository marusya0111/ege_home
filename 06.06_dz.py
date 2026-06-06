#1 задача.
# Текстовый файл состоит не более чем из 106 символов и содержит
# только заглавные буквы латинского алфавита (A..Z).
# Определите максимальное количество идущих подряд символов,
# среди которых нет сочетания стоящих рядом букв P и R (в любом порядке).

      #1способ
# with open ("files/1873.txt") as file:
#     data = file.read()
#     data = data.replace("PR","P R").replace("RP","R P")
#     answ = len(max(data.split(),key = len))
#     print(answ)
#2940

    #2способ
# with open ("files/1873.txt") as file:
#     data = file.read()
# count = 1
# max_len = 0
# for i in range(len(data)-1):
#     if data[i] + data[i+1] in ("PR","RP"):
#         count=1
#     else:
#         count+=1
#     max_len = max(count, max_len)
# print(max_len)
#2940


# 2задача.
#           1 способ
# Текстовый файл состоит из арабских цифр (0, 1, …, 9).
# Определите максимальное количество идущих подряд символов
# в прилагаемом файле, среди которых нет символов 0, стоящих рядом.

# with open("files/2410.txt") as file:
#     data = file.read()
#     data = data.replace("00","0 0")
#     answer = len(max(data.split(), key=len))
#     print(answer)
#977

#           2способ
with open("files/2410.txt") as file:
    data = file.read()
count = 1
max_len = 0
for i in range(len(data)-1):
    if data[i] + data[i+1] in "00":
        count = 1
    else:
        count+=1
    max_len = max(count, max_len)
print(max_len)
#977



