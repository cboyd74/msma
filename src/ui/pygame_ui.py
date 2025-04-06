import pygame
import sys

# Initialize Pygame
pygame.init()

# Fullscreen window setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
pygame.display.set_caption("Music Theory Program")

# Colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font_large = pygame.font.SysFont(None, 72)
font_medium = pygame.font.SysFont(None, 48)

# List of available keys
keys = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']

# Define button properties
button_width = 80
button_height = 40
button_margin = 10


# Function to draw fretboard
def draw_fretboard():
    # Fretboard properties
    fretboard_x = 100
    fretboard_y = 150
    fretboard_width = 600
    fretboard_height = 200
    num_strings = 6
    num_frets = 23

    # Draw fretboard (simplified)
    for string in range(num_strings):
        pygame.draw.line(screen, BLACK, (fretboard_x, fretboard_y + string * 30),
                         (fretboard_x + fretboard_width, fretboard_y + string * 30), 3)

    for fret in range(num_frets):
        pygame.draw.line(screen, BLACK, (fretboard_x + fret * 25, fretboard_y),
                         (fretboard_x + fret * 25, fretboard_y + num_strings * 30), 3)

    # Draw dots on the 12th fret
    pygame.draw.circle(screen, BLACK, (fretboard_x + 12 * 25, fretboard_y + 30), 8)  # 12th fret dots
    pygame.draw.circle(screen, BLACK, (fretboard_x + 12 * 25, fretboard_y + 60), 8)
    pygame.draw.circle(screen, BLACK, (fretboard_x + 12 * 25, fretboard_y + 90), 8)
    pygame.draw.circle(screen, BLACK, (fretboard_x + 12 * 25, fretboard_y + 120), 8)
    pygame.draw.circle(screen, BLACK, (fretboard_x + 12 * 25, fretboard_y + 150), 8)
    pygame.draw.circle(screen, BLACK, (fretboard_x + 12 * 25, fretboard_y + 180), 8)


# Function to draw buttons across the top
def draw_buttons():
    x = button_margin
    y = 50  # Vertical position for buttons

    for key in keys:
        pygame.draw.rect(screen, BLACK, (x, y, button_width, button_height))  # Button rectangle
        text = font_medium.render(key, True, WHITE)  # Key name text
        text_rect = text.get_rect(center=(x + button_width // 2, y + button_height // 2))  # Center text
        screen.blit(text, text_rect)
        x += button_width + button_margin  # Move x position for next button


# Main loop update
def main():
    clock = pygame.time.Clock()
    running = True
    selected_key = None
    page = 1  # 1 = Home page, 2 = Second page

    while running:
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    page = 2  # Go to the second page when space is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button was clicked on the second page
                if page == 2:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 50 <= mouse_y <= 90:  # Button height range
                        for i, key in enumerate(keys):
                            button_x = button_margin + i * (button_width + button_margin)
                            if button_x <= mouse_x <= button_x + button_width:
                                selected_key = key
                                print(f"Selected key: {selected_key}")

        if page == 1:
            # Draw title and subtitle on the home page
            title_text = font_large.render("MSMA", True, BLACK)
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
            screen.blit(title_text, title_rect)

            subtitle_text = font_medium.render("Press Space to Explore", True, BLACK)
            subtitle_rect = subtitle_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(subtitle_text, subtitle_rect)

        elif page == 2:
            # Draw fretboard and buttons on the second page
            draw_fretboard()
            draw_buttons()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
