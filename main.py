import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тир")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# Класс мишени
class Target:
    def __init__(self):
        self.radius = 30
        self.generate_new_position()

    def generate_new_position(self):
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (self.x, self.y), self.radius)
        pygame.draw.circle(surface, WHITE, (self.x, self.y), self.radius, 3)


# Инициализация игры
target = Target()
score = 0
game_active = True
start_time = pygame.time.get_ticks()
game_duration = 30000  # 30 секунд в миллисекундах

# Шрифты
font = pygame.font.Font(None, 36)


def check_click(pos):
    global score
    distance = ((pos[0] - target.x) ** 2 + (pos[1] - target.y) ** 2) ** 0.5
    if distance <= target.radius:
        score += 1
        target.generate_new_position()


def draw_text(text, position, color=WHITE):
    text_surface = font.render(text, True, color)
    window.blit(text_surface, position)


# Главный цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and game_active:
            check_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_active:
                # Рестарт игры
                game_active = True
                score = 0
                start_time = pygame.time.get_ticks()
                target.generate_new_position()

    # Обновление времени
    current_time = pygame.time.get_ticks()
    time_left = max(0, game_duration - (current_time - start_time))

    if time_left <= 0 and game_active:
        game_active = False

    # Отрисовка
    window.fill(BLACK)

    if game_active:
        target.draw(window)
        # Отображение таймера
        draw_text(f"Time: {time_left // 1000}", (10, 10))
        # Отображение счета
        draw_text(f"Score: {score}", (10, 50))
    else:
        # Экран завершения игры
        draw_text("Game Over!", (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        draw_text(f"Final Score: {score}", (WIDTH // 2 - 120, HEIGHT // 2))
        draw_text("Press SPACE to restart", (WIDTH // 2 - 150, HEIGHT // 2 + 50))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

import telebot

# Замените 'YOUR_BOT_TOKEN' на токен, полученный от @BotFather
TOKEN = '7573968967:AAGMW0Q3EqZHLvCIjCU4oh6EeqOXTtZfN5M'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик для всех типов сообщений
@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    response = "Этот бот лежит на локальном сервере с автозапуском"
    bot.reply_to(message, response)

if __name__ == '__main__':
    print('Бот запущен...')
    bot.polling(none_stop=True)

