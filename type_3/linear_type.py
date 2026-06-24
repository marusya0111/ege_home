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
#     chetn = "02468A"
#     max_len = 0
#     cnt = 0
#     for i in range(len(data)):
#         if data[i] in alph_12 and data[-1] in chetn:
#             cnt+=1
#         else:
#             cnt = 0
#         max_len = max(max_len,cnt)
#     print(max_len)


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
cnt = max_len = 0

with open("../files/2422.txt") as file:
    data = file.readline()
    for i in range(len(data)):
        if cnt == 0 and data[i] == "0":
            continue
        if data[i] in good:
            cnt+=1
            if data[i] in even:
                max_len = max(max_len, cnt)
        else:
            cnt = 0
    print(max_len)
#25




















