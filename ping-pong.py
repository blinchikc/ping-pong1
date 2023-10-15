from pygame import *
from random import *
from time import time as timer

window = display.set_mode((700, 500))
display.set_caption('ping-pong')


#классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size1, size2, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size1, size2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.x += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[k_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[k_s] and self.rect.y < 495:
            self.rect.x += self.speed

player1 = Player('platform.png', 10, 250, 10, 50, 5)
player2 = Player('platform.png', 10, 250, 10, 50, 5)
ball =GameSprite('ball_1615463127.png', 350, 250, 20, 20, 5)

speed_x = 3
speed_y = 3

game = True
finish = False

while game:
    if finish != True:
        window.fill((255,155,55))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    










#картинка
#background = transform.scale(image.load('galaxy.jpg'), (700, 500))

#групы
#monsters = sprite.Group()
#ullets = sprite.Group()
#asteroids = sprite.Group()

#спрайты
#player = Player('rocket.png', 300, 430, 65, 65, 5)
    
#for i in range(1, 5):
    #x = Enemy('ufo.png', randint(0, 500), 20, 65, 65, randint(1,3))
    #monsters.add(x)

#for q in range(1, 4):
    #a = Aster('asteroid.png', randint(0, 700), 20, 65, 65, 1)
    #asteroids.add(a)

#текст
#font.init()
#font = font.SysFont("Arial", 40)
#win = font.render('ты выиграл!', True, (255, 165, 0))
#lose = font.render('ты проиграл', True, (255, 165, 0))

#музыка
#mixer.init()
#mixer.music.load('space.ogg')
#fire_sound = mixer.Sound('fire.ogg')
#mixer.music.play()

#частота кадров
#FPS = 60
#clock = time.Clock()

#счётчики                               #     #
#score = 0                               #     #
#lost = 0                                #     #

#для игрового цикла                 ##           ##
#num_fire = 0                           #########
#rel_time = False
#run = True
#finish = False

#игровой цикл
#while run:

    #for e in event.get():
        #if e.type == QUIT:
            #run = False

        #elif e.type == KEYDOWN:
            #if e.key == K_SPACE:

                #if num_fire < 12 and rel_time == False:
                    #fire_sound.play()
                    #player.fire()
                    #num_fire += 1
                
               # if num_fire >= 12 and rel_time == False:
                   # last_time = timer()
                   # rel_time = True
    #если финиш не труе
#   if finish != True:
   #     window.blit(background, (0,0))
        #надписи
    #    q = font.render('Убито:' + str(score), True, (255, 165, 0))
    #    e = font.render('Пропущенно:' + str(lost), True, (255, 165, 0))
    #    window.blit(q, (25, 25))
    #    window.blit(e, (25, 60))

     #   monsters.draw(window)
       # monsters.update()

     #   asteroids.draw(window)
      #  asteroids.update()

      #  bullets.draw(window)
       # bullets.update()

      #  player.update()
      #  player.reset()

      #  if sprite.spritecollide(player, monsters, False) or lost >= 5:
      #      finish = True
      #      window.blit(lose, (225, 200))
        
     #   if sprite.spritecollide(player, asteroids, False) or lost >= 5:
       #     finish = True
      #      window.blit(lose, (225, 200))

      #  if sprite.groupcollide(monsters, bullets, True, True):
   #         score += 1
     #       x1 = Enemy('ufo.png', randint(0, 500), 0, 65, 65, 1)
    #        monsters.add(x1)

     #   if score >= 30:
      #      finish = True
      #      window.blit(win, (225, 200))
        
      #  if lost >= 5:
        #    finish = True
       #     window.blit(lose, (225, 200))

       # if rel_time == True:
        #    now_time = timer()
        #    if now_time - last_time < 2:
        #        per = font.render('...', True, (255, 165, 0))
  #              window.blit(per, (280, 450))
            #елсе
         #   else:
        #        num_fire = 0
          #      rel_time = False

    #дисплей упдете и клок тик
    #display.update()
   # clock.tick(FPS)