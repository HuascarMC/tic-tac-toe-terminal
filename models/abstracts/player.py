from abc import ABCMeta, abstractmethod

class Player(metaclass=ABCMeta):
    
 @abstractmethod
 def __init__(self):
     self.token = None

 @abstractmethod
 def play(self, board, spot):
     raise NotImplementedError

 def set_token(self, token):
     self.token = token

 def auto_token(self, opponents_token):
     if(opponents_token == 'X'):
        self.set_token('O')
     else:
        self.set_token('X')
