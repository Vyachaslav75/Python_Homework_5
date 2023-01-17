import random


def input_gamers(var_game):
    if var_game == 1:
        gamer1 = input('Введите имя первого игрока: ')
        gamer2 = input('Введите имя второго игрока: ')
    elif var_game == 2:
        gamer1 = input('Введите имя игрока: ')
        gamer2 = 'Simple Bot'
    elif var_game == 3:
        gamer1 = input('Введите имя игрока: ')
        gamer2 = 'Smart Bot'
    return (gamer1, gamer2)


def input_candy_col(gamer, candy, take_max, cand_tmp):
    if gamer == 'Simple Bot':
        gamer_num = random.randint(0, take_max)
    elif gamer == 'Smart Bot':
        gamer_num = smart_bot(candy, take_max, cand_tmp)
    else:
        print(gamer)
        gamer_num = int(input('Какое количество конфет вы берете?  '))
    print(f'{gamer} взял {gamer_num} конфет')
    return gamer_num


def smart_bot(candy, take_max, candy_tmp):
    if candy == candy_tmp:
        tmp = candy//(take_max+1)
        res = candy-(take_max+1)*tmp
    else:
        tmp = candy_tmp//(take_max+1)
        res = candy_tmp-(take_max+1)*tmp
    if res == 0:
        res = random.randint(1, take_max+1)
    return res


def game(candy=221, take_max=28, var_game=1):
    gamer1, gamer2 = input_gamers(var_game)
    if random.randint(0, 11) % 2 == 0:
        gamer1, gamer2 = gamer2, gamer1
    candy_tmp = candy
    while candy_tmp > 0:
        for i in [gamer1, gamer2]:
            gamer_num = input_candy_col(i, candy, take_max, candy_tmp)
            candy_tmp = candy_tmp-gamer_num
            if candy_tmp < 1:
                print(f"Игрок {i} выиграл!")
                break
            print(f'Осталось {candy_tmp}  конфет')


print('Выберите вариант игры:')
print('Если вы хотите играть вдвоем, введите 1')
print('Если вы хотите играть с ботом, введите 2')
print('Если вы хотите играть с умным ботом, введите 3')
variant_game = int(input('Введите вариант игры: '))
print('Если вы ввести свое кол-во конфет, введите 4')
user_col=0
user_col=int(input('Если вы ввести свое кол-во конфет, введите 4: '))
if user_col==4:
    user_col=int(input('Введите общее кол-во конфет : '))
    take_max=int(input('Введите сколько конфет можно взять за ход : '))
    game(candy=user_col, take_max=take_max, var_game=variant_game)
else:
    game(var_game=variant_game)
