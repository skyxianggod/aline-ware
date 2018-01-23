#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Settings(object):

    def __init__(self):
        '''窗口和背景色的设置'''
        self.screen_width = 1200
        self.screen_hight = 800
        self.bg_color = (230,230,230)
        '''飞机速度设置'''
        self.ship_speed=2

        '''射击的设置'''
        self.bullet_speed = 1
        self.bullet_wight = 3
        self.bullet_hight = 15
        self.bullet_color = 60,60,60
