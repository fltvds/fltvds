import pygame
import random
score = 0
roundwin = 5
endscore = 0
level = 1
def new_game():
    pygame.init()

    g_width = 1024
    g_height = 640

    win = pygame.display.set_mode((g_width,g_height))

    pygame.display.set_caption("Alien: Forsaken Land")

    clock = pygame.time.Clock()

    bulletSound = pygame.mixer.Sound('bullet.wav')
    hitSound = pygame.mixer.Sound('hit.wav')

    music = pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
    global score
    score = 0
    lives = 3
    screen = pygame.Surface((g_width, g_height))
    pth = ''
    
    class Menu:
        def __init__(self, punkts = [122, 130, u'Punkt',(250,250,30),(130,130,130)]):
            self.punkts = punkts
        
        def render(self, p, font, num_punkt):
            for i in self.punkts:
                if num_punkt == i[5]:
                    p.blit(font.render(i[2], 1, i[4]), (i[0], i[1]-30))
                else:
                    p.blit(font.render(i[2], 1, i[3]), (i[0], i[1]-30))

        def menu(self):
            done = True
            font_menu = pygame.font.SysFont('comicsans', 50, True)
            pygame.key.set_repeat(0,0)
            pygame.mouse.set_visible(True)
            punkt = 0
            while done:
                screen.fill((0,0,0))
                mp = pygame.mouse.get_pos()
                for i in self.punkts:
                    if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+50:
                        punkt =i[5]
                    self.render(screen, font_menu, punkt)
                    
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            exit()
                        elif e.type == pygame.KEYDOWN:
                            if e.type == pygame.K_ESCAPE:
                                exit()
                            if e.key == pygame.K_UP:
                                if punkt > 0:
                                   punkt -= 1
                            if e.key == pygame.K_DOWN:
                                if punkt < len(self.punkts)-1:
                                   punkt += 1
                        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                            if punkt == 0:
                                return ''
                                done = False
                            elif punkt == 1:
                                num = 1
                                return 'blue/'
                                done = False
                            elif punkt == 2:
                                return 'red/'
                                done = False
                            elif punkt == 3:
                                exit()
                        
                    win.blit(screen, (0, 30))
                    pygame.display.flip()



    class player(object):
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5
            self.isJump = False
            self.left = False
            self.right = False
            self.walkCount = 0
            self.jumpCount = 10
            self.standing = True
            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
#             self.isHit = False

        def draw(self, win):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            
#             if self.isHit:
#                 if self.left:
#                     win.blit(playerHit[1], (self.x,self.y))
#                 elif self.right:
#                     win.blit(playerHit[0], (self.x,self.y))

                

            if not(self.standing):
                if self.left:
                    win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount +=1
            else:
                if self.right:
                    win.blit(playerHit[0], (self.x, self.y))
                else:
                    win.blit(playerHit[1], (self.x, self.y))
            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

        def hit(self):
            self.isJump = False
            self.jumpCount = 10
            self.x = 100
            self.y = 440
            goblin.x = 400
            goblin.y = 440
            self.walkCount = 0
            font1 = pygame.font.SysFont('comicsans', 100)
            if lives == 1:
                text2 = font1.render('You are dead, Try again!', 1, (255,15,0))
                win.blit(text2, (g_width/2 - (text2.get_width()/2),200))
                pygame.display.flip()
                pygame.time.delay(1000)
                new_game()
            else:
                text = font1.render('-1', 1, (255,15,0))
                win.blit(text, (g_width/2 - (text.get_width()/2),200))
            pygame.display.update()
            i = 0
            while i < 200:
                pygame.time.delay(5)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 201
                        pygame.quit()

                    


    class projectile(object):
        def __init__(self,x,y,radius,color,facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 8 * facing

        def draw(self,win):
            if facing == 1:
                pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
                pygame.image.load('R3.png')
            elif facing == -1:
                pygame.draw.circle(win, self.color, (self.x - 15,self.y), self.radius)
                pygame.image.load('L3.png')

    class enemy(object):
        walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png'), pygame.image.load('R4E.png')]
        walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png'), pygame.image.load('L4E.png')]
        
        def __init__(self, x, y, width, height, end, player):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.path = [0, self.end]
            self.walkCount = 0
            self.vel = 1
            self.hitbox = (self.x+17, self.y + 2, 31, 57)
            self.health = 10
            self.visible = True

        def draw(self,win):
            self.move()
            if self.visible == True:
                if self.walkCount + 1 >= 33:
                    self.walkCount = 0

                if abs(man.x - self.x) < 200:
                    if man.x - self.x < 0:
                        self.vel = -1
                    else:
                        self.vel = 1
                         
                if self.vel > 0:
                    win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                    self.walkCount += 1
#                 else:                                        
#                     self.vel = 0
#                     if man.x - self.x > 0:
#                         win.blit(self.walkRight[0], (self.x, self.y))
#                     else:
#                         win.blit(self.walkLeft[0], (self.x, self.y))
                pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
                pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
                self.hitbox = (self.x - self.width//10, self.y + 2, 31, 57)
#                pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

        def move(self):
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0

        def hit(self):
            times = 0
            if self.health > 0:
                self.health -= 1
            else:
                self.visible = False
                global score
                global level
                global roundwin
                global endscore
                score += 1
                font1 = pygame.font.SysFont('comicsans', 50, True)
                if score == endscore + roundwin*level:
                    endscore = score
                    goblin2.visible = True
                    text3 = font1.render(('Level {} won, adding enemies').format(level), 1, (255,15,0))
                    if level < 2:     
                        level += 1
                    else:
                        text4 = font1.render(('You have won the game, restarting'), 1, (255,15,0))
                        win.blit(text4, (g_width/2 - (text4.get_width()/2),200))
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        new_game()
                    win.blit(text3, (g_width/2 - (text3.get_width()/2),200))
                    pygame.display.flip()
                    pygame.time.delay(1000)
                if man.x < g_width / 2:
                        self.__init__((man.x + (random.randint(100, g_width-man.x-50))), 440, 64, 64, g_width-50, man)
                elif man.x > g_width / 2:
                        self.__init__((man.x - (random.randint(100, man.x+50))), 440, 64, 64, g_width-50, man)

    class enemy2(object):
            walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png'), pygame.image.load('R4E.png')]
            walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png'), pygame.image.load('L4E.png')]
            def __init__(self, x, y, width, height, end, player):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.end = end
                self.path = [0, self.end]
                self.walkCount = 0
                self.vel = 1
                self.hitbox = (self.x+17, self.y + 2, 31, 57)
                self.health = 10
                self.visible = False

            def draw(self,win):
                self.move()
                if self.visible == True:
                    if self.walkCount + 1 >= 33:
                        self.walkCount = 0

                    if abs(man.x - self.x) < 200:
                        if man.x - self.x < 0:
                            self.vel = -1
                        else:
                            self.vel = 1
                             
                    if self.vel > 0:
                        win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                        self.walkCount += 1
                    else:
                        win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                        self.walkCount += 1
    #                 else:                                        
    #                     self.vel = 0
    #                     if man.x - self.x > 0:
    #                         win.blit(self.walkRight[0], (self.x, self.y))
    #                     else:
    #                         win.blit(self.walkLeft[0], (self.x, self.y))
                    pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
                    pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
                    self.hitbox = (self.x - self.width//10, self.y + 2, 31, 57)
    #                pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

            def move(self):
                if self.vel > 0:
                    if self.x + self.vel < self.path[1]:
                        self.x += self.vel
                    else:
                        self.vel = self.vel * -1
                        self.walkCount = 0
                else:
                    if self.x - self.vel > self.path[0]:
                        self.x += self.vel
                    else:
                        self.vel = self.vel * -1
                        self.walkCount = 0

            def hit(self):
                if self.health > 0:
                    self.health -= 1
                else:
                    global score
                    score += 1
                    self.visible = False
                    if man.x < g_width / 2:
                        self.__init__((man.x + (random.randint(100, g_width-man.x-50))), 440, 64, 64, g_width-50, man)
                        self.visible = True
                    elif man.x > g_width / 2:
                        self.__init__((man.x - (random.randint(100, man.x+50))), 440, 64, 64, g_width-50, man)
                        self.visible = True
                        
    def redrawGameWindow():
        win.blit(bg, (0,0))
        text = font.render('Score: ' + str(score), 1, (0,0,0))
        text2 = font.render('Lives: ' + str(lives), 1, (0,255,0,10))
        win.blit(text, (g_width-150, 10))
        win.blit(text2, (g_width - g_width + 10, 10))
        man.draw(win)
        goblin.draw(win)
        goblin2.draw(win)
        for bullet in bullets:
            bullet.draw(win)
        
        pygame.display.update()


    #mainloop  
    punkts = [(g_width/2-150,g_height/2-50,u'Green Alien',(128,128,128),(255,255,255),0),
              (g_width/2-150,g_height/2-10,u'Blue Alien',(128,128,128),(255,255,255),1),
              (g_width/2-150,g_height/2+30,u'Red Alien',(128,128,128),(255,255,255),2),
              (g_width/2-150,g_height/2+70,u'Exit',(128,128,128),(255,255,255),3)]

    m = Menu(punkts)
    pth = m.menu()
    
    walkRight = [pygame.image.load(pth+'R1.png'), pygame.image.load(pth+'R2.png'), pygame.image.load(pth+'R4.png'), pygame.image.load(pth+'R5.png'), pygame.image.load(pth+'R6.png'), pygame.image.load(pth+'R7.png'), pygame.image.load(pth+'R8.png'), pygame.image.load(pth+'R9.png'), pygame.image.load(pth+'R2.png')]
    walkLeft = [pygame.image.load(pth+'L1.png'), pygame.image.load(pth+'L2.png'), pygame.image.load(pth+'L4.png'), pygame.image.load(pth+'L5.png'), pygame.image.load(pth+'L6.png'), pygame.image.load(pth+'L7.png'), pygame.image.load(pth+'L8.png'), pygame.image.load(pth+'L9.png'), pygame.image.load(pth+'L2.png')] 
    playerHit = [pygame.image.load(pth+'Rhit.png'), pygame.image.load(pth+'Lhit.png')]
    bg_pic = ['bg2.jpg','bg.png']
    bg_num = random.randint(0,1)
    bg = pygame.image.load(bg_pic[bg_num])
    char = pygame.image.load(pth+'standing.png')
    
    font = pygame.font.SysFont('comicsans', 30, True)
    man = player(100, 440, 64, 64)
    goblin = enemy(400, 440, 64, 64, g_width-50, man)
    goblin2 = enemy2(600, 440, 64, 64, g_width-50, man)
    shootLoop = 0
    bullets = []
    run = True
    while run:
        clock.tick(30)

        if goblin.visible == True:
            if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                    man.hit()
                    if lives > 0:
                        lives -= 1
                        
        if goblin2.visible == True:
                if man.hitbox[1] < goblin2.hitbox[1] + goblin2.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin2.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > goblin2.hitbox[0] and man.hitbox[0] < goblin2.hitbox[0] + goblin2.hitbox[2]:
                        man.hit()
                        if lives > 0:
                            lives -= 1

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        for bullet in bullets:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    if goblin.visible == True:
                        hitSound.play()
                        goblin.hit()
                        bullets.pop(bullets.index(bullet))
                        
        for bullet in bullets:
            if bullet.y - bullet.radius < goblin2.hitbox[1] + goblin2.hitbox[3] and bullet.y + bullet.radius > goblin2.hitbox[1]:
                if bullet.x + bullet.radius > goblin2.hitbox[0] and bullet.x - bullet.radius < goblin2.hitbox[0] + goblin2.hitbox[2]:
                    if goblin2.visible == True:
                        hitSound.play()
                        goblin2.hit()
                        bullets.pop(bullets.index(bullet))
                        
            if bullet.x < man.x + 120 and bullet.x > man.x-100:
                bullet.x += bullet.vel
            else:
                try:
                    bullets.pop(bullets.index(bullet))
                except:
                    pass

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:
            bulletSound.play()
            if man.left:
                facing = -1
            else:
                facing = 1
                
            if len(bullets) < 5:
                bullets.append(projectile(round(man.x + (man.width//2)), round(man.y + man.height//2), 6, (0,0,0), facing))
                

            shootLoop = 1
        
        if keys[pygame.K_ESCAPE]:
            exit()
            

        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x < g_width - man.width / 2  - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.walkCount = 0
            
        if not(man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10
        
        redrawGameWindow()
    
    pygame.quit()

new_game()