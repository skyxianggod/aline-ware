#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from conf.settings import Settings
class Ship(object):

    def __init__(self,screen):
        self.ship_speed = Settings().ship_speed
        self.screen = screen
        self.image=pygame.image.load('F:\\aline-ware\\alien\\img\\1.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        # self.rect.center=float(self.rect.centerx)
        self.rect.bottom=self.screen_rect.bottom
        self.move_right=False
        self.move_left=False

    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def moving(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx +=self.ship_speed
        if self.move_left and self.rect.left > 0:
            self.rect.centerx -=self.ship_speed

        # self.rect.centerx=self.rect.center

