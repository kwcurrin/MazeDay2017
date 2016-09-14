# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:26:44 2016

@author: jessime
"""

import time

class Plant():

    def __init__(self, pos, board):
        self.pos = pos
        self.board = board
        self.level = 1
        self.health = 100

    def alive(self):
        return self.health > 0

class Sun():

    def __init__(self, pos, spawn_time):
        self.pos = pos
        self.lifetime = 10
        self.spawn_time = spawn_time

    def __str__(self):
        return 'Sun'

    def __repr__(self):
        return str(self)

    def alive(self):
        return self.lifetime > (time.time() - self.spawn_time)

class Sunflower(Plant):

    def __init__(self, pos, board):
        super().__init__(pos, board)
        self.reload_time = 20
        self.time_til_reload = 20
        self.suns = 0

    def __str__(self):
        return 'Sunflower'

    def __repr__(self):
        return str(self) # Advised against http://stackoverflow.com/questions/727761/python-str-and-lists

    def spawn(self, timedelta):
        self.time_til_reload -= timedelta
        if self.time_til_reload <= 0:
            new_sun = Sun(self.pos, time.time())
            self.board[self.pos].append(new_sun)
            self.board.items['suns'].append(new_sun)
            self.time_til_reload = self.reload_time

    def level_up(self):
        pass #Maybe later