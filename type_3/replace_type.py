#2422 Текстовый файл состоит из символов, обозначающих десятичные цифры
# и заглавные буквы латинского алфавита. Определите в прилагаемом
# файле максимальное количество идущих подряд символов,
# которые могут представлять запись чётного числа в двенадцатеричной
# системе счисления. В этой записи отсутствуют незначащие (ведущие) нули.

from string import digits, ascii_uppercase
with open("../files/2422.txt") as file:
    data = file.read()
    alph = digits + ascii_uppercase
    alph_12 = "0123456789AB"
    good = "02468A"
    bad = "13579B"
    max_len = 0
    for i in bad:
        data = data.replace(i," ")
    data = data.split()
    for i in data:
        data = [i.lstrip("0") for i in data]
        if data[-1] in good:
            max_len = len(max(data, key=len))
print(max_len)







