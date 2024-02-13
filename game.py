import pygame
import sys
import random

WIDTH = 750
HEIGHT = 550


def validate_number(board, row, col, num):
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check the 3x3 grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True


def draw_board(screen):
    # Draw the grid lines
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 5)
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 5)
        else:
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500))
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i))

    # draw the numbers above the grid
    font = pygame.font.Font(None, 36)
    for i in range(9):
        text = font.render(str(i + 1), True, (0, 0, 0))
        screen.blit(text, (70 + i * 50, 20))
        screen.blit(text, (20, 65 + i * 50))


def draw_numbers(screen, board):
    font = pygame.font.Font(None, 36)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, (0, 0, 0))
                screen.blit(text, (70 + j * 50, 65 + i * 50))


def generate_numbers(screen, board):
    counter = random.randint(50, 65)
    for i in range(counter):
        found = False
        while not found:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)
            if validate_number(board, row, col, num) and board[row][col] == 0:
                board[row][col] = num
                found = True


def track_mouse(screen):
    mouse_pos = pygame.mouse.get_pos()
    if 50 < mouse_pos[0] < 500 and 50 < mouse_pos[1] < 500:
        row = (mouse_pos[1] - 50) // 50
        col = (mouse_pos[0] - 50) // 50
        pygame.draw.arc(screen, (255, 0, 0), (55 + col * 50, 55 + row * 50, 42, 42), 0, 6.28, 1)
        return row, col
    return None


if __name__ == "__main__":
    pygame.init()
    pygame.display.init()
    if pygame.display.get_init() == 0:
        pygame.error("Display not initialized")
        pygame.quit()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    pygame.display.set_caption("Sudoku")

    screen.fill((211, 211, 211))

    board = [[0 for i in range(9)] for j in range(9)]

    draw_board(screen)
    generate_numbers(screen, board)
    draw_numbers(screen, board)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #if the button is  clicked then select the cell and change the value of it based on the number clicked
        track_mouse(screen) #change the working of the track func

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
