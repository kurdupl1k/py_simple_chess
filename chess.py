import pygame

class Piece:
  pieces = {
    'black': {
      'pawn':   '00', 'rook':   '01',
      'knight': '02', 'bishop': '03',
      'queen':  '04', 'king':   '05'
    },
    'white': {
      'pawn':   '10', 'rook':   '11',
      'knight': '12', 'bishop': '13',
      'queen':  '14', 'king':   '15'
    }
  }

  def __init__(self, y, x, value):
    self.y, self.x = y, x
    self.color = 'white' if value[0] == '0' else 'black'
    self.name = ''
    for x in Piece.pieces[self.color]:
      if Piece.pieces[self.color][x] == value:
        self.name = x




class Chess:
  def __init__(self):
    pygame.display.set_caption('Chess game')
      
    self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 640, 640
    self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    
    self.__init_background()

    self.field = [[' ' for y in range(8)] for x in range(8)]
    self.__init_pieces()

    self.pieces = { 'black': [], 'white': [] }

    for y in range(2):
      for x in range(8):
        self.pieces['black'].append(Piece(y, x, self.field[y][x]))

    for y in range(6, 8):
      for x in range(8):
        self.pieces['white'].append(Piece(y, x, self.field[y][x]))

    print()

    for x in self.field:
      print(x)

  def __init_pieces(self):
    self.field[0][0], self.field[0][7] = '11', '01'
    self.field[7][0], self.field[7][7] = '11', '01'
    self.field[0][1], self.field[0][6] = '12', '02'
    self.field[7][1], self.field[7][6] = '12', '02'
    self.field[0][2], self.field[0][5] = '13', '03'
    self.field[7][2], self.field[7][5] = '13', '03'
    self.field[0][4], self.field[7][4] = '14', '04'
    self.field[0][3], self.field[7][3] = '15', '05'
    
    for x in range(8):
      self.field[1][x], self.field[6][x] = '10', '00'

  def __init_background(self):
    self.background = pygame.image.load('sprites/board.png')    
  
  def __set_sprites(self):
    all_pieces_list = pygame.sprite.Group()

    

  def __log(self):
    pass
  
  def loop(self):
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
      
      surf = pygame.Surface((80, 80))
      surf.fill((0, 255 ,0))

      surf.set_alpha(100)
      
      self.screen.blit(self.background, (0, 0))
  

def main():
  pygame.init()

  game = Chess()
  game.loop()

  pygame.quit() 


if __name__ == '__main__':
  main()
