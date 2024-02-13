import pygame


def track_mouse(screen):
    # if the button is  clicked then select the cell and
    # change the value of it based on the number clicked
    mouse_pos = pygame.mouse.get_pos()
    if 50 < mouse_pos[0] < 500 and 50 < mouse_pos[1] < 500:
        row = (mouse_pos[1] - 50) // 50
        col = (mouse_pos[0] - 50) // 50
        pygame.draw.arc(screen, (255, 0, 0), (55 + col * 50, 55 + row * 50, 42, 42), 0, 6.28, 1)
        return row, col
    return None
