#2422 Текстовый файл состоит из символов, обозначающих десятичные цифры
# и заглавные буквы латинского алфавита. Определите в прилагаемом
# файле максимальное количество идущих подряд символов,
# которые могут представлять запись чётного числа в двенадцатеричной
# системе счисления. В этой записи отсутствуют незначащие (ведущие) нули.

from string import digits, ascii_uppercase
data = "20Y14L50Z06002"
alph_12 = "0123456789AB"
left = right = 0
max_len = 0
while right < len(data)-1:
    pair_12 = data[right] + data[right+1]
    if pair_12 in alph_12:
        lenght = (right - left)//2 +1
        max_len = max(max_len,lenght)
        right +=2
    else:
        right +=1
        left = right
print(max_len)


