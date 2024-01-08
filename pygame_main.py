import pygame
pygame.init()
win = pygame.display.set_mode((840, 630))
pygame.display.set_caption("Squarey")

bg = pygame.image.load("E:\\ProgramFiles\\PyGame\\prj1\\images\\bg_img.png").convert()
#icpic = pygame.image.load("E:\\ProgramFiles\\PyGame\\prj1\\images\\car.png").convert()

x = 100
y = 100
baddyX = 300
baddyY = 300
vel = 6
baddyVel = 4
run = True

#rt = icpic.get_rect()
#rt.centre = (20, 20)

def drawGame():
          win.blit(bg, (20, 20))
          #win.blit(icpic, rt)
          #pygame.Surface.blitscreen.blit(icpic, rt)
          pygame.draw.rect(win, (0, 0, 255), (x, y, 20, 20))
          pygame.draw.rect(win, (255, 0, 0), (baddyX, baddyY, 40, 40))
          pygame.display.update()
          

while run:
      pygame.time.delay(100)

      if baddyX < x - 10: 
            baddyX = baddyX + baddyVel 
            drawGame() 
      elif baddyX > x + 10:
            drawGame()
            baddyX = baddyX - baddyVel
      elif baddyY < y - 10: 
            baddyY = baddyY + baddyVel 
      elif baddyY > y + 10:
            baddyY = baddyY - baddyVel
      else:
          run = False
      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False

      keys = pygame.key.get_pressed()

      if keys[pygame.K_LEFT]:
            x -= vel

      if keys[pygame.K_RIGHT]:
            x += vel
      
      if keys[pygame.K_UP]:
            y -= vel
      
      if keys[pygame.K_DOWN]:
            y += vel
      
      drawGame()
          
pygame.quit()