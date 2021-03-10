class Board:
    def __init__(self):
        self.board = self.create_board()
        self.hints = self.create_board()

    def create_board(self):
        board = [['•'] * 9 for i in range(9)]
        figures = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        for i in range(8):
            board[1][i] = 'p'
            board[6][i] = 'P'
            board[0][i] = figures[i]
            board[7][i] = figures[i].upper()
        return board

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
                fig = fig.upper()

            self.board[8 - last.y][8 - last.x] = '•'
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
                    self.board[i][j] = '•'
                elif '^' in self.board[i][j]:
                    self.board[i][j] = self.board[i][j].replace('^', '')







