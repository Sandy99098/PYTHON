import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow()

    def move(self):
        head = self.body[0]
        x, y = head[0] + self.direction[0], head[1] + self.direction[1]
        self.body.insert(0, (x, y))
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        x, y = tail[0] + self.direction[0], tail[1] + self.direction[1]
        self.body.append((x, y))

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def collide(self):
        head = self.body[0]
        return head in self.body[1:]

# Food class
class Food:
    def __init__(self):
        self.position = self.new_position()

    def new_position(self):
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main function
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    running = True

    # Tiled background
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.rect(screen, (230, 230, 230) if (x // CELL_SIZE + y // CELL_SIZE) % 2 == 0 else (200, 200, 200), (x, y, CELL_SIZE, CELL_SIZE))

    # Double rectangular border
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT), 3)
    pygame.draw.rect(screen, WHITE, (3, 3, WIDTH - 6, HEIGHT - 6), 3)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        if snake.body[0] == food.position:
            snake.grow()
            food.position = food.new_position()

        screen.fill(BLACK)

        snake.move()
        if snake.collide() or snake.body[0][0] < 0 or snake.body[0][0] >= GRID_WIDTH or snake.body[0][1] < 0 or snake.body[0][1] >= GRID_HEIGHT:
            running = False

        snake.draw()
        food.draw()

        pygame.display.flip()
        clock.tick(3)  # Adjust the tick rate here for slower movement

    pygame.quit()

if __name__ == "__main__":
    main()

