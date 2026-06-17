#1задача
# Текстовый файл 2411.txt состоит из арабских цифр (0, 1, …, 9).
# Определите максимальное количество идущих подряд символов
# в прилагаемом файле, среди которых нет символов 1 и 2, а также 1 и 3 стоящих рядом.

# with open("../files/2411.txt") as file:
#     data = file.read()
#
# left = 0
# max_len = 0
# for right in range(1,len(data)):
#     if data[right] == data[right-1]:
#         left = right
#
#     cur_len = right - left + 1
#
#     max_len = max(max_len, cur_len)
# print(max_len)

