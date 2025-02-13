import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Get the screen dimensions
infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Matrix Rain")

# Define the font
font_size = 12
font = pygame.font.SysFont('Consolas', font_size)

# Create a list of katakana characters
katakana = [chr(i) for i in range(0x30A0, 0x30FF)]
characters = katakana + [str(i) for i in range(10)]  # Include numbers

# Define columns
columns = int(screen_width / font_size)
drops = [12] * columns

# Colors
black = (0, 0, 0)
green = (0, 255, 70)

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Fill the screen with a transparent black rectangle to create the trail effect
    screen.fill((0, 0, 0, 10))

    # Draw the characters
    for i in range(len(drops)):
        char = random.choice(characters)
        char_surface = font.render(char, True, green)
        x = i * font_size
        y = drops[i] * font_size

        # Blit the character to the screen
        screen.blit(char_surface, (x, y))

        # Update the drop position
        if y > screen_height or random.random() > 0.95:
            drops[i] = 0
        drops[i] += 1

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
