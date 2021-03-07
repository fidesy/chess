from pieces import *



class Game:
    def __init__(self):
        self.count = 1
        self.color_ = 'white'
        self.pawns = [Pawn(Place('A', '2'), 'white'),
                      Pawn(Place('B', '2'), 'white'),
                      Pawn(Place('C', '2'), 'white'),
                      Pawn(Place('D', '2'), 'white'),
                      Pawn(Place('E', '2'), 'white'),
                      Pawn(Place('F', '2'), 'white'),
                      Pawn(Place('G', '2'), 'white'),
                      Pawn(Place('H', '2'), 'white'),
                      Pawn(Place('A', '7'), 'black'),
                      Pawn(Place('B', '7'), 'black'),
                      Pawn(Place('C', '7'), 'black'),
                      Pawn(Place('D', '7'), 'black'),
                      Pawn(Place('E', '7'), 'black'),
                      Pawn(Place('F', '7'), 'black'),
                      Pawn(Place('G', '7'), 'black'),
                      Pawn(Place('H', '7'), 'black')]
        self.knights = [Knight(Place('B', '1'), 'white'),
                        Knight(Place('G', '1'), 'white'),
                        Knight(Place('B', '8'), 'black'),
                        Knight(Place('G', '8'), 'black')]
        self.bishops = [Bishop(Place('C', '1'), 'white'),
                        Bishop(Place('F', '1'), 'white'),
                        Bishop(Place('C', '8'), 'black'),
                        Bishop(Place('F', '8'), 'black')]
        self.kings = [King(Place('E', '1'), 'white'),
                      King(Place('E', '8'), 'black')]
        self.queens = [Queen(Place('D', '1'), 'white'),
                       Queen(Place('D', '8'), 'black')]
        self.rooks = [Rook(Place('A', '1'), 'white'),
                      Rook(Place('H', '1'), 'white'),
                      Rook(Place('A', '8'), 'black'),
                      Rook(Place('H', '8'), 'black')]

        self.figures = []
        self.figures.append(self.pawns)
        self.figures.append(self.knights)
        self.figures.append(self.bishops)
        self.figures.append(self.rooks)
        self.figures.append(self.queens)
        self.figures.append(self.kings)

    def get_piece(self):
        print(end='\n')
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
                new_coord = input('Введите координаты для хода: ')
                new_coord = Place(new_coord[0].upper(), new_coord[1])
                state = current_piece.move(new_coord)
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




# if __name__ == '__main__':
game = Game()
while True:
    game.move()







