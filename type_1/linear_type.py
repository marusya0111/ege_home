#1задача
# Текстовый файл 2411.txt состоит из арабских цифр (0, 1, …, 9).
# Определите максимальное количество идущих подряд символов
# в прилагаемом файле, среди которых нет символов 1 и 2, а также 1 и 3 стоящих рядом.

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

