from pygame import *
from random import randint

WIDTH = 600
HEIGHT = 500
FPS = 60
WIN_SCORE = 3

def generate_color():
    return(randint(0, 255), randint(0, 255), randint(0, 255))

background = generate_color()
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('ping-pong')
clock = time.Clock()

class GameSprite():
    def __init__(self, p_image, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < HEIGHT - 150:
            self.rect.y += self.speed
        
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT - 150:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, speed_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.speed_y = speed_y
    def update(self):
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.y >= HEIGHT - 50 or self.rect.y <= 0:
            speed_x *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


racket1 = Player('racket.png', 30, 200, 50, 150, 4)            
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

font.init()
font_text = font.Font(None, 35)
lose1 = font_text.render('PLAYER 1 LOSE', True, (100, 0, 0))
lose2 = font_text.render('PLAYER 2 LOSE', True, (100, 0, 0))


color_selection = False
run = True
finish = False

speed_x = 3
speed_y = 3

score1 = 0
score2 = 0

score_font = font.Font(None, 50)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            color_selection = True
        elif e.type == MOUSEBUTTONUP and e.button == 1:    
            color_selection = False

    if not finish:
        if color_selection:   
            background = generate_color()
        
        window.fill(background)

        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1
        
        if ball.rect.y > HEIGHT - 50 or ball.rect.y < 0:
                speed_y *= -1

        if ball.rect.x > WIDTH:
            score1 += 1
            ball.rect.x = 275
            ball.rect.y = 250

        if ball.rect.x < 0:
            score2 += 1
            ball.rect.x = 275
            ball.rect.y = 250

        if score1 >= WIN_SCORE or score2 >= WIN_SCORE:
            finish = True
            if score1 > score2:
                window.blit(lose2, (200, 200))
            else:
                window.blit(lose1, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()

        score_text = f'{score1}:{score2}'
        score_img = score_font.render(score_text, True, (255, 255, 255))
        score_rect = score_img.get_rect(center=(WIDTH // 2, 50))
        window.blit(score_img, score_rect)

        display.update()
        clock.tick(FPS)