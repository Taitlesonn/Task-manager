import pygame


pygame.init()

# Kolory
BLUE = (63, 132, 242)
LIGHT_BLUE = (92, 145, 230)
WHITE = (255, 255, 255)

# Font i rozmiar tekstu
font = pygame.font.Font(None, 36)

def draw_button(screen, color, x, y, width, height, text):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(width, height))
    screen.blit(text_surface, text_rect)

def Gmain(szerokosc: int, wysokosc: int):
    screen = pygame.display.set_mode((szerokosc, wysokosc))
    pygame.display.set_caption("Przykład przycisku w Pygame")
    running = True  # Zmieniona nazwa na 'running'

    while running:
        screen.fill((0, 0, 0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_color = LIGHT_BLUE if pygame.Rect(250, 200, 140, 60).collidepoint(mouse_x, mouse_y) else BLUE
        draw_button(screen, button_color, 250, 200, 140, 60, "Add an event")

        for zdarzenia in pygame.event.get():
            if zdarzenia.type == pygame.QUIT:
                running = False
            if zdarzenia.type == pygame.MOUSEBUTTONDOWN:  # Poprawiona nazwa zmiennej
                button_rect = pygame.Rect(250, 200, 140, 60)
                if button_rect.collidepoint(mouse_x, mouse_y):
                    print("Przycisk został kliknięty!")

        pygame.display.update()

    pygame.quit()  # Przeniesione poza pętlę

# Uruchomienie funkcji Gmain
Gmain(700, 700)
