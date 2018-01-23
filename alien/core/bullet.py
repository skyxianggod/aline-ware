#! /usr/bin/env python
# -*- coding: utf-8 -*-
# from conf.settings import Settings as set
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,settings.bullet_wight,settings.bullet_hight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def move_bullet(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)