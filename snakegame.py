import pygame as pg
import random

def is_collision(x1, y1, x2, y2):
    if abs(x1-x2) < 20 and abs(y1-y2) < 20:
        return True

def did_hit_boundry(x1,y1):
    if x1 < 0 or x1 > 780 or y1 < 0 or y1 > 580:
        return True

pg.init()

score_font = pg.font.Font(None, 32)
gameover_font = pg.font.Font(None, 64)
gameover_image = gameover_font.render("Game Over", True, (255, 255, 255))

screen = pg.display.set_mode((800,600))

running = True

snake_x = 300
snake_y = 300
speed = 2

food_x = random.randint(100,700)
food_y = random.randint(100,500)
speed = 1

direction = 'R'

score = 0

clock = pg.time.Clock()

fps = 60

while running:
    #event = pg.event.wait()
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            print(event)
        
            if event.key == pg.K_LEFT:
                direction = 'L'
            elif event.key == pg.K_RIGHT:
                direction = 'R'
            elif event.key == pg.K_UP:
                direction = 'U'
            elif event.key == pg.K_DOWN:
                direction = 'D'       

    screen.fill((0,100,100))
    
    if direction == 'L':
        snake_x -= speed
    elif direction == 'R':
        snake_x += speed
    elif direction == 'U':
        snake_y -= speed
    elif direction == "D":
        snake_y += speed

    pg.draw.rect(screen, (0,0,0), (snake_x, snake_y, 20, 20))
    pg.draw.rect(screen, (255,255,255), (food_x, food_y, 20, 20)) 

    if is_collision(snake_x, snake_y, food_x, food_y):
        score += 1
        food_x = random.randint(100,700)
        food_y = random.randint(100,500)
        speed += 2
        print(score)

    if did_hit_boundry(snake_x, snake_y,):
        speed = 0
        scren.blit(gameover_image, (300,300))

    score_image = score_font.render("Score:  " + str(score), True, (255, 255, 255))
    screen.blit(score_image, (10, 10))

    pg.display.update()
