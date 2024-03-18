from random import choice, randint

import pygame

# Инициализация PyGame:
pygame.init()

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()

# Центр поля:
BOARD_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


class GameObject:
    """Основной класс."""

    def __init__(self, body_color=screen, position=BOARD_CENTER):
        self.position = position
        self.body_color = body_color

    def draw(self):
        """Заглушка, метод будет определён в потомках"""
        raise NotImplementedError(f'Определите Draw {type(self).__name__}')


class Apple(GameObject):
    """Класс, созданный для описания яблока."""

    def __init__(self, body_color=APPLE_COLOR) -> None:
        super().__init__(body_color)
        self.randomize_position()

    def randomize_position(self):
        """Устанавливаем случайную позицию для яблока."""
        self.position = (
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        )

    def draw(self):
        """Метод для отрисовки яблока."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Описываем змейку."""

    def __init__(self):
        self.body_color = SNAKE_COLOR
        self.length = 1
        self.position = BOARD_CENTER
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None

    def draw(self):
        """Отрисовка змейки."""
        for position in self.positions:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def update_direction(self):
        """Обновление направления после нажатия."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Движение змейки."""
        head_position1, head_position2 = self.get_head_position()
        dx, dy = self.direction
        new_position = (
            ((head_position1 + GRID_SIZE * dx) % SCREEN_WIDTH),
            ((head_position2 + GRID_SIZE * dy) % SCREEN_HEIGHT)
        )

        if new_position in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new_position)

        if len(self.positions) > self.length:
            self.last = self.positions.pop()

    def get_head_position(self):
        """Узнаем где голова."""
        return self.positions[0]

    def reset(self):
        """Обнуляем змейку."""
        self.length = 1
        screen.fill(BOARD_BACKGROUND_COLOR)
        self.positions = [BOARD_CENTER]
        self.direction = choice([UP, DOWN, LEFT, RIGHT])


def handle_keys(game_object):
    """Обработка действий пользователя."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Описывем основную логику игры."""
    apple = Apple()
    snake = Snake()

    spawning_apple = apple.randomize_position()

    if spawning_apple in snake.positions:
        spawning_apple = apple.randomize_position()

    while True:
        clock.tick(SPEED)

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()

        pygame.display.update()
        handle_keys(snake)
        snake.draw()
        apple.draw()
        snake.move()
        snake.update_direction()


if __name__ == '__main__':
    main()
