def zipper(user_str):
    count = 1
    res = ''
    for i in range(1, len(user_str)):
        if user_str[i-1] == user_str[i]:
            count += 1
            if i == len(user_str)-1:
                res = res+str(count)+user_str[i-1]
        else:
            res = res+str(count)+user_str[i-1]
            count = 1
            if i == len(user_str)-1:
                res = res+str(count)+user_str[i]
    return res


def unzipper(user_str):
    res = ''
    for i in range(0, len(user_str), 2):
        res = res+user_str[i+1]*int(user_str[i])
    return res


#s1 = 'aasdddfffggggGGjjIIIKK'
#print(s1)
#s1 = zipper(s1)
#print(s1)
#s = '11122211335456666773444'
#s = zipper(s)
#print(s)
#print(unzipper(s1))
#print(unzipper(s))

s = input('Введите строку для упаковки: ')
print('Упакованная строка: ' + zipper(s))
s = input('Введите строку для распаковки: ')
print('Распакованная строка: ' + unzipper(s))