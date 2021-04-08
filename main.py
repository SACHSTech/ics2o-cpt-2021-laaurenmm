""" 
Hardware Components game
"""
 
import pygame
 
# Define some colors
black = (0, 0, 0)
beige = (240, 213, 141) #orange not beige
white = (255, 255, 255) 
green = (187, 235, 171)
pink = (255, 220, 204)
brown = (61, 38, 21)
blue = (162, 206, 224)
yellow = (255, 252, 156)
  
pygame.init()
  
# Set the width and height of the screen [width, height]
size = (500, 400)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Hardwware components game")

#set up graphics
background_image = pygame.image.load("Homeimage.jpg").convert()
image_CPU = pygame.image.load ("CPU.jpg").convert()
image_motherboard = pygame.image.load ("Motherboard.jpg").convert()
image_RAM = pygame.image.load ("RAM.jpg").convert()
image_harddrive = pygame.image.load ("Harddrive.jpg").convert()
image_graphicscard = pygame.image.load ("Graphicscard.jpg").convert()
image_powersupply = pygame.image.load ("Powersupply.jpg").convert()

player_image = pygame.image.load("star.jpg").convert() 
player_image.set_colorkey(white)

# Set positions of graphics
background_position = [0, 0]

pygame.display.set_caption("Hardware Components")
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
#buttonhome properties
rect_x = 450
rect_y = 10
rect_width = 45
rect_height = 45
button_pressed = True
mouse_click_position = [0,0]

#button1 properties
rect_x1 = 220
rect_y1 = 370
rect_width1 = 25
rect_height1 = 25
button_pressed1 = False
mouse_click_position = [0,0]

#button2 properties
rect_x2 = 270
rect_y2 = 370
rect_width2 = 25
rect_height2 = 25
button_pressed2 = False
mouse_click_position = [0,0]

#button3 properties
rect_x3 = 320
rect_y3 = 370
rect_width3 = 25
rect_height3 = 25
button_pressed3 = False
mouse_click_position = [0,0]

#button4 properties
rect_x4 = 370
rect_y4 = 370
rect_width4 = 25
rect_height4 = 25
button_pressed4 = False
mouse_click_position = [0,0]

#button5 properties
rect_x5 = 420
rect_y5 = 370
rect_width5 = 25
rect_height5 = 25
button_pressed5 = False
mouse_click_position = [0,0]

#button6 properties
rect_x6 = 470
rect_y6 = 370
rect_width6 = 25
rect_height6 = 25
button_pressed6 = False
mouse_click_position = [0,0]

#Loop until the user clicks the close button.
done = False


# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
            mouse_click_position = pygame.mouse.get_pos()

#HOME PAGE BUTTON IF STATEMENT
        if (rect_x <= mouse_click_position[0] and mouse_click_position[0] <= rect_x + rect_width) and (rect_y <= mouse_click_position[1] and mouse_click_position[1] <= rect_y + rect_height):
          button_pressed = True

        else:
          button_pressed = False

    # Set the screen background
        if button_pressed:
          background_image = pygame.image.load("Homeimage.jpg").convert()
        else:
          background_image = pygame.image.load("Homeimage.jpg").convert()


#CPU BUTTON PRESS IF STATEMENT
        if (rect_x1 <= mouse_click_position[0] and mouse_click_position[0] <= rect_x1 + rect_width1) and (rect_y1 <= mouse_click_position[1] and mouse_click_position[1] <= rect_y1 + rect_height1):
          button_pressed1 = True

        else:
          button_pressed1 = False

    # Set the screen background
        if button_pressed2:
          background_image = pygame.image.load("CPU.jpg").convert()
        else:
          background_image = pygame.image.load("Homeimage.jpg").convert()


#MOTHERBOARD BUTTON PRESS IF STATEMENT
        if (rect_x2 <= mouse_click_position[0] and mouse_click_position[0] <= rect_x2 + rect_width2) and (rect_y2 <= mouse_click_position[1] and mouse_click_position[1] <= rect_y2 + rect_height2):
          button_pressed2 = True

        else:
          button_pressed2 = False

    # Set the screen background
        if button_pressed2:
          background_image = pygame.image.load("Motherboard.jpg").convert()
        else:
          background_image = pygame.image.load("Homeimage.jpg").convert()

#RAM BUTTON PRESS IF STATEMENT
        if (rect_x3 <= mouse_click_position[0] and mouse_click_position[0] <= rect_x3 + rect_width3) and (rect_y3 <= mouse_click_position[1] and mouse_click_position[1] <= rect_y3 + rect_height3):
          button_pressed3 = True

        else:
          button_pressed3 = False

    # Set the screen background
        if button_pressed3:
          background_image = pygame.image.load("RAM.jpg").convert()
        else:
          background_image = pygame.image.load("Homeimage.jpg").convert()

#HARD DRIVE BUTTON PRESS IF STATEMENT
        if (rect_x4 <= mouse_click_position[0] and mouse_click_position[0] <= rect_x4 + rect_width4) and (rect_y4 <= mouse_click_position[1] and mouse_click_position[1] <= rect_y4 + rect_height4):
          button_pressed4 = True

        else:
          button_pressed4 = False

    # Set the screen background
        if button_pressed4:
          background_image = pygame.image.load("Harddrive.jpg").convert()
        else:
          background_image = pygame.image.load("Homeimage.jpg").convert()

#GRAPHICS CARD BUTTON PRESS IF STATEMENT
        if (rect_x5 <= mouse_click_position[0] and mouse_click_position[0] <= rect_x5 + rect_width5) and (rect_y5 <= mouse_click_position[1] and mouse_click_position[1] <= rect_y5 + rect_height5):
          button_pressed5 = True

        else:
          button_pressed5 = False

    # Set the screen background
        if button_pressed5:
          background_image = pygame.image.load("Graphicscard.jpg").convert()
        else:
          background_image = pygame.image.load("Homeimage.jpg").convert()

#POWERSUPPLY BUTTON PRESS IF STATEMENT
        if (rect_x6 <= mouse_click_position[0] and mouse_click_position[0] <= rect_x6 + rect_width6) and (rect_y6 <= mouse_click_position[1] and mouse_click_position[1] <= rect_y6 + rect_height6):
          button_pressed6 = True

        else:
          button_pressed6 = False

    # Set the screen background
        if button_pressed6:
          background_image = pygame.image.load("Powersupply.jpg").convert()
        else:
          background_image = pygame.image.load("Homeimage.jpg").convert()

    # --- Game logic should go here
# Get the current mouse position. This returns the position

# as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    player_x = player_position[0] - 50
    player_y = player_position[1] - 50
  
    # Copy image to screen:
    screen.blit(background_image, background_position)
    if button_pressed:
      screen.blit (background_image, background_position)
    elif button_pressed1:
      screen.blit (image_CPU, background_position)
    elif button_pressed2:
      screen.blit (image_motherboard, background_position)
    elif button_pressed3:
      screen.blit (image_RAM, background_position)
    elif button_pressed4:
      screen.blit (image_harddrive, background_position)
    elif button_pressed5:
      screen.blit (image_graphicscard, background_position)
    elif button_pressed6:
      screen.blit (image_powersupply, background_position)
    
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, black, [rect_x, rect_y, rect_width, rect_height])

    pygame.draw.rect(screen, blue, [rect_x1, rect_y1, rect_width1, rect_height1])

    pygame.draw.rect(screen, green, [rect_x2, rect_y2, rect_width2, rect_height2])

    pygame.draw.rect(screen, beige, [rect_x3, rect_y3, rect_width3, rect_height3])

    pygame.draw.rect(screen, yellow, [rect_x4, rect_y4, rect_width4, rect_height4])   

    pygame.draw.rect(screen, brown, [rect_x5, rect_y5, rect_width5, rect_height5]) 

    pygame.draw.rect(screen, pink, [rect_x6, rect_y6, rect_width6, rect_height6])
    
    #Set font, size
    font = pygame.font.SysFont('Cambria', 14, True, False)

    text = font.render(
        " CHANGE PAGE ->",True, beige)
    screen.blit(text, [90.3, 373.5])
    
    text = font.render(
        "CHANGE PAGE ->", True, black)
    screen.blit(text, [90, 373])  

    #Set other font, size
    font = pygame.font.SysFont('Cambria', 14, True, False)
    
    text = font.render(
        "HOME", True, white)
    screen.blit(text, [450, 20])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()