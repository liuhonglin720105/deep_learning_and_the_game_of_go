# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 11:00:41 2023

@author: liu honglin
"""

from dlgo import agent
from dlgo import goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move, point_from_coords
#import time

def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bot =agent.RandomBot()
    
    while not game.is_over():
        #time.sleep(0.3)
        
        print(chr(27) + "[2J")
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('__')
            point = point_from_coords(human_move.strip())
            move = goboard.Move.play(point)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)



if __name__ == '__main__':
    main()              
                  