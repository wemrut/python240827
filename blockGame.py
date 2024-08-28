import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록 깨기 게임")

# 색상 설정
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# 공 설정
ball_width = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_dx = 3 * random.choice((1, -1))
ball_dy = 3 * random.choice((1, -1))

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - 30
paddle_dx = 0
paddle_speed = 6

# 블록 설정
block_width = 75
block_height = 20
blocks = []
for i in range(5):
    for j in range(8):
        block_x = j * (block_width + 10) + 35
        block_y = i * (block_height + 10) + 50
        blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(black)
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_dx = -paddle_speed
            if event.key == pygame.K_RIGHT:
                paddle_dx = paddle_speed
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                paddle_dx = 0

    # 패들 이동
    paddle_x += paddle_dx
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > screen_width - paddle_width:
        paddle_x = screen_width - paddle_width

    # 공 이동
    ball_x += ball_dx
    ball_y += ball_dy

    # 공이 벽에 부딪히면 방향 전환
    if ball_x <= 0 or ball_x >= screen_width - ball_width:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy
    if ball_y >= screen_height:
        # 공이 화면 아래로 떨어지면 게임 오버
        print("게임 오버!")
        running = False

    # 공이 패들에 부딪히면 방향 전환
    if paddle_y < ball_y + ball_width < paddle_y + paddle_height and \
       paddle_x < ball_x + ball_width // 2 < paddle_x + paddle_width:
        ball_dy = -ball_dy

    # 블록 충돌 처리
    for block in blocks[:]:
        if block.collidepoint(ball_x + ball_width // 2, ball_y + ball_width // 2):
            ball_dy = -ball_dy
            blocks.remove(block)
            break

    # 패들 그리기
    paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, white, paddle)

    # 공 그리기
    pygame.draw.ellipse(screen, red, (ball_x, ball_y, ball_width, ball_width))

    # 블록 그리기
    for block in blocks:
        pygame.draw.rect(screen, blue, block)

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()
