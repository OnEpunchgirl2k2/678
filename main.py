import pygame
from player.player import Player
import game_object
from enemy.enemy import Enemy
from enemy.enemy_spawner import EnemySpawner
from input.input_manager import InputManager
import random
BG = (255, 255, 0)

pygame.init()
pygame.display.set_caption('shoot')


SIZE = (800,640)
canvas = pygame.display.set_mode(SIZE)


clock = pygame.time.Clock()

loop = True

input_manager =InputManager()

player = Player(600, 500, input_manager)

game_object.add(player)
game_object.add(EnemySpawner())
img = pygame.image.load('image/heart.png')

while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    
    hp_count = 0

    for obj in game_object.game_objects:
        if type(obj) == Enemy:
            if obj.is_active == False and obj.y > 627:
                hp_count += 1
    player.hp = 10
    player.hp -= hp_count
   
    
    if player.hp <= 0:
        player.is_active = False
    game_object.update()

    if player.is_active == False:
        canvas.fill((0,0,0))
        text = str("Game Over")
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(text, True, (255,255,255))
        text_width = text.get_width()
        text_height = text.get_height()
        canvas.blit(text, (400 - text_width/2, 320 - text_height/2 ))
    else:
        BG = pygame.image.load('')
        canvas.blit(BG, (0,0))
        game_object.render(canvas)
        img = pygame.transform.scale(img, (30, 30))
        for i in range(player.hp):

            canvas.blit(img, (10+ i*30, 10 ))
    pygame.display.flip()
    clock.tick(60)
