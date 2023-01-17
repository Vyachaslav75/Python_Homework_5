def change_str(user_str, del_str):
    res = ' '.join(list(filter(lambda elem: del_str not in elem.lower(), user_str.split())))
    return res


s = 'АБВГВ ылоажы фыыдлх абв Зщышф вабвв ффлжв абВ'
d_s = 'абв'
print(change_str(s, d_s))
