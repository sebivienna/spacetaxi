# A GAME

#      **--advice--**
#blue point give full hitpoints
#yellow point give 10 - 20 points
#2 player

import pygame
import random
import math


class PygView(object):
    width = 1024
    height = 800

    def __init__(self, width=1024, height=800, fps=60):
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
        self.background = pygame.image.load("stars002.jpg")
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
        #assign default groups to each sprite class
        Taxi.groups = self.taxigroup, self.allgroup
        Platform.groups = self.platformgroup, self.allgroup
        Apple.groups = self.applegroup, self.allgroup
        Cannon.groups=self.cannongroup, self.allgroup
        Cannonball.groups=self.cannonballgroup, self.allgroup


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

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            milliseconds = self.clock.tick(self.fps)
            seconds = milliseconds/1000.0
            self.playtime += seconds
            self.draw_text("FPS: {:6.3} P1:Fuel: {:6.3} P1:HP: {} ".format( self.clock.get_fps(), 
                           self.taxi1.fuel, self.taxi1.hitpoints))
            #self.draw_text("P2:Fuel: {:6.3} P2:HP: {:6.3}".format(self.taxi2.fuel, self.taxi2.hitpoints))
                   
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

           

            if self.taxi1.fuel < 0.002:
                running = False

            for taxi in self.taxigroup:
                self.crashgroup = pygame.sprite.spritecollide(taxi, self.applegroup, True )
                for crashtaxi in self.crashgroup:
                    taxi.bonus()
                    Apple()
                    

                                    
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

                    
            for taxi in self.taxigroup:
                self.crashgroup = pygame.sprite.spritecollide(taxi, self.cannonballgroup, True)
                for crashcannonball in self.crashgroup:
                    taxi.hitpoints -= 1
                                       
            for taxi in self.taxigroup:
                if not taxi.alive:
                    running = False
            pygame.display.flip()
            #self.screen.blit(self.background, (0, 0))

            self.allgroup.clear(self.screen, self.background)
            self.allgroup.update(seconds)
            self.allgroup.draw(self.screen)



        pygame.quit()


    def draw_text(self, text,x = 20 ,y = 30):
        """Center text in window
        """
        pygame.draw.rect(self.screen, (0, 0, 0), (0, y, PygView.width, 30))   
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(surface, (x ,y))


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
        self.alive = True

        #YELLOW 

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
        self.status = 0 #0 = yellow, 1 = red, 2 = green
        self.radius = 50 # for collide check
        self.x = x
        self.y = y
        self.dx = 0.0
        self.dy = 0.0
        self.speed = 0.1
        self.landed = False

        self.fuel = 10.0
        self.fuelfull = 10.0
        
        self.hitpoints = 100.0
        self.hitpointsfull = 100.0
        
    def bonus(self):
            self.fuel = self.fuelfull




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





class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((40, 40)) # created on the fly
        self.image.fill((1, 2, 3))
        pygame.draw.circle(self.image, (190, 0 , 20), (20, 20), 10, 0) # apple
        self.image.set_colorkey((1, 2, 3)) # black transparent
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        #Apple.images.append(self.image)
        self.timer = 0.0
        self.dx = 0.0
        self.dy = 0.0
        self.x = 0
        self.y = 0
        self.maxtime = 6.0
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
         self.image=pygame.Surface((20,20))
         pygame.draw.circle(self.image,(100,83,81),(10,10),10)
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

