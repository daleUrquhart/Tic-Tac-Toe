'''
Brian Yu, David Malan (2022-11-05) runner.py (0) [python file]. https://cs50.harvard.edu/ai/2020/weeks/1/.
'''
import pygame
import sys
import time
import tictactoe as ttt

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

import os, sys
ttf_path = os.path.join(sys.path[0], "OpenSans-Regular.ttf")

mediumFont = pygame.font.Font(ttf_path, 28)
largeFont = pygame.font.Font(ttf_path, 40)
moveFont = pygame.font.Font(ttf_path, 60)

user = None
game = ttt.Minimax()
board = game.board
ai_turn = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Let user choose a player. Proceeds to else afterwards
    if user is None:

        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw buttons
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("Play as X", True, black)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playO = mediumFont.render("Play as O", True, black)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = game.X
                AI = game.O
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = game.O
                AI = game.X
        
    else:
        game.AI = AI
        game.user = user
        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != None:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = game.utility(board)
        player = game.player(board)
        # Show title
        if game_over != None:
            winner = game.winner(board)
            if winner is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player:
            title = f"Play as {user}"
        else:
            title = f"Computer thinking..."
        
        # Decorating
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move
        if player == AI and not game_over:
            if ai_turn:
                time.sleep(0.5)
                
                # If it aint broke, dont fix it...
                test = (tuple(board[0]), tuple(board[1]), tuple(board[2]))
                move = game.minimax(test)

                if game.utility(board) == None:
                    board = game.result(board, move) 
                    
                ai_turn = False
            else:
                ai_turn = True
                                                                                                                                                                                                                                
        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed()
        if user == player and not game_over and click == 1:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == None and tiles[i][j].collidepoint(mouse)):
                        board = game.result(board, (i, j))
                        if game.utility(board) != None:
                            game_over = True
                        player = AI
        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    game = ttt.Minimax()
                    board = game.board
                    ai_turn = False

    pygame.display.flip()
