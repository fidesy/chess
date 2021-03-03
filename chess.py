#объявление переменных для работы
pole = [["*"] * 9 for z in range(8)]
up = ["    ","r", "n", "b", "q", "k", "b", "n", "r"] 
digit = ["8","7","6","5","4","3","2","1"]
alph = "     A  B  C  D  E  F  G  H"
alp = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
down = ["    ", "R", "N", "B", "Q", "K", "B", "N", "R"]
first = ["    ", "p", "p", "p", "p", "p", "p", "p", "p"]
second = ["   ", "P", "P", "P", "P", "P", "P", "P", "P"]
chess = ["♖","♘" ,"♗","♕","♔","♙","♜", "♞","♝","♛", "♚", "♟︎ "]
figures = ["r","n","b","q","k","p","R","N","B","Q","K","P"]
game = 1
state = 1
move = 1
white_attack = [["*"] * 9 for z in range(8)]
#переменные для реализации рокировки
lr,rr,LR,RR,wk,bk = 0,0,0,0,0,0 

#расстановка шахмат на доску
for i in range(8):
    for j in range(9):
        if i != 1 and i!=6 and i != 0 and i !=7:
            continue
        elif i == 0:
            pole[i][j] = up[j]
            white_attack[i][j] = up[j]
        elif i == 7:
            pole[i][j] = down[j]
            white_attack[i][j] = down[j]
        elif i == 1:
            pole[i][j] = first[j]
            white_attack[i][j] = first[j]
        else:
            pole[i][j] = second[j]
            white_attack[i][j] = second[j]

#установление номеров полей
for i in range(8):
    pole[i][0] = str(8-i) + "   " 
    white_attack[i][0] = str(8-i) + "   " 

#текст при старте программы

print("Игра - шахматы")
print(end="\n")
print("Заглавными буквами обозначены белые фигуры, прописными соответвенно черные.")
print(end="\n")

#функция для движения пешек
def peshka(st, x, y, new_x, new_y,enemy,var,friend):
#st=1 - белая фигура
    left = 1
    if st == 1:
        fig = "P"
    else:
        fig = "p"
    if st == 1:
        #проверка поля для движения на одну клетку 
        if new_x == x+1 and new_y == y and pole[8 - new_x][new_y] == "*":
            play = 0
        #проверка поля для движения на две клетки
        elif new_x == x + 2 and new_y == y and pole[8 - new_x][new_y] == "*" and x == 2:
            play = 0
        #проверка поля для атаки пешкой
        elif (new_x == x+1 and new_y == y -1 and pole[8 - new_x][new_y] in enemy) or (new_x == x +1 and new_y == y +1 and pole[8 - new_x][new_y] in enemy):
           play = 0
        elif new_x == x+1 and new_y == y -1 and pole[8 - new_x][new_y] not in friend:
           left = 0
           play = 0
        elif new_x == x +1 and new_y == y +1 and pole[8 - new_x][new_y] not in friend:
           left = 0
           play = 0
        else:
            play = 1
    #аналогичные условия для черной пешки
    else:
        if new_x == x-1 and new_y == y and pole[8 - new_x][new_y] == "*":
            play = 0
        elif  new_x == x-2 and new_y == y and pole[8 - new_x][new_y] == "*" and x == 7:
           play = 0
        elif (new_x == x-1 and new_y == y -1 and pole[8 - new_x][new_y] in enemy) or (new_x == x -1 and new_y == y +1 and pole[8 - new_x][new_y] in enemy):
           play = 0
       #условия для обозначения клетки, которую можно атаковать
        elif new_x == x-1 and new_y == y -1 and pole[8 - new_x][new_y] not in friend:
           left = 0
           play = 0
        elif new_x == x -1 and new_y == y +1 and pole[8 - new_x][new_y] not in friend:
           left = 0
           play = 0
       
        else:
            play = 1
    if play == 0 and var == 0:
        pole[8-new_x][new_y] = fig
        pole[8-x][y] = "*"
    elif ((play == 0 and var==1 and abs(new_x-x) == 1) or left ==0) and abs(new_x - x) == 1 and abs(new_y-y) != 0:
        white_attack[8-new_x][new_y] +="^"
    return play
    
#функция для движения коня
def horse(st, x, y, new_x, new_y, enemy,var):
    if st == 1:
        fig = "N"
    else:
        fig = "n"
    #все возможные варианты ходьбы конем
    if ((new_x == x + 2 and new_y == y + 1) or
    (new_x == x + 2 and new_y == y - 1) or
    (new_x == x - 2 and new_y == y + 1) or
    (new_x == x - 2 and new_y == y - 1) or
    (new_x == x + 1 and new_y == y + 2) or
    (new_x == x + 1 and new_y == y - 2) or
    (new_x == x - 1 and new_y == y + 2) or
    (new_x == x - 1 and new_y == y - 2)) and (pole[8-new_x][new_y] == "*" or pole[8-new_x][new_y] in enemy):
        play = 0
    else:
        play = 1
    if play == 0 and var == 0:
        pole[8-new_x][new_y] = fig
        pole[8-x][y] = "*"
    elif play == 0 and var==1:
        white_attack[8-new_x][new_y] +="^"
    return play
        
#функция для движения ладьи 
def rook(st, x, y, new_x, new_y, enemy,var):
    if st == 1:
        fig = "R"
    else:
        fig = "r"
    if new_y ==  y and new_x !=x:
        if x > new_x:
            for i in range(x-1, new_x-1, -1):
                if pole[8-i][y] == "*" or (pole[8-i][y] == pole[8-new_x][new_y] and (pole[8-new_x][new_y] in enemy or pole[8-new_x][new_y] == "*")):
                    play = 0
                else:
                    play = 1
                    break
        else:
            for i in range(x+1, new_x+1):
                if pole[8-i][y] == "*" or (pole[8-i][y] == pole[8-new_x][new_y] and (pole[8-new_x][new_y] in enemy or pole[8-new_x][new_y] == "*")):
                    play = 0
                    
                else:
                
                    play = 1
                    break
    elif new_x == x and new_y != y:
        if y > new_y:
            for i in range(y-1, new_y-1, -1):
                if pole[8-x][i] == "*" or (pole[8-x][i] == pole[8-new_x][new_y] and (pole[8-new_x][new_y] in enemy or pole[8-new_x][new_y] == "*")):
                    play = 0
                else:
                    play = 1
                    break
        else:
            for i in range(y+1, new_y+1):
                if pole[8-x][i] == "*" or (pole[8-x][i] == pole[8-new_x][new_y] and (pole[8-new_x][new_y] in enemy or pole[8-new_x][new_y] == "*")):
                    play = 0
                else:
                    play = 1
                    break
    else:
        play = 1
        
    if play == 0 and var == 0:
        pole[8-new_x][new_y] = fig
        pole[8-x][y] = "*"
    elif play == 0 and var==1:
        white_attack[8-new_x][new_y] +="^"
    return play 
    
#функция для движения слона 
def bishop(st, x, y, new_x, new_y,enemy,var):
    if st == 1:
        fig = "B"
    else:
        fig = "b"
    #движение вниз-влево
    try:
        if x > new_x and y > new_y:
            for i in range(1,x-new_x+1):
                if (pole[8-x+i][y-i] == "*" or (pole[8-x+i][y-i] == pole[8-new_x][new_y] and (pole[8-new_x][new_y] in enemy or pole[8-new_x][new_y] == "*"))) and y - new_y == x - new_x:
                    play = 0
                else:
                    play = 1
                    break
        #движение вниз-вправо
        elif x > new_x and y < new_y:
            for i in range(1,x-new_x+1):
                if (pole[8-x+i][y+i] == "*" or (pole[8-x+i][y+i] == pole[8-new_x][new_y] and (pole[8-new_x][new_y] in enemy or pole[8-new_x][new_y] == "*"))) and new_y - y== x - new_x:
                    play = 0
                else:
                    play = 1
                    break
        #движение вверх-вправо
        elif x <new_x and y < new_y:
            for i in range(1,new_x-x+1):
                if (pole[8-x-i][y+i] == "*" or (pole[8-x-i][y+i] == pole[8-new_x][new_y] and (pole[8-new_x][new_y] in enemy or pole[8-new_x][new_y] == "*"))) and new_y - y == new_x - x:
                    play = 0
                else:
                    play = 1
                    break
         #движение вверх-влево       
        elif x < new_x and y > new_y:
            for i in range(1,new_x-x+1):
                if (pole[8-x-i][y-i] == "*" or (pole[8-x-i][y-i] == pole[8-new_x][new_y] and (pole[8-new_x][new_y] in enemy or pole[8-new_x][new_y] == "*"))) and y - new_y == new_x - x:
                    play = 0
                else:
                    play = 1
                    break
        else:
            play = 1
    except IndexError:
        play = 0
    
    if play == 0 and var == 0:
        pole[8-new_x][new_y] = fig
        pole[8-x][y] = "*"
    elif play == 0 and var==1:
        white_attack[8-new_x][new_y] +="^"
    return play

#функция для движения ферзя
def queen(st, x, y, new_x, new_y, enemy,var):
    if st == 1:
        fig = "Q"
    else:
        fig = "q"
    status = rook(st, x, y, new_x, new_y, enemy,var)
    if status == 0 and var == 0:
            pole[8-new_x][new_y] = fig
    elif status == 0 and var == 1:
        pass
    else:
        status = bishop(st, x, y, new_x, new_y, enemy,var)
        if status == 0 and var == 0:
            pole[8-new_x][new_y] = fig
        elif status == 0 and var == 1:
            pass
        else:
            status = 1
    return status
    
def king(st, x, y, new_x, new_y, enemy,var):
    if st == 1:
        fig = "K"
    else:
        fig = "k"
    if (new_x == x or new_y == y) and (abs(new_x - x) == 1 or abs(new_y - y) == 1):
        if (pole[8-new_x][new_y] == "*" or pole[8-new_x][new_y] in enemy) and  (abs(new_y - y) == 1 or abs(new_x - x) == 1):
            play = 0
        else:
            play = 1
    elif abs(new_y - y) == 1 and abs(new_x - x) == 1:
        if  pole[8-new_x][new_y] in enemy or pole[8-new_x][new_y] == "*":
            play = 0
        else:
            play = 1
    elif state == 1 and var == 0:
        if new_x == 1 and new_y == 3 and pole[7][2] == "*" and pole[7][3] == "*" and pole[7][4] == "*" and LR == 0 and wk == 0:
            pole[7][4] = "R"
            pole[7][1] = "*"
            play = 0
        elif new_x == 1 and new_y == 7 and pole[7][6] == "*" and pole[7][7] == "*" and RR == 0 and wk == 0:
            pole[7][6] = "R"
            pole[7][8] = "*"
            play = 0
        else: play = 1
    elif state == 2 and var == 0:
        if new_x == 8 and new_y == 3 and pole[0][2] == "*" and pole[0][3] == "*" and pole[0][4] == "*" and lr == 0 and bk == 0:
            pole[0][4] = "r"
            pole[0][1] = "*"
            play = 0
        elif new_x == 8 and new_y == 7 and pole[0][6] == "*" and pole[0][7] == "*" and rr == 0 and bk == 0:
            pole[0][6] = "r"
            pole[0][8] = "*"
            play = 0
        else: play = 1
    else:
        play = 1
        

        
    if play == 0 and var == 0:
        pole[8-new_x][new_y] = fig
        pole[8-x][y] = "*"
    elif play == 0 and var == 1:
        white_attack[8-new_x][new_y] += "^"
    return play
                        


#основной цикл
while game:
    if pole[7][1] == "*": LR = 1
    if pole[7][8] == "*": RR = 1
    if pole[7][5] == "*": wk = 1
    if pole[0][1] == "*": lr = 1
    if pole[0][8] == "*": rr = 1
    if pole[0][5] == "*": bk = 1

    if state == 1:
        #обозначение вражеских и союзных фигур
        enemy = up + first
        friend = down + second
    else:
        friend = up + first
        enemy = down + second
    print(alph)
    for i in range(8):
        print(end="\n")
        for j in range(9):
            if pole[i][j] in figures:
                print(chess[figures.index(pole[i][j])].center(2), end=" ")
                continue 
            else:
                print(pole[i][j].center(2), end=" ")
    print(end="\n")
    if state == 1:
        color = "белыми"
        clr = "белых"
    else:
        color = "черными"
        clr = "черных"
    print(end="\n")
    print(str(move)+ " ход " + clr)
    coord = input("Введите позицию фигуры для хода "+color+":")
    coord = coord.upper()
    #нахождение фигуры на введенной клетке
    if coord[0] in alp and len(coord) > 1 and coord[1] in digit and coord[0] != " ":
        current_unit = pole[digit.index(coord[1])][alp.index(coord[0])]
    else:
        print("Неправильно введены координаты, попробуйте снова")
        print(end="\n")
        continue 
#проверка на возможность хода введенной фигурой
    if current_unit not in friend:
        print("На указанной координате нет возможной фигуры для хода, попробуйте снова")
        print(end="\n")
        continue 
    else:
        play = 0
        #введение координат для хода фигурой
        new_coord = input("Введите координаты для хода:")
        new_coord = new_coord.upper()
        #проверка корректности координаты
        try:
            if new_coord[0] in alp and len(new_coord) == 2 and new_coord[0] != " " and coord[1] in digit:
                if current_unit == "p" or current_unit == "P":
                    play = peshka(state, int(coord[1]), alp.index(coord[0]),  int(new_coord[1]), alp.index(new_coord[0]), enemy,0, friend)
                elif current_unit == "N" or current_unit == "n":
                    play = horse(state, int(coord[1]), alp.index(coord[0]),  int(new_coord[1]), alp.index(new_coord[0]), enemy,0)
                elif current_unit == "R" or current_unit == "r":
                    play = rook(state, int(coord[1]), alp.index(coord[0]),  int(new_coord[1]), alp.index(new_coord[0]), enemy,0)
                elif current_unit == "B" or current_unit == "b":
                    play = bishop(state, int(coord[1]), alp.index(coord[0]),  int(new_coord[1]), alp.index(new_coord[0]), enemy,0)
                elif current_unit == "Q" or current_unit == "q":
                    play = queen(state, int(coord[1]), alp.index(coord[0]),  int(new_coord[1]), alp.index(new_coord[0]), enemy,0)
                elif current_unit == "K" or current_unit == "k":
                    play = king(state, int(coord[1]), alp.index(coord[0]),  int(new_coord[1]), alp.index(new_coord[0]), enemy,0)
                    
            else:
                play = 1
        except  ValueError:
                  play = 1

       
    
     #смена сторон для хода   
    if state == 1 and play == 0:
        state = 2
    elif state == 2 and play == 0:
        state = 1
        move += 1
    else:
        print("Неправильно введены координаты, попробуйте снова")
        continue