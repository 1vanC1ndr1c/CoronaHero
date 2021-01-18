import pygame
import random
from corona_hero_app.sprites.main_character import MainCharacter
import os
from pathlib import Path
import pygame

class MainMenu:
    spritesPath = os.path.abspath(os.path.join(str(Path(__file__).parent.parent.parent)))
    buttons = {}
    background = None
    hlp = ""
    about = ""
    button_img = None

    def __init__(self):
        self.which_menu = 0
        self.background = os.path.join(self.spritesPath, "resources","sprites","MainMenu-Background.png")
        self.about = "This game was made as project on University in zagreb, Faculty of\n electrical engineering and computing, on course “Digital education.”\n Game is made to learn players about safety measures with COVID19\n and is sprite-based and retro-style. All the graphics, sounds and\n music are made from scratch with GIMP and the engine is PyGame.\n"
        self.about+="Members of the team who made this game are:\n\n"
        self.about+="Ivan Mihaljević “Fuzz Mihi” - story, graphics, artwork, UI design,\n" 
        self.about+="music, sounds, aditional programming\n\n"
        self.about+="Mislav Bajan - level design, level coding, aditional programming\n\n"
        self.about+="Ivan Cindrić - Programming\n\n"
        self.about+="Zvonimir Zovak - Programming\n\n"
        self.hlp = "Controls:\n\nMove left/right - Left/Right arrow\nJump - Up arrow\nShoot - Space\n\n if you do something wrong, or touch covid, you have to wash your hands by reaching sink!"
        
    def add_button(self,x,y,label):
        self.buttons[label] = (x,y)

    def make_menu(self,win,which_menu,pos):

        myfont = pygame.font.SysFont("Arial Black", 32)

        if(which_menu == 0):

            self.background = os.path.join(self.spritesPath, "resources","sprites","MainMenu-Background.png")
            button_img1 = pygame.image.load(os.path.join(self.spritesPath, "resources","sprites","Button.png"))
            img1_rect = pygame.Rect(self.buttons["new game"][0],self.buttons["new game"][1],250,77)
            win.blit(button_img1, self.buttons["new game"])
            label = myfont.render("New game", 1, (0,0,0))
            twidth,theight = myfont.size("New game")
            win.blit(label,(self.buttons["new game"][0]+(125-twidth/2),self.buttons["new game"][1]+(77/2-theight/2)))

            button_img2 = pygame.image.load(os.path.join(self.spritesPath, "resources","sprites","Button.png"))
            img2_rect = pygame.Rect(self.buttons["help"][0],self.buttons["help"][1],250,77)
            win.blit(button_img2, self.buttons["help"])
            label = myfont.render("Help", 1, (0,0,0))
            twidth,theight = myfont.size("Help")
            win.blit(label,(self.buttons["help"][0]+(125-twidth/2),self.buttons["help"][1]+(77/2-theight/2)))
            
            button_img3 = pygame.image.load(os.path.join(self.spritesPath, "resources","sprites","Button.png"))
            img3_rect = pygame.Rect(self.buttons["about"][0],self.buttons["about"][1],250,77)
            win.blit(button_img3, self.buttons["about"])
            label = myfont.render("About", 1, (0,0,0))
            twidth,theight = myfont.size("About")
            win.blit(label,(self.buttons["about"][0]+(125-twidth/2),self.buttons["about"][1]+(77/2-theight/2)))
            
            button_img4 = pygame.image.load(os.path.join(self.spritesPath, "resources","sprites","Button.png"))
            img4_rect = pygame.Rect(self.buttons["exit"][0],self.buttons["exit"][1],250,77)
            win.blit(button_img2, self.buttons["exit"])
            label = myfont.render("Exit", 1, (0,0,0))
            twidth,theight = myfont.size("Exit")
            win.blit(label,(self.buttons["exit"][0]+(125-twidth/2),self.buttons["exit"][1]+(77/2-theight/2)))

            if(pos is not None):
                
                if img1_rect.collidepoint(pos):
                    return 1

                elif img2_rect.collidepoint(pos):
                    return 2

                elif img3_rect.collidepoint(pos):
                    return 3
                
                elif img4_rect.collidepoint(pos):
                    return 4

                else:
                    return which_menu
            else:
                return 0
        
        elif(which_menu == 2 or which_menu == 3):
            self.background = os.path.join(self.spritesPath, "resources","sprites","Background-CaveBetter.png")
            button_img1 = pygame.image.load(os.path.join(self.spritesPath, "resources","sprites","Button.png"))
            img1_rect = pygame.Rect(self.buttons["back"][0],self.buttons["back"][1],250,77)
            win.blit(button_img1, self.buttons["back"])
            label = myfont.render("Back", 1, (0,0,0))
            twidth,theight = myfont.size("Back")
            win.blit(label,(self.buttons["back"][0]+(125-twidth/2),self.buttons["back"][1]+(77/2-theight/2)))

            if(which_menu == 2):
                sz = 0
                for h in self.hlp.split("\n"):
                    label = myfont.render(h, 1, (170,170,170))
                    twidth,theight = myfont.size(h)
                    win.blit(label,(0,sz))
                    sz+=34
            
            elif(which_menu == 3):
                sz = 0
                for h in self.about.split("\n"):
                    label = myfont.render(h, 1, (170,170,170))
                    twidth,theight = myfont.size(h)
                    win.blit(label,(0,sz))
                    sz+=34

            if(pos is not None):
                
                if img1_rect.collidepoint(pos):
                    return 0
                
                else:
                    return which_menu

            else:
                return which_menu
                
            
