import pygame#to initialize pygame

class Protagonist():#to make protagonist class(Player 1 )
    def __init__(self,screen,pos):
        self.screen = screen#so player 1 's character will load on the screen
        self.image = pygame.image.load("aimright.png")#to load player 1's character image
        self.rect = self.image.get_rect()#to rect player 1's character
        self.screen_rect = screen.get_rect()#to rect the screen
        self.rect.center = pos#to set player1's position

    def blitme(self):#to blit player 1 onto the screen
        self.screen.blit(self.image, self.rect)

