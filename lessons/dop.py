import pygame
import socket
import threading
import random
import pickle

# Инициализация Pygame
pygame.init()

# Константы для игры
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
FONT = pygame.font.Font(None, 36)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Базовый класс Hero
class Hero:
    def __init__(self, name):
        self.name = name
        self.choice = None  # Выбор игрока ("rock", "paper", "scissors")

    def make_choice(self, choice):
        """Выбор действия героем."""
        self.choice = choice

    def battle(self, other):
        """Определяет победителя между двумя героями."""
        if self.choice == other.choice:
            return "draw"
        if (self.choice == "rock" and other.choice == "scissors") or \
           (self.choice == "scissors" and other.choice == "paper") or \
           (self.choice == "paper" and other.choice == "rock"):
            return "win"
        return "lose"

# Классы-наследники Hero
class Warrior(Hero):
    pass

class Mage(Hero):
    pass

class Archer(Hero):
    pass

# Игровой клиент
class GameClient:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.hero = None
        self.running = True

    def send_data(self, data):
        """Отправляет данные на сервер."""
        self.socket.sendall(pickle.dumps(data))

    def receive_data(self):
        """Получает данные от сервера."""
        data = self.socket.recv(1024)
        return pickle.loads(data)

    def main_loop(self):
        """Главный игровой цикл клиента."""
        global SCREEN_WIDTH, SCREEN_HEIGHT
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hero Game")
        clock = pygame.time.Clock()

        while self.running:
            screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Выбор действий игрока
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.hero.make_choice("rock")
                        self.send_data({"action": "choice", "choice": "rock"})
                    elif event.key == pygame.K_p:
                        self.hero.make_choice("paper")
                        self.send_data({"action": "choice", "choice": "paper"})
                    elif event.key == pygame.K_s:
                        self.hero.make_choice("scissors")
                        self.send_data({"action": "choice", "choice": "scissors"})

            # Обновление экрана
            text = FONT.render(f"Your Hero: {self.hero.name}", True, BLACK)
            screen.blit(text, (10, 10))

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

# Сервер игры
class GameServer:
    def __init__(self, host, port, max_players=2):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(max_players)
        self.players = []
        self.max_players = max_players
        self.running = True

    def handle_client(self, conn, addr):
        """Обрабатывает подключение клиента."""
        print(f"Player connected from {addr}")
        player_data = pickle.loads(conn.recv(1024))
        self.players.append(player_data)

        while self.running:
            data = conn.recv(1024)
            if data:
                message = pickle.loads(data)
                print(f"Received from {addr}: {message}")
                # Логика обработки действий игроков

        conn.close()

    def run(self):
        """Запуск сервера."""
        print("Server started. Waiting for players...")
        while len(self.players) < self.max_players:
            conn, addr = self.socket.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

        print("All players connected. Starting game!")
        # Игровая логика (например, сражения между игроками)

# Запуск клиента или сервера
if __name__ == "__main__":
    mode = input("Start as (server/client): ").strip().lower()
    if mode == "server":
        server = GameServer("localhost", 5555)
        server.run()
    elif mode == "client":
        name = input("Enter your hero name: ")
        hero_class = input("Choose your class (warrior/mage/archer): ").strip().lower()

        if hero_class == "warrior":
            hero = Warrior(name)
        elif hero_class == "mage":
            hero = Mage(name)
        elif hero_class == "archer":
            hero = Archer(name)
        else:
            print("Invalid class. Defaulting to Warrior.")
            hero = Warrior(name)

        client = GameClient("localhost", 5555)
        client.hero = hero
        client.main_loop()
