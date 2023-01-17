
def input_gamers():
    gamer1 = input('Введите имя первого игрока: ')
    gamer2 = input('Введите имя второго игрока: ')
    return (gamer1, gamer2)


def check(array):
    for i in range(3):
        if array[i][0] == array[i][1] == array[i][2] != '_':
            return True
        elif array[0][i] == array[1][i] == array[2][i] != '_':
            return True
    if array[0][0] == array[1][1] == array[2][2] != '_':
        return True
    elif array[2][0] == array[1][1] == array[0][2] != '_':
        return True
    else:
        return False


def game(array):
    gamer1, gamer2 = input_gamers()
    count_step = 0
    while not check(array) and count_step < 9:
        for i in [gamer1, gamer2]:
            print(f'Игрок {i}, ваш ход')
            x = int(input('Введите y координату : '))
            y = int(input('Введите x координату : '))
            simb = input('Введите 0 или X :  ')
            array[x][y] = simb
            output_picture(array)
            if check(array):
                print(f'Игрок {i}, Выиграл!')
                break
            count_step += 1
            if count_step==9:
                    print('Ничья')
                    break


def output_picture(array):
    print('       0 1 2')
    print('  -----------')
    for i in range(3):
        res = f'  {i}|   '
        for j in range(3):
            res = res+array[i][j]+'|'
        print(res)
    print('')


array = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
output_picture(array)
game(array=array)
