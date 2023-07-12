from pygame import *
from random import randint

WIDTH = 600
HEIGHT = 500
FPS = 60

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
        if keys[K_DOWN] and self.rect.y < HEIGHT - 80:
            self.rect.y += self.speed
        
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT - 80:
            self.rect.y += self.speed

racket1 = Player('racket.png', 30, 200, 50, 150, 4)            
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

color_selection = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            color_selection = True
        elif e.type == MOUSEBUTTONUP and e.button == 1:    
            color_selection = False

    if color_selection:   
        background = generate_color()
    
    window.fill(background)
    
    racket1.update_l()
    racket1.reset()
    racket2.update_r()
    racket2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)
