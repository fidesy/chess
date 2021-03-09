from board import *


board = Board()

def letter_to_num(coord):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for letter in letters:
        if letter == coord:
            return letters.index(coord)

# функция которая проверяет поле на свободность или наличие вражеской фигуры
def isEnemy(old, new):
    return board.get(new) == '•' or board.get(new).isupper() != board.get(old).isupper()


class Place:
    def __init__(self, x, y):
        self.x = 8 - letter_to_num(x)
        self.y = int(y)

class Figure:
    def __init__(self, position, color):
        self.position = position
        self.color = color

        # board.change(self.position, self.position, self.color, 'p')

    def change_board(self, change, new_pos, fig):
        if change:
            board.change(self.position, new_pos, self.color, fig)
            self.position = new_pos
            return 1
        else:
            print('Нет возможности для такого хода. Попробуйте снова.')
            return 0


class Pawn(Figure):

    def move(self, new_pos):
        change = False

        if abs(self.position.y - new_pos.y) == 1 and self.position.x == new_pos.x and board.get(new_pos) == '•':
            change = True
        elif (self.position.y == 2 or self.position.y == 7) and self.position.x == new_pos.x \
                and abs(self.position.y - new_pos.y) == 2 and board.get(new_pos) == '•':
            change = True
        elif ((new_pos.y - self.position.y == 1 and self.color == 'white') or  \
                (self.position.y - new_pos.y == 1 and self.color == 'black')) and abs(self.position.x - new_pos.x) == 1 \
                and board.get(new_pos).isupper() != board.get(self.position).isupper() and board.get(new_pos) != '•':
            change = True

        return Figure.change_board(self, change, new_pos, 'p')


class Knight(Figure):
    def move(self, new_pos):
        change = False

        if abs(self.position.x - new_pos.x) == 1 and abs(self.position.y - new_pos.y) == 2 and \
                isEnemy(self.position, new_pos):
            change = True
        elif abs(self.position.x - new_pos.x) == 2 and abs(self.position.y - new_pos.y) == 1 and \
                isEnemy(self.position, new_pos):
            change = True

        return Figure.change_board(self, change, new_pos, 'n')


class Rook(Figure):
    def move(self, new_pos):
        change = False
        if self.position.x == new_pos.x:  # вертикально
            if self.position.y > new_pos.y:  # down
                for ind in range(self.position.y, new_pos.y, -1):
                    if board.get([self.position.x, ind - 1]) == '•' or ind == new_pos.y + 1 and \
                            isEnemy(new_pos, self.position):
                        change = True
                    else:
                        change = False
                        break

            elif new_pos.y > self.position.y:  # up
                for ind in range(self.position.y, new_pos.y):
                    if board.get([self.position.x, ind + 1]) == '•' or ind == new_pos.y - 1 and \
                            isEnemy(new_pos, self.position):
                        change = True
                    else:
                        change = False
                        break

        elif self.position.y == new_pos.y:  # горизонтально
            if self.position.x > new_pos.x:  # ->
                for ind in range(self.position.x - 1, new_pos.x - 1, -1):
                    if board.get([ind, self.position.y]) == '•' or ind == new_pos.x and \
                            isEnemy(new_pos, self.position):
                        change = True
                    else:
                        change = False
                        break

            elif new_pos.x > self.position.x:  # <-
                for ind in range(self.position.x, new_pos.x):
                    if board.get([ind + 1, self.position.y]) == '•' or ind == new_pos.x - 1 \
                            and isEnemy(new_pos, self.position):
                        change = True
                    else:
                        change = False
                        break

        return Figure.change_board(self, change, new_pos, 'r')

class Bishop(Figure):
    def move(self, new_pos):
        change = False
        if abs(self.position.x - new_pos.x) == abs(self.position.y - new_pos.y):
            if self.position.x > new_pos.x and self.position.y > new_pos.y:
                for ind in range(1, self.position.x - new_pos.x + 1):
                    if board.get([self.position.x - ind, self.position.y - ind]) == '•' or \
                            ind == self.position.x - new_pos.x and isEnemy(new_pos, self.position):
                        change = True
                    else:
                        change = False
                        break

            elif self.position.x < new_pos.x and self.position.y < new_pos.y:
                for ind in range(1, new_pos.x - self.position.x + 1):
                    if board.get([self.position.x + ind, self.position.y + ind]) == '•' or \
                            ind == new_pos.x - self.position.x and isEnemy(new_pos, self.position):
                        change = True
                    else:
                        change = False
                        break
            elif self.position.x > new_pos.x and self.position.y < new_pos.y:
                for ind in range(1, self.position.x - new_pos.x + 1):
                    if board.get([self.position.x - ind, self.position.y + ind]) == '•' or \
                            ind == self.position.x - new_pos.x and isEnemy(new_pos, self.position):
                        change = True
                    else:
                        change = False
                        break

            elif self.position.x < new_pos.x and self.position.y > new_pos.y:
                for ind in range(1, new_pos.x - self.position.x + 1):
                    if board.get([self.position.x + ind, self.position.y - ind]) == '•' or \
                            ind == new_pos.x - self.position.x and isEnemy(new_pos, self.position):
                        change = True
                    else:
                        change = False
                        break

        return Figure.change_board(self, change, new_pos, 'b')


class Queen(Bishop, Rook):
    def move(self, new_pos):
        if Bishop.move(self, new_pos) == 1:
            return Bishop.change_board(self, True, new_pos, 'q')
        elif Rook.move(self, new_pos) == 1:
            return Rook.change_board(self, True, new_pos, 'q')


class King(Figure):
    def move(self, new_pos):
        change = False

        if abs(self.position.x - new_pos.x) == 1 and abs(self.position.y - new_pos.y) == 1 and \
                isEnemy(self.position, new_pos):
            change = True
        elif self.position.x == new_pos.x and abs(self.position.y - new_pos.y) == 1 and isEnemy(self.position, new_pos):
            change = True
        elif abs(self.position.x - new_pos.x) == 1 and self.position.y == new_pos.y and isEnemy(self.position, new_pos):
            change = True

        return Figure.change_board(self, change, new_pos, 'k')


class Checker(Figure):

    def move(self, new_pos):
        change = False

        if (new_pos.y - self.position.y == 1 and self.color == 'white' or
            self.position.y - new_pos.y == 1 and self.color == 'black') and abs(self.position.x - new_pos.x) == 1 \
                and board.get(new_pos) == '•':
            change = True

        def to_attack(last, new):
            if type(new) != list:
                new_ = [new.x, new.y]
            else:
                new_ = new

            coordinates = [min(new_[0], last.x) + 1, min(new_[1], last.y) + 1]
            if abs(new_[1] - last.y) == 2 and abs(new_[0] - last.x) == 2:
                if board.get(coordinates).isupper() != \
                        board.get(last) and board.get(coordinates) != '•' and board.get(new_) == '•':
                    return 1


        potential_attack = [[new_pos.x + 2, new_pos.y + 2], [new_pos.x + 2, new_pos.y - 2],
                            [new_pos.x - 2, new_pos.y - 2], [new_pos.x - 2, new_pos.y + 2]]

        if to_attack(self.position, new_pos) == 1:
            board.change(self.position, [min(self.position.x, new_pos.x) + 1, min(self.position.y, new_pos.y) + 1],
                         self.color, '•')
            Figure.change_board(self, True, new_pos, 'p')
            change = 'attack'


        for coord in potential_attack:
            if coord[0] < 9 and coord[1] < 9:
                if to_attack(new_pos, coord) == 1 and change == 'attack':
                    change = 'again'


        if change is True or change == 'attack':
            return Figure.change_board(self, change, new_pos, 'p')
        elif change == 'again':
            print('Продолжайте ход...')
            board.show()
            return 0
        elif change is False:
            print('Нет возможности для такого хода. Попробуйте снова.')
            return 0



