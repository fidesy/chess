class Board:
    def __init__(self):
        self.board = [['•'] * 9 for i in range(9)]
        figures = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']

        for i in range(8):
            self.board[1][i] = 'p'
            self.board[6][i] = 'P'
            self.board[0][i] = figures[i]
            self.board[7][i] = figures[i].upper()


    def show(self):
        print('')
        print('   A B C D E F G H')
        for i in range(8):
            print(end='\n')
            for j in range(9):
                self.board[i][-1] = str(8 - i) + ' '
                print(self.board[i][j-1], end=' ')
        print('')


    def change(self, last, new_pos, color, fig):
        if color == 'white':
            fig = fig.upper()
        if type(new_pos) == list:  # исключительно для шашек
            self.board[8 - last.y][8 - last.x] = '•'
            self.board[8 - new_pos[1]][8 - new_pos[0]] = fig
        else:
            self.board[8 - last.y][8 - last.x] = '•'
            self.board[8 - new_pos.y][8 - new_pos.x] = fig


    def get(self, position):
        if type(position) == list:
            return self.board[8 - position[1]][8 - position[0]]
        else:
            return self.board[8 - position.y][8 - position.x]






