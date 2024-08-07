import pygame
import sys
import random

# Inicialización de pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mi Juego")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)  # Color para el tercer nivel

# Reloj para controlar el frame rate
clock = pygame.time.Clock()

# Clase para el enemigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, color, horizontal_speed, vertical_speed):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = random.choice([-1, 1])
        self.horizontal_speed = horizontal_speed
        self.vertical_speed = vertical_speed

    def update(self):
        # Movimiento lateral
        self.rect.x += self.move_direction * self.horizontal_speed
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.move_direction *= -1

        # Movimiento hacia abajo
        self.rect.y += self.vertical_speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()  # Elimina al enemigo si sale de la pantalla

# Clase para el jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - 60
        self.bullets = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        
        # Limitar el movimiento del jugador dentro de la pantalla
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width
        
        # Disparar proyectiles
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.add(bullet)

# Clase para los proyectiles
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

# Función para mostrar la pantalla de "Perdiste"
def show_game_over():
    font = pygame.font.SysFont(None, 50)
    text = font.render("Perdiste", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    retry_text = font.render("Presiona R para reintentar o Q para salir", True, BLACK)
    retry_rect = retry_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
        screen.fill(WHITE)
        screen.blit(text, text_rect)
        screen.blit(retry_text, retry_rect)
        pygame.display.flip()
        clock.tick(60)

# Función para mostrar la pantalla de victoria
def show_victory_screen():
    font = pygame.font.SysFont(None, 50)
    text = font.render("Ganaste, Crack!", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    retry_text = font.render("Presiona R para volver al principio o Q para salir", True, BLACK)
    retry_rect = retry_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
        screen.fill(WHITE)
        screen.blit(text, text_rect)
        screen.blit(retry_text, retry_rect)
        pygame.display.flip()
        clock.tick(60)

# Función para manejar el juego
def play_game(level=1):
    enemies = pygame.sprite.Group()
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    # Configuración de los enemigos según el nivel
    if level == 1:
        enemy_color = RED
        enemy_horizontal_speed = 3
        enemy_vertical_speed = 1
        num_enemies = 5
    elif level == 2:
        enemy_color = BLUE
        enemy_horizontal_speed = 5
        enemy_vertical_speed = 2
        num_enemies = 10
    elif level == 3:
        enemy_color = GREEN
        enemy_horizontal_speed = 7
        enemy_vertical_speed = 3
        num_enemies = 15

    for i in range(num_enemies):
        # Ajustes para evitar que los enemigos se generen fuera de la pantalla
        x_position = random.randint(0, SCREEN_WIDTH - 50)  # Genera una posición x aleatoria dentro de la pantalla
        y_position = random.randint(0, SCREEN_HEIGHT // 2 - 50)  # Genera una posición y aleatoria en la mitad superior de la pantalla
        enemy = Enemy(x_position, y_position, enemy_color, enemy_horizontal_speed, enemy_vertical_speed)
        enemies.add(enemy)
        all_sprites.add(enemy)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Actualizar todos los sprites
        all_sprites.update()
        player.bullets.update()

        # Detectar colisiones entre balas y enemigos
        collisions = pygame.sprite.groupcollide(enemies, player.bullets, True, True)
        
        # Detectar colisiones entre enemigos y el jugador
        if pygame.sprite.spritecollideany(player, enemies):
            show_game_over()
            return  # Regresar al menú principal después de mostrar el mensaje de "Perdiste"

        # Verificar si todos los enemigos han sido eliminados
        if len(enemies) == 0:
            if level == 1:
                play_game(level=2)  # Cambiar al segundo nivel
                return
            elif level == 2:
                play_game(level=3)  # Cambiar al tercer nivel
                return
            elif level == 3:
                if show_victory_screen():
                    return  # Volver al menú principal después de mostrar el mensaje de victoria

        # Verificar si algún enemigo ha llegado al fondo de la pantalla
        if any(enemy.rect.y >= SCREEN_HEIGHT for enemy in enemies):
            show_game_over()
            return

        screen.fill(WHITE)
        all_sprites.draw(screen)
        player.bullets.draw(screen)
        pygame.display.flip()
        clock.tick(60)

# Función para dibujar el menú de selección de niveles
def draw_level_selection_menu():
    font = pygame.font.SysFont(None, 55)
    text = font.render("Selecciona un nivel (1, 2 o 3)", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2 - 100))
    
    level_texts = ["Nivel 1", "Nivel 2", "Nivel 3"]
    for i, level_text in enumerate(level_texts):
        level_text_surface = font.render(level_text, True, BLACK)
        screen.blit(level_text_surface, (SCREEN_WIDTH // 2 - level_text_surface.get_width() // 2, SCREEN_HEIGHT // 2 - level_text_surface.get_height() // 2 + i * 60))
    
    # Botón de Salir
    exit_button = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 150, 150, 50)
    pygame.draw.rect(screen, BLACK, exit_button)
    exit_text = font.render("Salir", True, WHITE)
    screen.blit(exit_text, (exit_button.centerx - exit_text.get_width() // 2, exit_button.centery - exit_text.get_height() // 2))

    return exit_button

# Bucle principal
def main():
    selected_level = None
    
    while selected_level is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_level = 1
                elif event.key == pygame.K_2:
                    selected_level = 2
                elif event.key == pygame.K_3:
                    selected_level = 3
            
        screen.fill(WHITE)
        exit_button = draw_level_selection_menu()
        pygame.display.flip()

        # Manejar clic en el botón de salir
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if exit_button.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()
                
    # Comenzar el juego con el nivel seleccionado
    play_game(selected_level)

if __name__ == "__main__":
    main()
