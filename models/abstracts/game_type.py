from abc import ABCMeta, abstractmethod
from ..game_state import GameState
from ..board import Board
from ..handle_turns import HandleTurns
from ..game_display import GameDisplay
from ..human_player import HumanPlayer
import copy

class GameType(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        self.board = Board()
        self.gameState = GameState()
        self.handleTurns = HandleTurns()
        self.playerOne = None
        self.playerTwo = None

    def play(self):
        self.set_up()
        GameDisplay.show(self.board)
        self.start()
        GameDisplay.show(self.board)
        GameDisplay.game_over()

    def start(self):
       while not self.gameState.finished(self.board):
           if(self.handleTurns.currentPlayerToken == self.playerOne.token):
             self.handle_play(self.playerOne)
           else:
             self.handle_play(self.playerTwo)
       self.end_game()

    def handle_play(self, player):
        if( isinstance(player, HumanPlayer) ):
             try_spot = GameDisplay.get_player_spot(GameDisplay, self.board.get_available_spots())
             spot = copy.deepcopy(try_spot)
             player.play(self.board, spot)
             GameDisplay.chosen_spot(player.token, spot)
        else:
             spot = player.play(self.board)
             GameDisplay.chosen_spot(player.token, spot)
        GameDisplay.show(self.board)
        self.handleTurns.change()

    def set_up(self):
        self.handleTurns.currentPlayerToken = GameDisplay.get_first_player(GameDisplay)
        self.set_tokens()

    def set_tokens(self):
      while self.playerTwo.token == None:
          self.playerOne.set_token(self.handleTurns.currentPlayerToken)
          self.playerTwo.auto_token(self.playerOne.token)

    def end_game(self):
        if (self.gameState.check_win(self.board)[0]):
         winnerToken = self.gameState.check_win(self.board)[1][0]
         GameDisplay.winner(winnerToken)
        elif (self.gameState.finished(self.board)):
         GameDisplay.tie()
