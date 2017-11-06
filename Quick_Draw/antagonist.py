import pygame#to initialize pygame

class Antagonist():#to create the antagonist class (player 2)
    def __init__(self,screen,pos):
        self.screen = screen#to load player 2's character onto the screen
        self.image = pygame.image.load("aimleft.png")#to load player 2's charcater
        self.rect = self.image.get_rect()#to rect player 2's character
        self.screen_rect = screen.get_rect()#to rect the screen
        self.rect.center = pos#to set player 2's character's position

    def blitme(self):#to blit player 2's character
        self.screen.blit(self.image, self.rect)
