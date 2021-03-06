# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 18:46:58 2016

@author: jessime
"""

TYPE_STATS = [{'name' : 'Basic',
               'health' : 100,
               'pause' : 1,
               'attack' : 4,
               'attack_pause' : 1
               },
              {'name' : 'Tank',
               'health' : 300,
               'pause' : 2,
               'attack' : 9,
               'attack_pause' : 1
               },
              {'name' : 'Speedy',
               'health' : 75,
               'pause' : .5,
               'attack' : 2,
               'attack_pause' : .3
               }
               ]

class Zombie():

    def __init__(self, level, pos, board):
        self.level = level
        self.pos = pos
        self.board = board

        self.name = TYPE_STATS[self.level]['name']
        self.health = TYPE_STATS[self.level]['health']
        self.pause = TYPE_STATS[self.level]['pause']
        self.attack = TYPE_STATS[self.level]['attack']
        self.attack_pause = TYPE_STATS[self.level]['attack_pause']
        self.time_till_move = self.pause
        self.is_frozen = False

        self.spawn()

    def __str__(self):
        return '{}Zombie({}, {})'.format(self.name, self.health, self.pos[1])

    def __repr__(self):
        return str(self)

    def freeze(self):
        if not self.is_frozen:
            self.is_frozen = True
            self.pause *= 2

    def left_pos(self):
        return [self.pos[0], self.pos[1] - 1]

    def spawn(self):
        self.board[self.pos].append(self)
        self.board.items['zombies'].append(self)

    def do_attack(self, timedelta):
        if self.attack_pause <= 0:
            self.attack_pause = TYPE_STATS[self.level]['attack_pause']
            contains_plant = self.board.is_plant(self.left_pos())
            if any(contains_plant):
                plant = self.board[self.left_pos()][contains_plant.index(True)]
                plant.health -= self.attack
        else:
            self.attack_pause -= timedelta

    def move(self, timedelta):
        if self.time_till_move <= 0:
            self.time_till_move = self.pause
            contains_plant = self.board.is_plant(self.left_pos())
            if not any(contains_plant):
                index = self.board[self.pos].index(self)
                del self.board[self.pos][index]
                self.board[self.left_pos()].append(self)
                self.pos[1] -= 1

        else:
            self.time_till_move -= timedelta

    def alive(self):
        return self.health > 0

    def update(self, timedelta):
        self.move(timedelta)
        self.do_attack(timedelta)
        return self.pos[1] == 0