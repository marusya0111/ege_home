#1задача
# Текстовый файл 2411.txt состоит из арабских цифр (0, 1, …, 9).
# Определите максимальное количество идущих подряд символов
# в прилагаемом файле, среди которых нет символов 1 и 2, а также 1 и 3 стоящих рядом.

# 3мя способами
#
# While
# Линейный
# Плавающее окно


#           1способ. While

# with open("files/2411.txt") as file:
#     data = file.read()
#
#     while "13" in data and "12" in data:
#         data = data.replace("12","1 2").replace("21","2 1")
#         data = data.replace("13","1 3").replace("31","3 1")
#
#     data = data.split()
#     answ = len(max(data, key=len))
#
# print(answ)
#339

#           2способ. Линейный

# with open("files/2411.txt") as file:
#      data = file.read()
# cur = 1
# max_len = 0
# for i in range(len(data)-1):
#     if data[i] + data[i+1] in ("12","13","21","31"):
#         cur=1
#     else:
#         cur+=1
#     max_len = max(cur, max_len)
# print(max_len)
#339

#            3способ окно

with open("files/2411.txt") as file:
    data = file.read()

left = 0
max_len = 0
for right in range(1,len(data)):
    if data[right] == data[right-1]:
        left = right

    cur_len = right - left + 1

    max_len = max(max_len, cur_len)
print(max_len)


