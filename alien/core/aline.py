#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

from alien.conf.settings import Settings


class Aline(Sprite):

    def __init__(self,settings,screen):
        super(Aline,self).__init__()
        self.screen = screen
        self.image =pygame.image.load('F:\\aline-ware\\alien\\img\\2.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def move(self):
        self.x += Settings().alien_spped
        self.rect.x = self.x
