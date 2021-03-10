class Board:
    def __init__(self):
        self.board = [['‧'] * 9 for i in range(9)]

    def show(self):
        print('')
        print('   A  B  C  D  E  F  G  H')

        for i in range(8):
            print(end='\n')
            for j in range(9):
                self.board[i][-1] = str(8 - i) + ' '
                print(self.board[i][j-1].center(2), end=' ')
        print('')


    def change(self, last, new_pos, color, fig):
        if last is None:
            self.board[8 - new_pos.y][8 - new_pos.x] = fig
        else:
            if color == 'white':
                fig = '○'
            elif color == 'black':
                fig = '●'
            if type(new_pos) == list:  # исключительно для шашек
                self.board[8 - last.y][8 - last.x] = '‧'
                self.board[8 - new_pos[1]][8 - new_pos[0]] = fig
            else:
                self.board[8 - last.y][8 - last.x] = '‧'
                self.board[8 - new_pos.y][8 - new_pos.x] = fig

    def get(self, position):
        if type(position) == list:
            return self.board[8 - position[1]][8 - position[0]]
        else:
            return self.board[8 - position.y][8 - position.x]

    def clean(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == '*':
                    self.board[i][j] = '‧'
                elif '^' in self.board[i][j]:
                    self.board[i][j] = self.board[i][j].replace('^', '')

board = Board()

def letter_to_num(coord):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for letter in letters:
        if letter == coord:
            return letters.index(coord)

# функция которая проверяет поле на свободность или наличие вражеской фигуры
def isEnemy(old, new):
    return board.get(new) == '‧' or board.get(new).isupper() != board.get(old).isupper()

class Place:
    def __init__(self, x, y):
        self.x = 8 - letter_to_num(x)
        self.y = int(y)

class Figure:
    def __init__(self, position, color):
        self.position = position
        self.color = color

        if color == 'black':
            board.change(self.position, self.position, self.color, '●')
        else:
            board.change(self.position, self.position, self.color, '○')


    def change_board(self, change, new_pos, fig):
        if change:
            board.change(self.position, new_pos, self.color, fig)
            self.position = new_pos
            return 1
        else:
            print('Нет возможности для такого хода. Попробуйте снова.')
            return 0

    def help(self, current_piece):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        different = False
        to_attack = []
        for i in range(8):
            for j in range(8):
                coordinates = Place(letters[i], j + 1)
                print(coordinates.x, coordinates.y)
                if current_piece.move(coordinates, 'check') == 1:
                    different = True
                    to_attack.append([8 - coordinates.y, 8 - coordinates.x])

        for elem in to_attack:
            if board.board[elem[0]][elem[1]] == '‧':
                board.board[elem[0]][elem[1]] = '*'
            else:
                board.board[elem[0]][elem[1]] += '^'
        if different:
            board.show()
            board.clean()
        else:
            print('Нет возможности для хода.')


class Checker(Figure):

    def move(self, new_pos, mission):
        change = False

        if (new_pos.y - self.position.y == 1 and self.color == 'white' or
            self.position.y - new_pos.y == 1 and self.color == 'black') and abs(self.position.x - new_pos.x) == 1 \
                and board.get(new_pos) == '‧':
            change = True

        def to_attack(last, new):
            if type(new) != list:
                new_ = [new.x, new.y]
            else:
                new_ = new

            coordinates = [min(new_[0], last.x) + 1, min(new_[1], last.y) + 1]
            if abs(new_[1] - last.y) == 2 and abs(new_[0] - last.x) == 2:
                if board.get(coordinates) != board.get(last) and board.get(coordinates) != '‧' and \
                        board.get(new_) == '‧':
                    return 1


        potential_attack = [[new_pos.x + 2, new_pos.y + 2], [new_pos.x + 2, new_pos.y - 2],
                            [new_pos.x - 2, new_pos.y - 2], [new_pos.x - 2, new_pos.y + 2]]

        if to_attack(self.position, new_pos) == 1:
            board.change(self.position, [min(self.position.x, new_pos.x) + 1, min(self.position.y, new_pos.y) + 1],
                         '', '‧')
            Figure.change_board(self, True, new_pos, '‧')
            change = 'attack'

        for coord in potential_attack:

            if coord[0] < 9 and coord[0] > 0 and coord[1] < 9 and coord[1] > 0:
                if to_attack(new_pos, coord) == 1 and change == 'attack':
                    change = 'again'


        if change is True or change == 'attack':
            return Figure.change_board(self, change, new_pos, '‧')
        elif change == 'again':
            print('Продолжайте ход...')
            board.show()
            return 0
        elif change == 'again':
            return 1
        elif change is False:
            print('Нет возможности для такого хода. Попробуйте снова.')
            return 0

class Game:
    def __init__(self):
        self.count = 1
        self.color_ = 'white'
        self.checker = [Checker(Place('A', '1'), 'white'),
                        Checker(Place('A', '3'), 'white'),
                        Checker(Place('B', '2'), 'white'),
                        Checker(Place('C', '1'), 'white'),
                        Checker(Place('C', '3'), 'white'),
                        Checker(Place('D', '2'), 'white'),
                        Checker(Place('E', '1'), 'white'),
                        Checker(Place('E', '3'), 'white'),
                        Checker(Place('F', '2'), 'white'),
                        Checker(Place('G', '1'), 'white'),
                        Checker(Place('G', '3'), 'white'),
                        Checker(Place('H', '2'), 'white'),
                        Checker(Place('A', '7'), 'black'),
                        Checker(Place('B', '8'), 'black'),
                        Checker(Place('B', '6'), 'black'),
                        Checker(Place('C', '7'), 'black'),
                        Checker(Place('D', '8'), 'black'),
                        Checker(Place('D', '6'), 'black'),
                        Checker(Place('E', '7'), 'black'),
                        Checker(Place('F', '8'), 'black'),
                        Checker(Place('F', '6'), 'black'),
                        Checker(Place('G', '7'), 'black'),
                        Checker(Place('H', '8'), 'black'),
                        Checker(Place('H', '6'), 'black')]
        self.figures = []

        self.figures.append(self.checker)

    def game(self):
        while True:
            # print('''
            # Опции:
            #         1. Сделать ход.
            #         2. Показать поле.
            #         3. Подсказка хода.
            #         ''')
            try:
                # choice = int(input('Введитите опцию: '))
                choice = 1
                if choice == 1:
                    self.move()
                elif choice == 2:
                    board.show()
                elif choice == 3:
                    current_piece = self.get_piece()
                    current_piece.help(current_piece)
                else:
                    print('Неизвестная команда.')
            except:
                print('Неизвестная команда.')


    def get_piece(self):
        print('')
        if self.color_ == 'white':
            print(f'{self.count} ход белых.')
        else:
            print(f'{self.count} ход черных.')
        move = input('Введите координаты фигуры для хода: ')
        try:
            position = Place(move[0].upper(), move[1])
        except:
            print('Неправильно введены координаты, попробуйте снова.')
            return None
        state = False
        for figure in self.figures:
            for fig in figure:
                if fig.position.x == position.x and fig.position.y == position.y and fig.color == self.color_:
                    current_fig = fig
                    state = True
                    break
        if state:
            return current_fig
        else:
            print('Неправильно введены координаты, попробуйте снова.')

    def move(self):
        current_piece = self.get_piece()

        if current_piece != None:
            try:
                old_position = current_piece.position  # for saving data

                new_coord = input('Введите координаты для хода: ')
                new_coord = Place(new_coord[0].upper(), new_coord[1])
                state = current_piece.move(new_coord, 'attack')
                if state == 1:
                    board.show()
            except:
                print('Неправильно введены координаты, попробуйте снова.')
                state = 0
            if self.color_ == 'white' and state == 1:
                self.color_ = 'black'
            elif self.color_ == 'black' and state == 1:
                self.color_ = 'white'
                self.count += 1

if __name__ == '__main__':
    game = Game()
    game.game()