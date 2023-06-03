import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coin Collector")

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

player_width = 50
player_height = 50
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height
player_speed = 5
player_image = pygame.Surface((player_width, player_height))
player_image.fill(green)

coin_width = 20
coin_height = 20
coin_speed = 3
coin_image = pygame.Surface((coin_width, coin_height))
coin_image.fill(yellow)
coins = []
for i in range(10):
    coin_x = random.randint(0, screen_width - coin_width)
    coin_y = random.randint(0, screen_height / 2)
    coins.append([coin_x, coin_y])

obstacle_width = 100
obstacle_height = 20
obstacle_speed = 1
obstacle_image = pygame.Surface((obstacle_width, obstacle_height))
obstacle_image.fill(red)
obstacles = []
for i in range(5):
    obstacle_x = random.randint(0, screen_width - obstacle_width)
    obstacle_y = random.randint(screen_height / 4, screen_height - player_height)
    obstacles.append([obstacle_x, obstacle_y])

game_over = False
score = 0

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the coins
    for i in range(len(coins)):
        coins[i][1] += coin_speed
        if coins[i][1] > screen_height:
            coins[i][0] = random.randint(0, screen_width - coin_width)
            coins[i][1] = random.randint(0, screen_height / 2)
        if player_x < coins[i][0] + coin_width and player_x + player_width > coins[i][0] and player_y < coins[i][1] + coin_height and player_y + player_height > coins[i][1]:
            coins[i][0] = random.randint(0, screen_width - coin_width)
            coins[i][1] = random.randint(0, screen_height / 2)
            score += 1

    # Move the obstacles and check for collision with player
    for i in range(len(obstacles)):
        obstacles[i][1] += obstacle_speed
        if obstacles[i][1] > screen_height:
            obstacles[i][0] = random.randint(0, screen_width - obstacle_width)
            obstacles[i][1] = random.randint(screen_height / 2, screen_height - obstacle_height)
        if player_x < obstacles[i][0] + obstacle_width and player_x + player_width > obstacles[i][0] and player_y < obstacles[i][1] + obstacle_height and player_y + player_height > obstacles[i][1]:
            game_over = True
    
    # Fill the screen with white color
    screen.fill(white)

    # Draw the player
    screen.blit(player_image, (player_x, player_y))

    # Draw the coins
    for coin in coins:
        screen.blit(coin_image, coin)

    # Draw the obstacles
    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)

    # Draw the score on the screen
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
pygame.quit()
quit()