import pygame
import sys
import random

WIDTH = 750
HEIGHT = 550


def draw_board(screen):
    # Draw the grid lines
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 5)
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 5)
        else:
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500))
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i))


def generate_numbers(screen):
    board = [[0 for i in range(9)] for j in range(9)]
    font = pygame.font.Font(None, 36)
    counter = random.randint(25, 27)
    for i in range(counter):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            continue
        num = random.randint(1, 9)
        board[row][col] = num

        #TODO: VALIDATE THE BOARD

        font = pygame.font.Font(None, 36)
        text = font.render(str(num), True, (0, 0, 0))
        screen.blit(text, (70 + col * 50, 65 + row * 50))


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

    # make a green background
    screen.fill((211, 211, 211))

    draw_board(screen)

    generate_numbers(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
