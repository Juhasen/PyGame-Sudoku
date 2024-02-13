import pygame


def track_mouse(screen):
    mouse_pos = pygame.mouse.get_pos()
    if 50 < mouse_pos[0] < 500 and 50 < mouse_pos[1] < 500:
        row = (mouse_pos[1] - 50) // 50
        col = (mouse_pos[0] - 50) // 50
        return row, col
    return None


def handle_click(screen, board):
        pos = track_mouse(screen)
        #clear previous position
        pygame.draw.rect(screen, (211, 211, 211), (550, 380, 400, 100))
        text = []
        if pos:
            row, col = pos
            row += 1
            col += 1
            pos = (row, col)
            font = pygame.font.Font(None, 36)
            text = font.render(str(pos), True, (0, 0, 0))
            screen.blit(text, (670, 380))
        elif pos is None:
            font = pygame.font.Font(None, 25)
            text = font.render("Out of the bounds", True, (0, 0, 0))
            screen.blit(text, (550, 380))
        if pos:
            row -= 1
            col -= 1
            pos = (row, col)
        return pos

