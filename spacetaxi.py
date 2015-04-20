# A GAME

#**--advice--**
#have
#your
#own
#ideas
#for
#more
#fun
#:)


import pygame
import random
import math


class PygView(object):
    width = 1024
    height = 750

    def __init__(self, width=1024, height=750, fps=60):
        """Initialize pygame, window, background, font,...
           default arguments
        """
                                
                         
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        PygView.widht = width
        PygView.height = height
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        #self.background.fill((255,255,255)) # fill background white
        try: 
            self.background = pygame.image.load("stars002.jpg")
        except:
            print("Sorry, you can´t play this game in the orignial background art. See README.md")
            self.make_stars()
        
                    
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 24, bold=True)
        #self.player1 = 0.0
        #self.player2 = 0.0

        self.platformgroup = pygame.sprite.Group()
        self.taxigroup = pygame.sprite.Group()
        self.allgroup = pygame.sprite.Group()
        self.applegroup = pygame.sprite.Group()
        self.cannongroup=pygame.sprite.Group()
        self.cannonballgroup=pygame.sprite.Group()
        self.bananagroup = pygame.sprite.Group()
        self.chewgumgroup = pygame.sprite.Group()
        self.states = ["menu", "play", "gameover", "credits", "rules"]
        self.state = "menu"
         
        
        #assign default groups to each sprite class
        Taxi.groups = self.taxigroup,
        Platform.groups = self.platformgroup, self.allgroup
        Apple.groups = self.applegroup, self.allgroup
        Cannon.groups=self.cannongroup, self.allgroup
        Cannonball.groups=self.cannonballgroup, self.allgroup
        Banana.groups = self.bananagroup, self.allgroup
        ChewGum.groups = self.chewgumgroup, self.allgroup


        self.taxi1 = Taxi(width/2, height/2)
        #self.taxi2 = Taxi(width, 800)
        self.platform1 = Platform(150, 125) #left up
        self.platform2 = Platform(150, 700) #left down
        self.platform3 = Platform(800, 125) #right up
        self.platform4 = Platform(800, 700) #right down
        #self.platform5 = Plattform(100, 100) #middle
        self.apple1 = Apple()
        #self.apple2 = Apple()
        #self.apple3 = Apple()
        self.cannon1 = Cannon(width/2, 0, 0, self.taxi1) #down
        self.cannon2 = Cannon(width/2, height, 0, self.taxi1) #up
        self.banana = Banana()
        self.chewgum = ChewGum()
        

    def paint(self):
        """painting on the surface"""
        #------- try out some pygame draw functions --------
        #pygame.draw.rect(Surface, color, Rect, width=0): return Rect
        #pygame.draw.rect(self.background, (0,255,0), (50,50,100,25)) # rect: (x1, y1, width, height)
        #pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
        #pygame.draw.circle(self.background, (0,200,0), (200,50), 35)
        #pygame.draw.polygon(Surface, color, pointlist, width=0): return Rect
        #pygame.draw.polygon(self.background, (0,180,0), ((250,100),(300,0),(350,50)))
        # pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1): return Rect
        #pygame.draw.arc(self.background, (0,150,0),(400,10,150,100), 0, 3.14) # radiant instead of grad
        #------------------- blitting a Ball --------------
        #myball = Ball() # creating the Ball object
        #myball.blit(self.background) # blitting it

    def run(self):
        """The mainloop
        """
        self.paint()
        self.screen.blit(self.background, (0, 0))
        self.showfps = False

        running = True
        while running:
            #self.screen.blit(self.background, (0, 0))
            

            milliseconds = self.clock.tick(self.fps)
            seconds = milliseconds/1000.0
            self.playtime += seconds 
            if self.state == "menu":
                text = "Press p to Start"  #1
                self.draw_text(text, 50 ,100)  
                text = "Press esc to Quit"  #4
                self.draw_text(text, 50, 220)
                text = "Press c for Credits"  #3
                self.draw_text(text, 50, 180)
                text = "Press i for Instruction"  #2
                self.draw_text(text, 50, 140)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_f:
                            self.showfps = not self.showfps
                            
                        if event.key == pygame.K_p:
                            print("ppp")
                            
                            self.taxi1.reset()
                            self.taxi1.x = PygView.widht/2
                            self.taxi1.y = PygView.height/2
                            self.state = "play"
                            
                        if event.key == pygame.K_ESCAPE:
                                running = False

                        if event.key == pygame.K_i:
                            self.state = "rules" 
                       
                        if event.key == pygame.K_c:
                            self.state = "credits"
                            
                       
            if self.state == "rules":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_ESCAPE:
                            self.state = "menu"           
                textlist1 = ["This is a Spacetaxi game.",
                             "You control the SpaceTaxi with",
                             "the arrow keys. You only allowed",
                             "to land on the top of the", 
                             "platform. The red point makes your",
                             "fuel full. The yellow point gives ",
                             "you between 100 and 20 score. ",
                             "The blue  point gives you full ",
                             "hitpoints. The cannons subtract from ",
                             "your hitpoints with the cannonballs ",
                             "one hitpoint. Much fun with the game."]
                             
                for row in range(0, len(textlist1)):
                    self.draw_text(textlist1[row], 100,  row*20+20)
                
                self.draw_text("Press esc to come to the menu", 100, row*20+70)
                          
            if self.state == "credits":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_ESCAPE:
                            self.state = "menu"
                textlist2 = ["Producer: Sebastian K. ",
                             "Sound: There isn´t a sound",
                             "Design: Sebastian K.", 
                             "Programmer: Sebastian K. and Co.",
                             "In Test: Alex W. and Horst",
                             "Idea: Sebastian K. with Horst",
                             ]            
                                 
                textlist3 = ["In Cooperatin with",
                             "spielend-programmieren.at"
                             ]          
                              
                for row in range(0, len(textlist2)):
                    self.draw_text(textlist2[row], 100,  row*20+20)
                for row2 in range(0, len(textlist3)):    
                    self.draw_text(textlist3[row2], 100, row*20+row2*20+50)
                self.draw_text("Press esc to come to the menu", 100, row*20+row2*20+100)           
                           
                                        
            if self.state == "play" or self.state == "gameover":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_f:
                            self.showfps = not self.showfps
                    
                        if event.key == pygame.K_ESCAPE:
                                self.state = "menu"
                            
                self.draw_text("Score:{:6.3} Fuel:{:6.3} HP:{} State:{}".format( self.taxi1.score, 
                               self.taxi1.fuel, self.taxi1.hitpoints, self.state))
                if self.showfps: 
                    self.draw_text("FPS:{:6.3}".format(self.clock.get_fps()), PygView.width - 200.0, PygView.height - 90.0)
                
                if self.state == "gameover":
                    self.font = pygame.font.SysFont('mono', 42, bold=True)
                    self.draw_text("GAMEOVER", PygView.width/2, PygView.height/2)
                    self.font = pygame.font.SysFont('mono', 24, bold=True)
                    
                    
                if self.state ==  "play":
                    
                        
                    for taxi in self.taxigroup:
                        taxi.status = 0
                        self.crashgroup = pygame.sprite.spritecollide(taxi, self.platformgroup, False )
                        #taxi.landed = False
                        for crashplatform in self.crashgroup:
                            if taxi.rect.centerx < crashplatform.rect.centerx:
                                if taxi.rect.left > crashplatform.rect.left:
                                    taxi.status = 2 #green
                                    taxi.landed = True
                                    taxi.dy = 0.0
                                    taxi.dx = 0.0
                                else:
                                    taxi.status = 1
                            if taxi.rect.centerx > crashplatform.rect.centerx:
                                if taxi.rect.right < crashplatform.rect.right:
                                    taxi.status = 2 #green
                                    taxi.landed = True
                                    taxi.dy = 0.0
                                    taxi.dx = 0.0
                                else:
                                    taxi.status = 1
                            if taxi.rect.centery > crashplatform.rect.centery:
                                if taxi.rect.top < crashplatform.rect.bottom:
                                    taxi.alive = False
                                    taxi.landed = False
                                    taxi.dy = 0.0
                                    taxi.dy = 0.0



                        print(taxi.status)

                   

                

                    for taxi in self.taxigroup:
                        self.crashgroup = pygame.sprite.spritecollide(taxi, self.applegroup, True )
                        for crashtaxi in self.crashgroup:
                            taxi.bonus_fuel()
                            Apple()
                    
                    
                    for taxi in self.taxigroup:
                        self.crashgroup = pygame.sprite.spritecollide(taxi, self.cannonballgroup, True)
                        for crashcannonball in self.crashgroup:
                            taxi.hitpoints -= 1    
                    
                    for taxi in self.taxigroup:
                        if taxi.hitpoints < 0.1 :
                            taxi.alive = False
                            print("No more HP")
                            
                        if taxi.fuel < 0.1:
                            taxi.alive = False
                            print("No more Fuel")
                            
                        if not taxi.alive:
                            
                            self.state = "gameover"
                            
                  
                    
                    
                    for taxi in self.taxigroup:
                        self.crashgroup = pygame.sprite.spritecollide(taxi, self.bananagroup, True)
                        for crashbanana in self.crashgroup:
                            taxi.bonus_score()
                            Banana()
                    
                    for taxi in self.taxigroup:
                       self.crashgroup = pygame.sprite.spritecollide(taxi, self.chewgumgroup, True)
                       for crashchewgum in self.crashgroup:
                           taxi.bonus_hitpoints()
                           ChewGum()
                    
                
                
                
                
                #pygame.display.flip()                      
                #for platform in self.platformgroup:
                #    self.crashgroup = pygame.sprite.spritecollide(platform, self.applegroup, True)
                #    for crashplatform in self.crashgroup:
                #        Apple()
                
                
                for apple in self.applegroup:
                    self.crashgroup = pygame.sprite.spritecollide(apple, self.platformgroup, False)
                    for crasplatform in self.crashgroup:
                        apple.kill()
                        Apple()
                        break

   
                        
                        
                for banana in self.bananagroup:
                   self.crashgroup = pygame.sprite.spritecollide(banana, self.platformgroup, False)
                   for crasplatform in self.crashgroup:
                       banana.kill()
                       Banana()
                       break
                        
                        
                                         
                for chewgum in self.chewgumgroup:
                   self.crashgroup = pygame.sprite.spritecollide(chewgum, self.platformgroup, False)
                   for crasplatform in self.crashgroup:
                       chewgum.kill()
                       ChewGum()
                       break
                    
            
            
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))
            
            #self.allgroup.clear(self.screen, self.background)
            if self.state == "play" or self.state == "gameover":
                
                self.allgroup.update(seconds)
                self.allgroup.draw(self.screen)
                
            if self.state == "play":
                self.taxigroup.update(seconds)
                self.taxigroup.draw(self.screen)



        pygame.quit()


    def draw_text(self, text,x = 20 ,y = 30):
        """Center text in window
        """
        #pygame.draw.rect(self.screen, (0, 0, 0), (0, y, PygView.width, 30))   
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(surface, (x ,y))


    def make_stars(self):
        self.background = pygame.Surface((1024, 750))
        for star in range(100):
            pygame.draw.circle(self.background, ((random.randint(245, 255), 250, 60)), 
                               (random.randint(0, 1024),
                                random.randint(0, 750)), (random.choice((0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2))))
    
    

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((250, 50)) # created on the fly
        self.image.fill((1, 2, 3))
        self.image.set_colorkey((1, 2, 3)) # black transparent
        #paint taxi
        pygame.draw.rect(self.image, (140, 100, 20), (7, 7, 250, 50))
        #pygame.draw.circle(self.image, (255,0,0), (50,50), 50, 2) # red circle
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.radius = 50 # for collide check
        self.x = x
        self.y = y
        self.dx = 0.0
        self.dy = 0.0



    def update(self, seconds):
        # no need for seconds but the other sprites need it
        #self.rect.center = pygame.mouse.get_pos()

        #self.dy += 0.1
        self.x += self.dx
        self.y += self.dy
        self.rect.centerx = self.x
        self.rect.centery = self.y




class Taxi(pygame.sprite.Sprite):
    images = [] #yellow, red, green
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.groups)
        

        #YELLOW 0

        self.image_yellow = pygame.Surface((150,50)) # created on the fly
        self.rect = self.image_yellow.get_rect()
        self.image_yellow.fill((255, 255, 255))
        #self.image_yellow.set_colorkey((1,2,3)) # black transparent
        #paint taxi
        pygame.draw.rect(self.image_yellow, (130, 0, 130), (65, 0, 50, 35))  # kabine
        pygame.draw.rect(self.image_yellow, (255, 255, 0), (20, 20, 250, 20)) # taxi hülle yellow
        pygame.draw.circle(self.image_yellow, (255, 255, 254), (50, 43), 8, 0) # wheel left
        pygame.draw.circle(self.image_yellow, (255, 255, 254), (130, 43), 8, 0) # wheel right
        pygame.draw.circle(self.image_yellow, (0, 0, 0), (50, 43), 2, 0) # wheel left middle
        pygame.draw.circle(self.image_yellow, (0, 0, 0), (130, 43), 2, 0) # wheel right middle
        #pygame.draw.circle(self.image, (255,0,0), (50,50), 50, 2) # red circle
        self.image_yellow.set_colorkey((255,255,255))
        self.image_yellow = self.image_yellow.convert_alpha()
        Taxi.images.append(self.image_yellow)

        #RED 1

        self.image_red = pygame.Surface((150,50)) # created on the fly
        self.image_red.fill((255, 255, 255))
        self.image_red.set_colorkey((1,2,3)) # black transparent
        pygame.draw.rect(self.image_red, (130, 0, 130), (65, 0, 50, 35)) #kabine
        pygame.draw.rect(self.image_red, (255, 0, 0), (20, 20, 250, 20)) #taxi hülle red
        pygame.draw.circle(self.image_red, (255, 255, 254), (50, 43), 8, 0) # wheel left
        pygame.draw.circle(self.image_red, (255, 255, 254), (130, 43), 8, 0) # wheel right
        pygame.draw.circle(self.image_red, (0, 0, 0), (50, 43), 2, 0) # wheel left middle
        pygame.draw.circle(self.image_red, (0, 0, 0), (130, 43), 2, 0) # wheel right middle
        self.image_red.set_colorkey((255,255,255))
        self.image_red = self.image_red.convert_alpha()
        Taxi.images.append(self.image_red)

        #GREEN 2

        self.image_green = pygame.Surface((150,50)) # created on the fly
        self.image_green.fill((255, 255, 255))
        self.image_green.set_colorkey((1,2,3)) # black transparent
        pygame.draw.rect(self.image_green, (130, 0, 130), (65, 0, 50, 35)) #kabine
        pygame.draw.rect(self.image_green, (0, 255, 0), (20, 20, 250, 20)) #taxi hülle green
        pygame.draw.circle(self.image_green, (255, 255, 254), (50, 43), 8, 0) # wheel left
        pygame.draw.circle(self.image_green, (255, 255, 254), (130, 43), 8, 0) # wheel right
        pygame.draw.circle(self.image_green, (0, 0, 0), (50, 43), 2, 0) # wheel left middle
        pygame.draw.circle(self.image_green, (0, 0, 0), (130, 43), 2, 0) # wheel right middle
        self.image_green.set_colorkey((255,255,255))
        self.image_green = self.image_green.convert_alpha()
        Taxi.images.append(self.image_green)

        self.image = Taxi.images[0]
        self.x = x
        self.y = y
        self.radius = 50 # for collide check
        

    def reset(self):
        self.image = Taxi.images[0]
        self.alive = True
        self.status = 0 #0 = yellow, 1 = red, 2 = green
        
        self.dx = 0.0
        self.dy = 0.0
        self.speed = 0.1
        self.landed = False

        self.fuel = 10.0
        self.fuelfull = 10.0
        
        self.hitpoints = 30.0
        self.hitpointsfull = 30.0
        
        self.score = 0.0
        self.rect.centerx = PygView.width / 2
        self.rect.centery = PygView.height / 2
        
        
    
       
    def bonus_fuel(self):
            self.fuel = self.fuelfull
    
    def bonus_score(self):
        self.score +=  random.randint(10, 20)
    
    def bonus_hitpoints(self):
        self.hitpoints = self.hitpointsfull




    def update(self, seconds):
        # no need for seconds but the other sprites need it
        #self.rect.center = pygame.mouse.get_pos()
        self.image = Taxi.images[self.status]
        #keys
        pressedkeys = pygame.key.get_pressed()
        #self.dx, self.dy = 0, 0 # no cursor key, no movement
        if pressedkeys[pygame.K_LEFT] and not self.landed:
            self.dx -= self.speed
        if pressedkeys[pygame.K_RIGHT] and not self.landed:
            self.dx += self.speed
        if pressedkeys[pygame.K_UP]:
            self.landed =  False
            self.dy -= self.speed
        if pressedkeys[pygame.K_DOWN] and not self.landed:
            self.dy += self.speed



        if not self.landed:
            self.dy += 0.01  #gravity
        self.x += self.dx
        self.y += self.dy


        # check
        if self.y >800:
            self.y = 800
            self.dy = 0.0
        if self.y <0:
            self.y = 0
            self.dy = 0.0
        if self.x <0:
            self.x = 0
            self.dx = 0.0
        if self.x >1024:
            self.x = 1024
            self.dx = 0.0
        self.rect.centerx = self.x
        self.rect.centery = self.y

        self.fuel -= 0.02
        if self.fuel < 0.001:
            self.fuel = 0.001
            





class Cannon(pygame.sprite.Sprite):
    def __init__(self,x,y, angle, target):
        pygame.sprite.Sprite. __init__(self, self.groups) # !!!!!!!!!
        #Reloadbar(self)
        self.target = target
        self.image = pygame.Surface((250, 250))
        self.image.fill((1, 2, 3))
        self.image.set_colorkey((1, 2, 3))
        pygame.draw.circle(self.image,(145, 110, 20), (125, 125), 75, 0)
        pygame.draw.rect(self.image,(103, 103, 103), (110, 110, 30, 125), )
        #pygame.draw.rect(self.image,(58, 19, 5), (20, 80, 30, 10))
        #pygame.draw.rect(self.image,(17, 11, 9), (20, 45, 60, 15))
        self.image=self.image.convert_alpha()
        self.original=self.image.copy()
        self.oldrect = self.original.get_rect()
        self.image=pygame.transform.rotozoom(self.original, angle, 1.0)
        self.rect=self.image.get_rect()
        self.reloadtime=0.0  # how many time of the reloadtimefull has passed
        self.reloadtimefull=2.0 + random.random()*3
        
        self.x = x
        self.y = y
        self.dx = 0.0
        self.dy = 0.0
        self.oldrect.centerx = self.x
        self.oldrect.centery = self.y
        self.rect.centerx = self.x
        self.rect.centery = self.y
    
    def update(self, seconds):
        # rotate toward mouse
        dx = self.target.rect.centerx - self.rect.centerx
        dy =  self.target.rect.centery - self.rect.centery
        self.angle = math.atan2(-dx, -dy)/math.pi * 180.0 
        self.image = pygame.transform.rotozoom(self.original, self.angle+180, 1.0)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y


        if self.reloadtime < self.reloadtimefull:
            self.reloadtime += seconds
        else:
            #shoot
            startx = 125 * math.cos((self.angle+90) * math.pi / 180) 
            starty = 125 * math.sin((self.angle+90)* math.pi / -180)
            Cannonball(self.rect.centerx + startx, self.rect.centery + starty,
                       self.target.rect.centerx, self.target.rect.centery)  
            self.reloadtime = 0.0   
        #self.rect.centerx = self.oldrect.centerx - self.rect.centerx
        #self.y += self.oldrect.centery - self.rect.centery       
       



class Cannonball(pygame.sprite.Sprite):
    def __init__(self,x,y,targetx,targety):
         pygame.sprite.Sprite. __init__(self,self.groups) #!!!!!!!!!!
         self.image = pygame.Surface((20,20))
         pygame.draw.circle(self.image,(191,191,191),(10,10),10)
         self.image.set_colorkey((0,0,0))
         self.image=self.image.convert_alpha()
         self.rect = self.image.get_rect()
         self.x = x
         self.y = y
         self.dx=0
         self.dy=0
         self.maxspeed = 4.5
         self.targetx = targetx
         self.targety = targety
         distancex = self.targetx - self.x
         distancey = self.targety - self.y
         distance = ( distancex**2 + distancey**2)**0.5
         self.dx = distancex / distance
         self.dy = distancey / distance
         self.dx *= self.maxspeed
         self.dy *= self.maxspeed  
         
    def update(self, seconds):
         self.x=self.x + self.dx
         self.y=self.y + self.dy
         if self.x < 0:
             self.kill()
         if self.y < 0:
             self.kill()
         if self.x> PygView.width:
             self.kill()
         if self.y> PygView.height:
             self.kill()     
         self.rect.centerx = self.x
         self.rect.centery = self.y
         
         
         

class Fruit (pygame.sprite.Sprite):
    def __init__(self, color, maxtime = 6):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((40, 40)) # created on the fly
        self.image.fill((1, 2, 3))
        pygame.draw.circle(self.image, color, (20, 20), 10, 0) # apple
        self.image.set_colorkey((1, 2, 3)) # black transparent
        self.rect = self.image.get_rect()
        #Apple.images.append(self.image)
        self.timer = 0.0
        self.image = self.image.convert_alpha()
        self.dx = 0.0
        self.dy = 0.0
        self.x = 0
        self.y = 0
        self.maxtime = maxtime
        self.newpos()
        
        
        
    def newpos(self):
        self.x = random.randint (0, PygView.widht)
        self.y = random.randint (0, PygView.height)


    def update(self, seconds):
        # no need for seconds but the other sprites need it
        #self.rect.center = pygame.mouse.get_pos()

        #self.dy += 0.1
        self.x += self.dx
        self.y += self.dy
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.timer += seconds
        if self.timer > self.maxtime:
            self.timer = 0.0
            self.newpos()
        
        
class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self, (190, 0, 20), 6)
        
class Banana(Fruit):
    def __init__ (self):
        Fruit.__init__ (self, (255, 255, 0), 2)
        
        
class ChewGum(Fruit):
    def __init__  (self):
        Fruit. __init__ (self, (0, 33, 255),  4)

                                 
        
    


class Ball(object):
    """this is not a native pygame sprite but instead a pygame surface"""
    def __init__(self, radius = 50, color=(0,0,255), x=320, y=240):
        """create a (black) surface and paint a blue ball on it"""
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        # create a rectangular surface for the ball 50x50
        self.surface = pygame.Surface((2*self.radius,2*self.radius))
        # pygame.draw.circle(Surface, color, pos, radius, width=0) # from pygame documentation
        pygame.draw.circle(self.surface, color, (radius, radius), radius) # draw blue fillcircle on ball surface
        self.surface = self.surface.convert() # for faster blitting.
        # to avoid the black background, make black the transparent color:
        # self.surface.set_colorkey((0,0,0))
        # self.surface = self.surface.convert_alpha() # faster blitting with transparent color


    def blit(self, background):
        """blit the Ball on the background"""
        background.blit(self.surface, ( self.x, self.y))


if __name__ == '__main__':

    # call with width of window and fps
    PygView().run()
