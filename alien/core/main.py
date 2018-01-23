#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
import  pygame
from pygame.sprite import Group
from alien.core.ship import  Ship
from alien.core.bullet import Bullet
from alien.conf.settings import Settings
from alien.core.aline import Aline
class run(object):
    def __init__(self):
        self.ALSettings=Settings()
        self.screen = pygame.display.set_mode(
            (self.ALSettings.screen_width,self.ALSettings.screen_hight)
        )
        self.ALship=Ship(self.screen)
        self.ALaline=Aline(self.ALSettings,self.screen)


    def check_event(self,bullets):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_down_event(event,bullets)
            elif event.type == pygame.KEYUP:
                self.check_up_event(event)

    def check_up_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ALship.move_right=False
        if event.key == pygame.K_LEFT:
            self.ALship.move_left=False

    def check_down_event(self,event,bullets):
        if event.key == pygame.K_RIGHT:
            self.ALship.move_right=True
        if event.key == pygame.K_LEFT:
            self.ALship.move_left=True
        elif event.key == pygame.K_SPACE:
            new_bullet = Bullet(self.ALSettings,self.screen,self.ALship)
            bullets.add(new_bullet)


    def flush_screen(self,bullets,alines):
        self.screen.fill(self.ALSettings.bg_color)
        for bullet in bullets.sprites():
            bullet.move_bullet()
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        for aline in alines.sprites():
            aline.move()
            aline.blitme()
        self.ALship.blitme()
        pygame.display.flip()



    def get_aline_number(self,settings,aline_width):

        available_space_x = settings.screen_width - 2*aline_width
        number_alines_x = int(available_space_x/(2*aline_width))
        return number_alines_x

    def get_aline_rows(self,settings,aline_height,ship_height):
        available_space_y=(settings.screen_hight - (3*aline_height)- ship_height)
        number_rows = int(available_space_y/(3*aline_height))
        return  number_rows


    def creat_alines(self,settings,alines,screen,aline_number,row_number):

        aline = Aline(settings,screen)
        aline_width = aline.rect.width
        aline.x = aline_width + 2 * aline_width * aline_number
        aline.rect.x = aline.x
        aline.rect.y = aline.rect.height + 2 * aline.rect.height * row_number
        alines.add(aline)

    def creat_fleet_aline(self,settings,screen,alines,ship):
        alien = Aline(settings,screen)
        number_alines_x = self.get_aline_number(settings,alien.rect.width)
        number_alines_y = self.get_aline_rows(settings,alien.rect.height,ship.rect.height)
        print(number_alines_y,"}}}}}")
        for alien_row in range(number_alines_y):
            for aline_number in range(number_alines_x):
                self.creat_alines(settings,screen,alines,aline_number,alien_row)


    def running(self):
        bullets = Group()
        alines = Group()
        self.creat_fleet_aline(self.ALSettings,alines,self.screen,self.ALship)
        while True:
            self.check_event(bullets)
            self.ALship.moving()
            self.flush_screen(bullets,alines)



A=run()
A.running()