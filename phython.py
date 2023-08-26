import pygame
import random

# Define the screen size and title
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snake"

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the snake's starting position and size
SNAKE_STARTING_POSITION = (100, 100)
SNAKE_SIZE = 10

# Define the snake's speed
SNAKE_SPEED = 10

# Define the food's starting position and size
FOOD_STARTING_POSITION = (200, 200)
FOOD_SIZE = 10

# Define the game's state
GAME_STATE_RUNNING = 0
GAME_STATE_OVER = 1

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)
clock = pygame.time.Clock()

# Create the snake
snake = pygame.Rect(SNAKE_STARTING_POSITION, (SNAKE_SIZE, SNAKE_SIZE))

# Create the food
food = pygame.Rect(FOOD_STARTING_POSITION, (FOOD_SIZE, FOOD_SIZE))

# Set the game state to running
game_state = GAME_STATE_RUNNING

# Main game loop
while game_state == GAME_STATE_RUNNING:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = GAME_STATE_OVER
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.move_ip(0, -SNAKE_SPEED)
            elif event.key == pygame.K_DOWN:
                snake.move_ip(0, SNAKE_SPEED)
            elif event.key == pygame.K_LEFT:
                snake